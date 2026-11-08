---
name: consistency-checker
description: >-
  Use mediante pedido explícito de revisar a consistência interna de documento,
  resposta extensa ou conjunto de arquivos no ChatGPT Work ou no Codex, ou etapa
  nomeada dessa análise em workflow já autorizado. Abrange divergências de nomes,
  definições, datas, unidades, números e regras entre texto, tabelas, gráficos,
  anexos, código e documentação. Não use para checagem externa de fatos,
  padronização meramente estética, conferência de completude ou revisão geral
  de código; não impor esta análise à execução comum de tarefas.
---

# consistency-checker

## Entradas e escopo

- Identificar a entrega, sua versão e as partes autorizadas para comparação, incluindo anexos e fontes internas designadas como referência. Usar somente contexto, arquivos e ferramentas realmente disponíveis; não presumir acesso a outros chats, memória ou artefatos.
- Pedir apenas informação que mude uma conclusão material. Se faltar fonte essencial, delimitar a análise possível e registrar a pendência.
- Trabalhar com evidências e justificativas observáveis, sem solicitar deliberação interna privada. Não pesquisar fatos externos, executar projetos, editar a entrega ou chamar outras meta-skills automaticamente. Se houver autorização de correção no pedido, aplicar somente os ajustes sustentados pelas evidências.

## Procedimento

1. Extrair nomes, definições, datas, números, unidades e regras repetidas, com suas localizações. Registrar referente, população, período, versão, condições e denominador relevantes a cada ocorrência.
2. Comparar ocorrências entre texto, tabelas, gráficos e anexos efetivamente acessíveis. Examinar títulos, eixos, legendas e notas antes de interpretar valores; não inferir conteúdo visual ilegível. No Codex, comparar os contratos, símbolos, constantes, configurações e documentação pertinentes, citando caminho e linha ou símbolo.
3. Verificar se as ocorrências expressam a mesma coisa sob as mesmas condições. Converter unidades compatíveis e considerar arredondamentos documentados. Distinguir mudanças legítimas de população, período, versão ou escopo. Não presumir contradição por sinônimos válidos nem equivalência por nomes iguais.
4. Separar **divergência confirmada**, **ambiguidade/pendência** e **diferença legítima**. Uma população recrutada de 15 e uma analisada de 12 podem coexistir; esclarecer rótulos ambíguos em vez de igualar números. Distinguir contradição do próprio artefato de erro ou limitação de extração.
5. Sugerir a correção mínima com base na instrução vigente e na fonte designada ou comprovadamente autoritativa para aquele escopo. Explicar essa prioridade com evidência observável; não escolher por maioria, posição no documento, data isolada ou preferência automática pelo código. Sem autoridade ou definição suficiente, registrar as alternativas e a confirmação necessária, sem inventar um valor correto.

## Entrega

Apresentar conclusão curta limitada ao material inspecionado e os achados, preferencialmente em tabela:

`ID | Divergência ou ambiguidade | Localizações e evidências comparadas | Impacto | Correção sugerida e fonte, ou pendência`

Justificar o impacto sobre interpretação ou uso, sem exagerar gravidade. Mencionar diferenças legítimas quando evitarem falso positivo; não listar toda repetição coerente. Se não houver achados, declarar apenas que não foram encontradas inconsistências no escopo observado. Informar materiais inacessíveis e separar sugestões de alterações efetivamente realizadas.

## Verificação e parada

- Conferir se cada achado cita as ocorrências comparadas, considera escopo/tempo/unidades e sustenta a correção em uma fonte identificada. Rejeitar falsos positivos de sinonímia, arredondamento ou populações distintas.
- Após correção autorizada, reler as ocorrências afetadas e verificar se o ajuste criou nova divergência. Relatar somente inspeções, execuções e resultados realmente observados; coerência interna não comprova veracidade externa nem corretude integral.
- Encerrar ao comparar as partes acessíveis do escopo e registrar divergências, correções ou pendências. Se faltar evidência decisiva, entregar o resultado delimitado e o dado necessário, sem ampliar a tarefa ou forçar uma conclusão.
