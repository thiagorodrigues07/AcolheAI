# Auditoria — AcolheAI

## Encontrado

A cópia de origem em uma pasta tinha arquivos vazios; o código utilizável estava em um ZIP aninhado. Backend recebia histórico sem validar formato/tamanho, rodava com modo debug e devolvia detalhes internos de exceções. A interface inseria texto do usuário via `innerHTML`, permitindo injeção de HTML. A lista de dependências tinha nome incorreto e estava vazia.

## Corrigido

Consolidada a cópia funcional; corrigida a lista de dependências; adicionados limites e validação para mensagem e histórico; chave da API validada por variável de ambiente; erros internos não são devolvidos ao cliente; debug desligado; texto exibido com `textContent`; incluídos README, `.gitignore` e licença MIT. CORS foi removido pois a interface e API são servidas pela mesma origem.

## Sugestões

Adicionar testes automatizados, configurar limites/rate limiting para uso público e revisar o prompt de segurança antes de apresentar o sistema como apoio em situações de crise. O serviço requer chave Groq e acesso à internet para a conversa.

## Verificação

Página inicial, rota de status, validação de JSON e comportamento sem chave passaram no teste de fumaça local usando Flask test client. A chamada real à Groq não foi testada porque depende de chave e acesso externo.


Preparado o ponto de entrada `app.py` e movidos os arquivos estáticos para `public/` para compatibilidade com a Vercel.
