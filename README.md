<div align="center">

# AcolheAI

**Chatbot experimental de acolhimento emocional inicial com inteligência artificial.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_API-F55036?style=for-the-badge&logo=groq&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

[Repositório](https://github.com/thiagorodrigues07/AcolheAI)

</div>

## Sobre o projeto

O **AcolheAI** é um projeto acadêmico experimental que utiliza inteligência artificial para oferecer uma experiência inicial de conversa acolhedora. A aplicação combina uma interface web com uma API desenvolvida em Flask e integração com a API da Groq.

O assistente foi configurado para responder com linguagem natural, empatia e cuidado, incentivando a reflexão e, quando apropriado, a busca por apoio humano e profissional.

> **Importante:** o AcolheAI é um protótipo experimental. Não substitui psicólogos, médicos, serviços de emergência ou qualquer atendimento profissional.

## Funcionalidades

- Interface de chat para envio e recebimento de mensagens.
- Integração com a API da Groq e o modelo `llama-3.3-70b-versatile`.
- Envio de histórico de conversa para manter o contexto.
- Validação do conteúdo recebido pela API.
- Limite de tamanho para mensagens e histórico.
- Endpoint de status para verificar a disponibilidade da aplicação.
- Tratamento de falhas na comunicação com o serviço de IA.

## Tecnologias

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem do back-end |
| Flask | Aplicação web e criação dos endpoints |
| Groq API | Integração com o serviço de inteligência artificial |
| Llama 3.3 70B Versatile | Modelo de linguagem configurado no projeto |
| HTML e CSS | Estrutura e apresentação da interface |
| JavaScript | Interações do chat no navegador |

## Estrutura do projeto

```text
AcolheAI/
├── app.py
├── main.py
├── requirements.txt
├── core/
│   └── prompt_mestre.py
├── services/
│   └── ia_services.py
└── public/
    ├── index.html
    ├── style.css
    └── app.js
```

## Como executar localmente

### Pré-requisitos

- Python 3.10 ou superior
- Git
- Uma chave de API da Groq

### 1. Clone o repositório

```bash
git clone https://github.com/thiagorodrigues07/AcolheAI.git
cd AcolheAI
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a chave da API

No PowerShell:

```powershell
$env:GROQ_API_KEY="sua-chave-aqui"
```

Não compartilhe sua chave e não a inclua em arquivos versionados.

### 5. Inicie a aplicação

```bash
python main.py
```

Acesse `http://127.0.0.1:5500` no navegador.

## Endpoints disponíveis

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/` | Exibe a interface do chat |
| `POST` | `/chat` | Envia uma mensagem para o serviço de IA |
| `GET` | `/status` | Retorna o estado da aplicação |

Exemplo de corpo para `POST /chat`:

```json
{
  "mensagem": "Olá, gostaria de conversar.",
  "historico": []
}
```

## Aprendizados e objetivos técnicos

- Desenvolvimento de aplicações web com Python e Flask.
- Integração com APIs externas de inteligência artificial.
- Organização do código em módulos e serviços.
- Construção e validação de endpoints REST.
- Gerenciamento de variáveis de ambiente.
- Tratamento de erros e limites de entrada.
- Criação e refinamento de instruções para modelos de linguagem.

## Próximas melhorias

- Implementar testes automatizados para os endpoints.
- Aprimorar a observabilidade e os registros de execução.
- Revisar continuamente os mecanismos de segurança e encaminhamento para apoio humano.
- Avaliar estratégias de privacidade e retenção de dados.

## Autor

**Thiago Rodrigues**

- GitHub: [@thiagorodrigues07](https://github.com/thiagorodrigues07)
- LinkedIn: [Thiago Rodrigues](https://www.linkedin.com/in/thiago-rodrigues-810b06367/)

