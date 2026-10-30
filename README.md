# AcolheAI

Aplicação web experimental de apoio emocional inicial, desenvolvida como projeto acadêmico. A pessoa conversa com uma interface simples, e as mensagens são processadas pelo serviço de IA configurado. O AcolheAI não substitui acompanhamento profissional.

## Tecnologias

Python, Flask, API da Groq, HTML, CSS, JavaScript e fontes Newsreader e DM Sans do Google Fonts.

## Instalação e execução

1. Instale Python 3.10 ou superior.
2. Crie e ative um ambiente virtual (`python -m venv .venv`).
3. Instale as dependências: `pip install -r requirements.txt`.
4. Defina `GROQ_API_KEY` no ambiente. No PowerShell: `$env:GROQ_API_KEY="sua-chave"`.
5. Execute `python main.py` e abra http://127.0.0.1:5500.

## Uso

Com JavaScript, escreva uma mensagem e pressione Enter ou o botão **Enviar**. Shift + Enter insere uma quebra de linha. Sem JavaScript, use o botão **Enviar**; o formulário envia a mensagem ao endpoint `/conversa` e exibe a resposta em uma página recarregada. O endpoint JSON `POST /chat`, com `mensagem` e `historico`, continua disponível para a interface interativa.

A conversa não é guardada entre sessões. As mensagens são processadas pelo serviço de IA configurado; evite incluir dados pessoais. A interface usa fontes hospedadas pelo Google Fonts.

## Objetivo de aprendizagem

Praticar integração entre uma interface web acessível, uma API em Flask e um serviço de inteligência artificial.

## Hospedagem na Vercel

O projeto exporta a aplicação Flask por `app.py` e mantém os arquivos do navegador em `public/`. Na Vercel, mantenha a pasta raiz como diretório do projeto e configure `GROQ_API_KEY` em **Settings → Environment Variables**, no ambiente Production. Nunca coloque a chave em arquivos do repositório.
