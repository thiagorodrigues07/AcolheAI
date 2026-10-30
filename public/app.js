const form = document.querySelector("#chat-form");
const input = document.querySelector("#message-input");
const sendButton = document.querySelector("#send-button");
const messages = document.querySelector("#messages");
const statusMessage = document.querySelector("#chat-status");
const historyInput = document.querySelector("#history-input");

const history = [];
let isSending = false;

function setStatus(message, isError = false) {
  statusMessage.textContent = message;
  statusMessage.classList.toggle("is-error", isError);
}

function updateSendButton() {
  sendButton.disabled = isSending || !input.value.trim();
  sendButton.textContent = isSending ? "Enviando" : "Enviar";
}

function formatTime() {
  return new Intl.DateTimeFormat("pt-BR", { hour: "2-digit", minute: "2-digit" }).format(new Date());
}

function addMessage(text, role, pending = false) {
  const article = document.createElement("article");
  article.className = "message " + (role === "user" ? "user-message" : "assistant-message");
  if (pending) article.classList.add("message-pending");
  const paragraph = document.createElement("p");
  paragraph.textContent = text;
  const time = document.createElement("time");
  time.className = "message-time";
  time.dateTime = new Date().toISOString();
  time.textContent = formatTime();
  article.append(paragraph, time);
  messages.append(article);
  messages.scrollTop = messages.scrollHeight;
  return article;
}

function friendlyError(status) {
  if (status === 503) return "O chat está indisponível no momento. Tente novamente mais tarde.";
  if (status === 400) return "Não foi possível enviar esta mensagem. Confira o texto e tente novamente.";
  return "Não consegui obter uma resposta agora. Seu texto continua aqui para você tentar novamente.";
}

input.addEventListener("input", updateSendButton);
input.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    form.requestSubmit();
  }
});

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const message = input.value.trim();
  if (!message || isSending) return;

  isSending = true;
  input.disabled = true;
  updateSendButton();
  setStatus("Aguarde um instante enquanto preparo uma resposta.");
  const userMessage = addMessage(message, "user", true);
  const loadingMessage = addMessage("A IA está preparando uma resposta.", "assistant", true);

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mensagem: message, historico: history.slice(-18) })
    });
    let data = {};
    try { data = await response.json(); } catch { data = {}; }
    if (!response.ok || typeof data.resposta !== "string" || !data.resposta.trim()) {
      throw new Error(String(response.status || 502));
    }

    history.push({ role: "user", content: message }, { role: "assistant", content: data.resposta });
    if (history.length > 18) history.splice(0, history.length - 18);
    historyInput.value = JSON.stringify(history);
    userMessage.classList.remove("message-pending");
    loadingMessage.remove();
    addMessage(data.resposta, "assistant");
    input.value = "";
    setStatus("");
  } catch (error) {
    userMessage.remove();
    loadingMessage.remove();
    setStatus(friendlyError(Number(error.message)), true);
  } finally {
    isSending = false;
    input.disabled = false;
    updateSendButton();
    input.focus();
  }
});

updateSendButton();
