# Auditoria — AcolheAI

## Encontrado

A cópia de origem em uma pasta tinha arquivos vazios; o código utilizável estava em um ZIP aninhado. O backend recebia histórico sem validar formato/tamanho, rodava com modo debug e devolvia detalhes internos de exceções. A interface inicial inseria texto do usuário via `innerHTML`, permitindo injeção de HTML. A lista de dependências tinha nome incorreto e estava vazia.

## Corrigido anteriormente

Consolidada a cópia funcional; corrigida a lista de dependências; adicionados limites e validação para mensagem e histórico; chave da API validada por variável de ambiente; erros internos não são devolvidos ao cliente; debug desligado; texto exibido com `textContent`; incluídos README, `.gitignore` e licença MIT. CORS foi removido pois a interface e API são servidas pela mesma origem.

## Direção visual aprovada

Interface editorial de conversa, com grade assimétrica, verde profundo e terracota, Newsreader e DM Sans. Não usa imagens genéricas, emojis, cards promocionais, depoimentos, métricas inventadas ou texto de venda. As chamadas "Iniciar conversa" levam diretamente ao chat. A interface informa o processamento por IA, recomenda evitar dados pessoais e explica que não substitui acompanhamento profissional.

## Melhorias implementadas

Redesenhada a interface responsiva em HTML, CSS e JavaScript nativos, sem animações de rolagem. Adicionados estados acessíveis de envio e erro, navegação por teclado e preservação da mensagem em caso de falha. O histórico continua apenas na conversa atual. O contrato JSON `POST /chat` foi preservado. Uma rota HTML `POST /conversa` permite usar o formulário sem JavaScript, com respostas renderizadas no servidor, conteúdo escapado pelo Jinja e verificação de origem da requisição.

## Verificação

A sintaxe de `public/app.js` passou em `node --check`. O Flask test client confirmou HTTP 200 para a página, CSS, JavaScript e `/status`; o chat JSON mockado respondeu 200; o formulário sem JavaScript respondeu 200 e escapou texto semelhante a HTML; envios de outra origem ao formulário são bloqueados com 403; sem chave configurada, ambos os envios responderam 503 sem expor a mensagem interna de configuração. O envio real à Groq não foi testado. A revisão visual em navegador não foi concluída porque o navegador disponível não conseguiu conectar ao servidor local de desenvolvimento.

## Pendências e sugestões

O prompt do backend contém referências de apoio para situações de crise, mas a interface não oferece orientação específica. Revisar a precisão e adequação dessas referências continua sendo uma pendência antes de divulgar o sistema como apoio em crise. Configurar rate limiting antes de abrir o chat publicamente.
