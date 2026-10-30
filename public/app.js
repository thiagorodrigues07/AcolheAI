const form = document.querySelector("#chat-form");
const input = document.querySelector("#message-input");
const sendButton = document.querySelector("#send-button");
const messages = document.querySelector("#messages");
const statusMessage = document.querySelector("#chat-status");
const suggestions = document.querySelector("#suggestions");

const history = [];
let isSending = false;

function setStatus(message, isError = false) {
  statusMessage.textContent = message;
  statusMessage.classList.toggle("is-error", isError);
}

function updateSendButton() {
  sendButton.disabled = isSending || !input.value.trim();
  sendButton.querySelector("span").textContent = isSending ? "Enviando" : "Enviar";
}

function formatTime() {
  return new Intl.DateTimeFormat("pt-BR", { hour: "2-digit", minute: "2-digit" }).format(new Date());
}

function addMessage(text, role, { pending = false } = {}) {
  const article = document.createElement("article");
  article.className = "message " + (role === "user" ? "message-user" : "message-assistant");
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

function addTypingIndicator() {
  const indicator = document.createElement("div");
  indicator.className = "message message-assistant";
  indicator.id = "typing-indicator";
  indicator.setAttribute("aria-label", "A IA está preparando uma resposta");
  const dots = document.createElement("span");
  dots.className = "typing-dots";
  dots.setAttribute("aria-hidden", "true");
  for (let index = 0; index < 3; index += 1) dots.append(document.createElement("span"));
  indicator.append(dots);
  messages.append(indicator);
  messages.scrollTop = messages.scrollHeight;
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

suggestions.addEventListener("click", (event) => {
  const button = event.target.closest("[data-suggestion]");
  if (!button) return;
  input.value = button.dataset.suggestion;
  updateSendButton();
  input.focus();
});

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const message = input.value.trim();
  if (!message || isSending) return;
  isSending = true;
  input.disabled = true;
  updateSendButton();
  setStatus("Aguarde um instante enquanto preparo uma resposta.");
  const userMessage = addMessage(message, "user", { pending: true });
  addTypingIndicator();

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mensagem: message, historico: history.slice(-19) })
    });
    let data = {};
    try { data = await response.json(); } catch { data = {}; }
    if (!response.ok || typeof data.resposta !== "string" || !data.resposta.trim()) {
      throw new Error(String(response.status || 502));
    }
    history.push({ role: "user", content: message }, { role: "assistant", content: data.resposta });
    userMessage.classList.remove("message-pending");
    addMessage(data.resposta, "assistant");
    input.value = "";
    suggestions.hidden = true;
    setStatus("");
  } catch (error) {
    userMessage.remove();
    setStatus(friendlyError(Number(error.message)), true);
  } finally {
    document.querySelector("#typing-indicator")?.remove();
    isSending = false;
    input.disabled = false;
    updateSendButton();
    input.focus();
  }
});

updateSendButton();
