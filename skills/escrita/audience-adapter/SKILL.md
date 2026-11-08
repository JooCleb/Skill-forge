---
name: audience-adapter
description: >-
  Adapte linguagem, profundidade, ordem e exemplos de textos, explicações ou
  documentação no ChatGPT Work e, quando envolver código, no Codex. Use mediante
  pedido explícito de adequar material a determinado público, nível ou contexto,
  ou em etapa nomeada de adaptação ao público de um workflow já autorizado.
  Preserve fatos, condições, limites e formalidade solicitada. Não use para mera
  correção textual, criação de exposição aprofundada sem pedido de adaptação,
  inferência de capacidade por identidade pessoal ou simplificação que altera fatos.
---

# audience-adapter

Adaptar a apresentação ao público informado, mantendo o núcleo conceitual e a finalidade do material. Tratar nível de conhecimento, contexto de uso e grau de formalidade como dimensões distintas.

## Entradas

- Identificar o material ou tema, o público pretendido, os conhecimentos prévios declarados, a finalidade e as restrições de formato, extensão e registro.
- Usar somente contexto fornecido ou efetivamente acessível e pertinente. Não pressupor acesso a histórico, arquivos, pesquisa ou memória.
- Perguntar apenas se uma informação ausente mudar materialmente a entrega. Se o nível for desconhecido e for possível prosseguir, declarar brevemente um ponto de partida provisório e ajustável; não apresentar essa escolha como diagnóstico da pessoa.
- Não deduzir capacidade, escolaridade ou familiaridade técnica a partir de idade, gênero, nacionalidade, deficiência, profissão ou outra identidade. Usar pré-requisitos e necessidades informados; um rótulo amplo de público não comprova domínio de cada conceito.

## Procedimento

1. **Fixar o conteúdo essencial.** Identificar afirmações, relações, definições, números, hipóteses, exceções e limites que precisam sobreviver à adaptação. Se houver fonte, comparar com ela; se houver apenas um tema, explicitar as condições relevantes sem inventar material de origem.
2. **Calibrar para a finalidade.** Selecionar o que explicar, em que ordem e com qual densidade com base nos pré-requisitos reais. Para iniciantes no tema, construir as conexões necessárias; para especialistas, preservar precisão e densidade útil, sem infantilizar. Não equiparar linguagem simples a tom informal nem formalidade a excesso de jargão.
3. **Reescrever proporcionalmente.** Ajustar termos, tamanho das frases, ordem, detalhamento e exemplos. Definir jargões indispensáveis no primeiro uso quando não forem pré-requisitos estabelecidos. Relacionar exemplos ao que o público já sabe, verificar resultados e declarar limites das analogias. Evitar complexidade acidental, estereótipos e exemplos decorativos.
4. **Preservar alcance e força.** Manter negações, quantificadores, causalidade, incerteza, unidades, condições e exceções que mudem o entendimento. Reduzir repetição e detalhes acessórios conforme a finalidade; não omitir ressalvas essenciais para caber em um limite. Se houver conflito de extensão, sinalizar a restrição e conservar o núcleo correto. Separar possível erro da fonte da adaptação, sem corrigi-lo silenciosamente.
5. **Oferecer camadas quando úteis.** Entregar primeiro o nível solicitado e acrescentar aprofundamento opcional apenas se ajudar. Não impor currículo, exercícios ou perguntas de diagnóstico. Explicar escolhas materiais com referências ao artefato, sem solicitar ou expor deliberação interna privada.

## Entrega

Entregar a versão adaptada pronta para uso, com conteúdo essencial preservado e grau de formalidade solicitado; na ausência deste, manter o registro do material. Acrescentar apenas a premissa de nível ou contexto adotada, quando necessária, e observações breves sobre lacunas ou perdas inevitáveis. Evitar relatório de revisão se não solicitado.

## Adaptação ao Codex

Adaptar explicações de código, comentários, documentação ou exemplos somente dentro do escopo pedido. Preservar semântica, contratos, identificadores, APIs, sintaxe e ressalvas de segurança; distinguir pseudocódigo de código executável. Não modificar implementação para adequar linguagem sem autorização correspondente. Usar arquivos, ferramentas e permissões disponíveis; distinguir execução observada de inspeção e não afirmar testes que não ocorreram.

## Verificação

- Comparar o original e a versão adaptada quanto ao núcleo essencial, força das afirmações, condições, números, referências e limites; manter citações literais identificadas, sem reescrever aspas como se fossem originais.
- Conferir se termos e exemplos dependem apenas dos pré-requisitos declarados ou dos introduzidos no texto, e se a profundidade e o registro atendem à finalidade.
- Verificar ausência de infantilização, inferências pessoais, promessas de compreensão e simplificações falsas. Fundamentar ajustes em trechos e resultados observáveis.

## Escopo e parada

Não transformar esta função em revisão universal nem chamar outras meta-skills automaticamente. Manter o recorte de adaptação: desenvolver uma exposição completa pertence ao escopo de escrita-aprofundada-didatica; corrigir redação preservando o público pertence a revisao-textual-fiel. Essas distinções não exigem carregar nenhuma delas.

Encerrar quando a versão atender ao público e à finalidade informados, preservando o essencial e registrando somente limitações materiais. Se faltar conteúdo indispensável, solicitar apenas esse conteúdo; não inventá-lo nem ampliar a tarefa para pesquisa, publicação ou edição externa.
