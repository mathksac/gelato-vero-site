import os
import re
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": os.getenv("FRONTEND_ORIGIN", "*")}})

BANCO = os.getenv("DATABASE_PATH", "cadastros.db")


def conectar():
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS cadastros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                telefone TEXT,
                criado_em TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)


@app.get("/")
def inicio():
    return jsonify({"mensagem": "API da Gelato Vero está funcionando."})


@app.get("/api/saude")
def saude():
    return jsonify({"status": "ok"})


@app.post("/api/cadastro")
def cadastrar():
    dados = request.get_json(silent=True) or {}
    nome = str(dados.get("nome", "")).strip()
    email = str(dados.get("email", "")).strip().lower()
    telefone = str(dados.get("telefone", "")).strip()

    if not nome or len(nome) > 100:
        return jsonify({"erro": "Informe um nome válido."}), 400
    if len(email) > 150 or not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email):
        return jsonify({"erro": "Informe um e-mail válido."}), 400
    if len(telefone) > 20:
        return jsonify({"erro": "Telefone muito longo."}), 400

    try:
        with conectar() as conexao:
            conexao.execute(
                "INSERT INTO cadastros (nome, email, telefone) VALUES (?, ?, ?)",
                (nome, email, telefone or None)
            )
        return jsonify({"mensagem": "Cadastro realizado com sucesso."}), 201
    except sqlite3.IntegrityError:
        return jsonify({"erro": "Este e-mail já está cadastrado."}), 409


criar_tabela()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)