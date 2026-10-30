import os

from groq import Groq


class IAService:
    """Cliente pequeno para enviar o histórico à API da Groq."""

    MODELO = "llama-3.3-70b-versatile"
    MAX_TOKENS = 1024

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError("Configure a variável de ambiente GROQ_API_KEY.")
        self.cliente = Groq(api_key=api_key)

    def enviar_mensagem(self, historico: list[dict[str, str]], system_prompt: str) -> str:
        mensagens = [{"role": "system", "content": system_prompt}, *historico]
        resposta = self.cliente.chat.completions.create(
            model=self.MODELO,
            max_tokens=self.MAX_TOKENS,
            messages=mensagens,
        )
        conteudo = resposta.choices[0].message.content
        if not conteudo:
            raise RuntimeError("A API retornou uma resposta vazia.")
        return conteudo
