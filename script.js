// Depois de publicar a API Flask, coloque aqui o endereço dela, por exemplo:
// const API_URL = "https://seu-backend.exemplo.com";
const API_URL = "";

document.getElementById("ano").textContent = new Date().getFullYear();

const formulario = document.getElementById("form-cadastro");
const mensagem = document.getElementById("mensagem");

formulario.addEventListener("submit", async (evento) => {
  evento.preventDefault();
  mensagem.textContent = "";

  if (!API_URL) {
    mensagem.textContent = "O formulário está pronto. O cadastro será ativado quando o servidor Python for publicado.";
    return;
  }

  const dados = {
    nome: formulario.nome.value.trim(),
    email: formulario.email.value.trim(),
    telefone: formulario.telefone.value.trim()
  };

  try {
    const resposta = await fetch(`${API_URL}/api/cadastro`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dados)
    });
    const resultado = await resposta.json();

    if (!resposta.ok) throw new Error(resultado.erro || "Não foi possível concluir o cadastro.");
    mensagem.textContent = "Cadastro realizado com sucesso! Obrigado.";
    formulario.reset();
  } catch (erro) {
    mensagem.textContent = erro.message || "Não foi possível conectar ao servidor. Tente novamente.";
  }
});