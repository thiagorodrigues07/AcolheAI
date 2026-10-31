# Auditoria — AcolheAI

## Encontrado

A cópia de origem em uma pasta tinha arquivos vazios; o código utilizável estava em um ZIP aninhado. O backend recebia histórico sem validar formato/tamanho, rodava com modo debug e devolvia detalhes internos de exceções. A interface inseria texto do usuário via `innerHTML`, permitindo injeção de HTML. A lista de dependências tinha nome incorreto e estava vazia.

## Corrigido

Consolidada a cópia funcional; corrigida a lista de dependências; adicionados limites e validação para mensagem e histórico; chave da API validada por variável de ambiente; erros internos não são devolvidos ao cliente; debug desligado; texto exibido com `textContent`; incluídos README, `.gitignore` e licença MIT. CORS foi removido pois a interface e API são servidas pela mesma origem.

## Sugestões

Adicionar testes automatizados, configurar limites/rate limiting para uso público e revisar o prompt de segurança antes de apresentar o sistema como apoio em situações de crise. O serviço requer chave Groq e acesso à internet para a conversa.

## Verificação anterior

Página inicial, rota de status, validação de JSON e comportamento sem chave passaram no teste de fumaça local usando Flask test client. A chamada real à Groq não foi testada porque depende de chave e acesso externo.

Preparado o ponto de entrada `app.py` e movidos os arquivos estáticos para `public/` para compatibilidade com a Vercel.

## Redesign da interface

A interface antiga foi substituída por uma experiência responsiva em HTML, CSS e JavaScript nativos. Foram adicionados hierarquia visual mais clara, exemplos opcionais para iniciar a conversa, avisos sobre processamento por IA e limites do sistema, controles acessíveis por teclado, estados de envio e erro, e preservação do rascunho quando a API falha. O contrato `POST /chat` e o formato de histórico foram mantidos. A exibição de mensagens continua usando `textContent` para evitar interpretar conteúdo como HTML.

## Sugestão de segurança

A interface não mostra orientação específica para situações de crise. O prompt do backend contém orientações e referências de apoio; revisar a precisão e adequação dessas referências continua sendo uma pendência antes de divulgar o sistema como apoio em crise.
