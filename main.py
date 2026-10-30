import json
import os
from urllib.parse import urlsplit

from flask import Flask, abort, jsonify, render_template, request, send_from_directory

from core.prompt_mestre import PromptMestre
from services.ia_services import IAService

app = Flask(__name__, static_folder=None)
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024

prompt_mestre = PromptMestre()
MAX_MENSAGEM = 4000
MAX_HISTORICO = 20
HISTORICO_FORMULARIO = 18


def validar_conversa(mensagem, historico):
    if not isinstance(mensagem, str) or not mensagem.strip():
        return "A mensagem não pode estar vazia.", None, None

    mensagem = mensagem.strip()
    if len(mensagem) > MAX_MENSAGEM:
        return f"A mensagem deve ter até {MAX_MENSAGEM} caracteres.", None, mensagem
    if not isinstance(historico, list) or len(historico) >= MAX_HISTORICO:
        return "O histórico enviado é inválido ou muito longo.", None, mensagem

    mensagens_validas = []
    for item in historico:
        if not isinstance(item, dict):
            return "O histórico enviado é inválido.", None, mensagem
        role, conteudo = item.get("role"), item.get("content")
        if role not in {"user", "assistant"} or not isinstance(conteudo, str):
            return "O histórico enviado é inválido.", None, mensagem
        if len(conteudo) > MAX_MENSAGEM:
            return "Há uma mensagem muito longa no histórico.", None, mensagem
        mensagens_validas.append({"role": role, "content": conteudo})

    return None, mensagens_validas, mensagem


def obter_resposta(mensagem, historico):
    mensagens = [*historico, {"role": "user", "content": mensagem}]
    return IAService().enviar_mensagem(mensagens, prompt_mestre.get_prompt())


@app.get("/")
def index():
    return send_from_directory(os.path.join(app.root_path, "public"), "index.html")


@app.get("/style.css")
def estilo():
    return send_from_directory(os.path.join(app.root_path, "public"), "style.css")


@app.get("/app.js")
def javascript():
    return send_from_directory(os.path.join(app.root_path, "public"), "app.js")


@app.post("/chat")
def chat():
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return jsonify({"erro": "Envie os dados em formato JSON."}), 400

    erro, historico, mensagem = validar_conversa(
        dados.get("mensagem"), dados.get("historico", [])
    )
    if erro:
        return jsonify({"erro": erro}), 400

    try:
        return jsonify({"resposta": obter_resposta(mensagem, historico)})
    except RuntimeError:
        return jsonify({"erro": "O chat está indisponível no momento."}), 503
    except Exception:
        app.logger.exception("Falha ao consultar o serviço de IA")
        return jsonify({"erro": "Não foi possível obter uma resposta agora."}), 502


@app.post("/conversa")
def conversa_sem_javascript():
    origem = request.headers.get("Origin")
    if origem and urlsplit(origem).netloc.lower() != request.host.lower():
        abort(403)

    mensagem = request.form.get("mensagem", "")
    try:
        historico_enviado = json.loads(request.form.get("historico", "[]"))
    except (TypeError, json.JSONDecodeError):
        historico_enviado = []

    erro, historico, mensagem = validar_conversa(mensagem, historico_enviado)
    if erro:
        return render_template(
            "conversa.html", historico=historico_enviado if isinstance(historico_enviado, list) else [],
            rascunho=mensagem or "", erro=erro,
        ), 400

    try:
        resposta = obter_resposta(mensagem, historico)
        conversa = [
            *historico,
            {"role": "user", "content": mensagem},
            {"role": "assistant", "content": resposta},
        ][-HISTORICO_FORMULARIO:]
        return render_template(
            "conversa.html", historico=conversa, rascunho="", erro=None,
        )
    except RuntimeError:
        return render_template(
            "conversa.html", historico=historico, rascunho=mensagem,
            erro="O chat está indisponível no momento. Tente novamente mais tarde.",
        ), 503
    except Exception:
        app.logger.exception("Falha ao consultar o serviço de IA no envio sem JavaScript")
        return render_template(
            "conversa.html", historico=historico, rascunho=mensagem,
            erro="Não foi possível obter uma resposta agora. Seu texto continua disponível para tentar novamente.",
        ), 502


@app.get("/status")
def status():
    return jsonify({"status": "online", "bot": "AcolheAI"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5500")), debug=False)
