# Gelato Vero

Site institucional da sorveteria Gelato Vero.

## Tecnologias
- Frontend: HTML, CSS e JavaScript
- Backend: Python, Flask e SQLite

## Rodar o backend localmente
1. Entre na pasta `backend`.
2. Crie um ambiente virtual: `python -m venv .venv`.
3. Ative o ambiente virtual.
4. Instale: `pip install -r requirements.txt`.
5. Execute: `python app.py`.
6. A API ficará em `http://localhost:5000`.

## Publicação
O GitHub Pages hospeda os arquivos estáticos da raiz (`index.html`, `style.css` e `script.js`), mas não executa Python. Publique a pasta `backend` em um serviço compatível com Flask e configure a variável `API_URL` em `script.js` com o endereço público da API.

## Identidade visual
Paleta provisória em rosa morango, bege e marrom. A logo original ainda precisa ser adicionada ao repositório.
