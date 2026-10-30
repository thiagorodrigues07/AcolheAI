import os

from flask import Flask, jsonify, request, send_from_directory

from core.prompt_mestre import PromptMestre
from services.ia_services import IAService

app = Flask(__name__, static_folder=None)
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024

prompt_mestre = PromptMestre()
MAX_MENSAGEM = 4000
MAX_HISTORICO = 20


@app.get("/")
def index():
    return send_from_directory(os.path.join(app.root_path, "public"), "index.html")


@app.get("/style.css")
def estilo():
    return send_from_directory(os.path.join(app.root_path, "public"), "style.css")


@app.post("/chat")
def chat():
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return jsonify({"erro": "Envie os dados em formato JSON."}), 400

    mensagem = dados.get("mensagem")
    historico = dados.get("historico", [])
    if not isinstance(mensagem, str) or not mensagem.strip():
        return jsonify({"erro": "A mensagem não pode estar vazia."}), 400
    mensagem = mensagem.strip()
    if len(mensagem) > MAX_MENSAGEM:
        return jsonify({"erro": f"A mensagem deve ter até {MAX_MENSAGEM} caracteres."}), 400
    if not isinstance(historico, list) or len(historico) >= MAX_HISTORICO:
        return jsonify({"erro": "O histórico enviado é inválido ou muito longo."}), 400

    mensagens_validas = []
    for item in historico:
        if not isinstance(item, dict):
            return jsonify({"erro": "O histórico enviado é inválido."}), 400
        role, conteudo = item.get("role"), item.get("content")
        if role not in {"user", "assistant"} or not isinstance(conteudo, str):
            return jsonify({"erro": "O histórico enviado é inválido."}), 400
        if len(conteudo) > MAX_MENSAGEM:
            return jsonify({"erro": "Há uma mensagem muito longa no histórico."}), 400
        mensagens_validas.append({"role": role, "content": conteudo})

    mensagens_validas.append({"role": "user", "content": mensagem})
    try:
        resposta = IAService().enviar_mensagem(
            mensagens_validas, prompt_mestre.get_prompt()
        )
        return jsonify({"resposta": resposta})
    except RuntimeError as erro:
        return jsonify({"erro": str(erro)}), 503
    except Exception:
        app.logger.exception("Falha ao consultar o serviço de IA")
        return jsonify({"erro": "Não foi possível obter uma resposta agora."}), 502


@app.get("/status")
def status():
    return jsonify({"status": "online", "bot": "AcolheAI"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5500")), debug=False)

