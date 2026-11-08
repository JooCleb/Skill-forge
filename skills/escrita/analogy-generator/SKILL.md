---
name: analogy-generator
description: >-
  Crie analogias com correspondências explícitas e limites de validade no ChatGPT
  Work ou no Codex quando houver código. Use mediante pedido explícito de explicar
  um conceito por analogia, tornar um trecho abstrato intuitivo por comparação,
  ou etapa nomeada de analogia em workflow já autorizado. Não use para mera revisão
  textual, metáfora decorativa, explicação técnica sem pedido de comparação,
  substituir uma definição técnica ou forçar equivalência literal que distorça
  o mecanismo.
---

# analogy-generator

## Entradas

- Identifique conceito ou trecho, relação central, público, conhecimentos familiares e extensão desejada. Aproveite a analogia sugerida pelo usuário, se houver, sem presumir que seja válida.
- Use o contexto fornecido; se o público não estiver definido, adote linguagem introdutória e uma situação cotidiana simples, declarando a suposição quando relevante. Pergunte apenas se a informação ausente mudar materialmente o mecanismo explicado ou a escolha do domínio familiar.

## Procedimento

1. **Fixe a relação correta.** Enuncie brevemente o significado técnico e a relação que precisa ficar intuitiva: dependência, transformação, acesso, proporção ou outra estrutura pertinente. Corrija uma premissa falsa antes de compará-la. Preserve hipóteses, direção das relações e distinções necessárias.
2. **Escolha uma comparação útil.** Prefira um único domínio familiar que preserve essa relação, sem depender de semelhança superficial. Considere no máximo duas candidatas; descarte as que exigirem mais explicações que o próprio conceito ou induzirem erro central. Não apresente a busca interna por candidatas.
3. **Explique e mapeie.** Conte a analogia de forma curta e explicite quais elementos e quais relações correspondem ao conceito. Separe entidade, localização, conteúdo e operação quando forem distintos; em ponteiros, por exemplo, diferencie endereço, objeto e acesso indireto. Não suponha equivalência entre todas as propriedades dos dois domínios.
4. **Delimite a validade.** Confira ao menos uma inferência plausível que a comparação poderia induzir e que não vale no conceito. Declare o limite relevante com um contraste concreto. Se pedirem que toda relação da analogia valha literalmente, recuse essa extensão e indique o que o mapeamento permite concluir. Não use analogia como prova, evidência empírica ou justificativa causal.
5. **Volte ao conceito.** Retome a definição técnica e percorra um exemplo real do domínio explicado, com valores, operações ou consequências conferíveis. Relacione o exemplo ao mapa. Distinga exemplo hipotético de fato observado; não invente fontes, medições ou execução.
6. **Adapte ao código, se pertinente.** Use a linguagem e a semântica do trecho disponível; se precisar escolher uma linguagem, explicite a escolha. Preserve tipos, referências, mutação, validade e tempo de vida quando afetarem a relação. Mostre um trecho mínimo apenas se útil; identifique-o como ilustrativo quando não executado. Não altere arquivos ou execute o projeto apenas para produzir a analogia.

Se nenhuma comparação simples preservar a relação central, diga isso brevemente, dispense a analogia e explique por um exemplo concreto ou contraexemplo do próprio domínio. Faça o mesmo quando a abrangência ou a exatidão exigida no pedido não puder ser preservada: não substitua essa exigência por uma analogia parcial, salvo se esse recorte já estiver autorizado. Não prolongue a procura nem fabrique um mapa de equivalências.

## Entrega

Entregue uma analogia curta, um mapa explícito de correspondências, o limite de validade e a conexão com a definição técnica e o exemplo real. Prefira uma tabela pequena — elemento ou relação da analogia, correspondente técnico e vínculo preservado — quando facilitar a leitura; em respostas breves, use frases de correspondência. Não omita o limite para encurtar.

No caminho sem analogia, entregue a razão da inadequação e o exemplo concreto conectado à definição; marque o mapa como não aplicável, sem inventar correspondências. Respeite a extensão pedida, sem acrescentar aula, exercícios ou comparações adicionais por padrão.

## Verificação

- Confira se o mapa preserva a relação central e se cada inferência apresentada decorre do conceito, sem transferir propriedades não mapeadas.
- Verifique se o limite impede o equívoco mais relevante e se definição e exemplo continuam corretos sem a metáfora. Confira valores e operações usados; não alegue testes ou pesquisa que não realizou.
- Trabalhe com trechos, correspondências e justificativas observáveis; não solicite deliberação interna privada. Use somente conteúdo acessível e ferramentas disponíveis, quando necessárias. Não presuma acesso a chats, memória, arquivos ou pesquisa, nem chame outras meta-skills automaticamente.

## Condição de parada

Encerre quando a relação estiver explicada com correspondências válidas, limite claro e retorno técnico exemplificado, ou quando o exemplo concreto substituir justificadamente uma comparação inadequada. Se faltar um dado indispensável, indique a lacuna e peça apenas esse dado. Não transforme a função em rotina para outras respostas nem avance para tarefas externas.
