# AcolheAI

Chatbot experimental de acolhimento emocional inicial, feito como projeto acadêmico. A aplicação envia as mensagens à API da Groq e exibe as respostas no navegador. Não substitui atendimento profissional.

## Tecnologias

Python, Flask, Groq API, HTML, CSS e JavaScript.

## Instalação e execução

1. Instale Python 3.10 ou superior.
2. Crie e ative um ambiente virtual (`python -m venv .venv`).
3. Instale as dependências: `pip install -r requirements.txt`.
4. Defina `GROQ_API_KEY` no ambiente. No PowerShell: `$env:GROQ_API_KEY="sua-chave"`.
5. Execute `python main.py` e abra http://127.0.0.1:5500.

## Exemplo de uso

Envie uma mensagem no campo do chat. O endpoint `POST /chat` recebe JSON com `mensagem` e, opcionalmente, `historico`.

## Objetivo de aprendizagem

Praticar integração entre uma interface web, uma API em Flask e um serviço de inteligência artificial.

## Hospedagem na Vercel

O projeto exporta a aplicação Flask por `app.py` e mantém os arquivos do navegador em `public/`, estrutura reconhecida pela Vercel. Importe este repositório na Vercel, mantenha a pasta raiz como diretório do projeto, adicione `GROQ_API_KEY` em **Settings → Environment Variables** e faça o deploy. Configure a variável para Production (e Preview se quiser testar prévias). Nunca coloque a chave em arquivos do repositório.
