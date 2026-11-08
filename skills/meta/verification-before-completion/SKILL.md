---
name: verification-before-completion
description: >-
  Condicione declarações de sucesso à evidência atual no ChatGPT Work ou no Codex
  quando houver código. Use mediante pedido explícito de verificar uma declaração
  de sucesso ou etapa nomeada de verificação antes da conclusão em workflow já
  autorizado, como confirmar uma correção ou um salvamento. Não use em conversas
  casuais, para repetir testes suficientes e ainda válidos, nem para auditoria
  integral de fatos, requisitos ou segurança sem pedido específico.
---

# verification-before-completion

Vincule a conclusão ao que foi observado, no escopo autorizado.

## Entradas

- Pedido explícito ou etapa nomeada autorizada; afirmação de sucesso pretendida e critérios vigentes.
- Artefato ou ação real, versão e destino; evidências disponíveis, como resultados de testes, retornos de ferramentas e registros de gravação.
- Capacidades, acessos e permissões efetivamente disponíveis.

Recupere essas informações do contexto e dos artefatos pertinentes. Peça apenas o dado ausente que mude materialmente o veredito ou a próxima verificação.

## Procedimento

1. Confirme o pedido explícito desta análise ou a etapa nomeada já autorizada. Fora desse escopo, atenda à solicitação sem abrir uma auditoria de conclusão. Não acione outras meta-skills automaticamente nem exija deliberação interna privada; use artefatos, resultados e justificativas observáveis.
2. Identifique exatamente o que se pretende afirmar. Separe estados como criado, salvo, testado e publicado; estabeleça a evidência mínima adequada a cada estado. Não amplie uma confirmação pontual para uma auditoria integral.
3. Inspecione o resultado real e os retornos relevantes, incluindo erros, resultado final e código de saída quando houver. Relacione a evidência à versão do artefato, configuração, ambiente e destino. Um relato de sucesso de terceiro exige confirmação suficiente para sustentar a declaração.
4. Reaproveite evidência suficiente e ainda válida. Confira mudanças posteriores no artefato, dependências, configuração e estado externo pertinente. Revalide somente o que essas mudanças possam afetar ou o que ainda não foi comprovado. A passagem do tempo, isoladamente, não exige repetir testes de um artefato imutável; estados externos podem exigir nova consulta.
5. Execute as verificações relevantes faltantes com recursos autorizados. Para afirmar “corrigido”, obtenha resultado observado do caso que falhava na versão atual; reutilize uma execução existente se ela ainda satisfizer essas condições. Inspeção de código, alteração de arquivo ou lint isolado não comprovam a correção funcional. Registre entrada, resultado esperado, observado e comando ou método pertinente.
6. Para ações mediadas por ferramenta, leia a confirmação da operação no destino correto. Chamada enviada, tarefa em fila, ausência de resposta, timeout ou retorno de erro não comprovam conclusão. Consulte o estado se houver capacidade e autorização; não repita uma mutação sem verificar seus possíveis efeitos.
7. Se houver falha comprovada, corrija dentro do escopo autorizado e revalide a parte afetada. Se faltar acesso, artefato ou capacidade, registre “não verificado” ou “pendente”, com a lacuna concreta. Não converta impossibilidade de verificar em aprovação ou em falha comprovada do artefato.

## Entrega

Apresente uma conclusão breve, o alcance comprovado, a evidência rastreável e as limitações. Use uma tabela por afirmação apenas quando facilitar a comparação. Distinga os estados:

| Estado | Evidência adequada |
| --- | --- |
| Criado | Artefato real identificado e inspecionado no contexto informado. |
| Salvo | Gravação confirmada no destino solicitado; releitura quando necessária. Existência local não comprova salvamento em outro serviço. |
| Testado | Verificação executada, com seu resultado descrito. “Testado” não significa “aprovado”. |
| Publicado | Publicação confirmada no destino pertinente. Build, envio ou fila não bastam. |

Declare “aprovado” somente no alcance das verificações que passaram; detalhe falhas, pendências e partes não verificadas. Identifique inspeção, simulação e execução real pelo que efetivamente ocorreu. Preserve referências, caminhos, versões e trechos mínimos dos resultados, sem expor segredos.

Exemplo de conclusão: “Corrigido para a entrada X na versão Y: o comando Z retornou o resultado esperado W, com saída 0. A publicação ainda não foi verificada.” Use apenas dados realmente observados.

## Verificação

Antes de entregar o veredito, confira se cada declaração aponta para evidência suficiente da versão e do destino pertinentes e se alguma mudança posterior a invalidou. Mantenha separados o artefato correto, a ação confirmada e a etapa ainda pendente. Não alegue acesso, pesquisa, testes ou persistência que não ocorreram.

## Condição de parada

Encerre quando as afirmações pretendidas estiverem sustentadas ou delimitadas por falhas e pendências concretas. Reutilize verificações suficientes ainda válidas e não acrescente testes por ritual. Se resolver uma pendência exigir ampliar o escopo ou obter autorização inexistente, relate o bloqueio e a próxima ação necessária, sem declarar sucesso nessa parte.
