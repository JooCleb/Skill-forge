---
name: completeness-checker
description: >-
  Compare uma entrega com os requisitos vigentes no ChatGPT Work ou com artefatos
  de código no Codex. Use mediante pedido explícito de conferir se faltou algo
  solicitado, ou etapa nomeada dessa conferência em workflow já autorizado.
  Confira conteúdo mínimo, anexos e formatos com evidências rastreáveis. Não use
  para responder perguntas simples, revisar estilo, provar corretude integral,
  auditar segurança ou cobrar requisitos já substituídos; não imponha checklist
  de completude à execução comum de tarefas.
---

# completeness-checker

## Entradas e escopo

- Identificar o pedido, suas alterações autorizadas e a versão da entrega a conferir. Consultar somente contexto, arquivos e mecanismos disponíveis e autorizados; não presumir acesso a outros chats, memória ou anexos.
- Pedir apenas o material cuja ausência impeça uma conclusão relevante. Se persistir uma lacuna, delimitar a conferência; não inventar a lista integral de requisitos nem declarar completude global.
- Conferir cobertura sem ampliar o pedido. Não corrigir a entrega, pesquisar fatos, executar código ou chamar outras meta-skills automaticamente. Usar artefatos, evidências e justificativas observáveis, sem solicitar deliberação interna privada.

## Procedimento

1. Consolidar os requisitos vigentes a partir das fontes disponíveis, identificando origem e ordem das alterações. Aplicar substituições expressamente autorizadas; preservar exigências anteriores que continuem válidas. Registrar conflitos não resolvidos sem escolher silenciosamente uma versão.
2. Decompor pedidos compostos em itens verificáveis com identificadores estáveis. Incluir restrições, quantidades, anexos, formatos, instruções de uso e critérios de aceite efetivamente solicitados. Separar sugestões de obrigações; não acrescentar boas práticas como exigências.
3. Mapear cada item ao trecho, página, caminho, arquivo ou outra evidência da versão inspecionada. Abrir anexos acessíveis e conferir formato real, legibilidade e conteúdo mínimo exigido; nome de arquivo, link, promessa ou título de seção não bastam. No Codex, localizar arquivos e símbolos pertinentes; informar separadamente se execução ou testes solicitados têm evidência observada, sem alegar que foram executados nesta análise.
4. Classificar pela evidência e justificar:
   - **Atendido:** os elementos requeridos estão presentes com substância verificável para o critério de cobertura.
   - **Parcial:** parte do requisito está presente, mas faltam componentes, profundidade mínima solicitada ou evidência de parte da entrega.
   - **Ausente:** falta o item ou seu conteúdo requerido; uma seção somente com título ou marcador vazio é ausente quanto ao conteúdo. Separar estrutura e conteúdo se forem requisitos distintos.
   - **Não aplicável:** uma condição expressa do pedido não se verifica, com justificativa. Retirar requisitos substituídos da cobrança e registrar sua substituição, sem contá-los como lacunas.
5. Registrar o limite da observação separadamente do status. Se um artefato alegado não puder ser aberto, marcar **pendente de verificação**, sem concluir atendimento ou ausência. Se necessário, deixar o status indeterminado até obter evidência; não usar “não aplicável” para encobrir falta de acesso. Mera ausência na amostra inspecionada não prova ausência no restante inacessível.

## Entrega

Apresentar uma conclusão curta sobre a cobertura observada e um checklist rastreável, preferencialmente em tabela:

`ID | Requisito vigente e origem | Evidência/localização | Status | Lacuna ou limite`

Dimensionar o checklist ao pedido. Destacar lacunas e pendências materiais, com a ação mínima necessária para resolvê-las. Informar o que foi inspecionado, o que ficou inacessível e quais substituições alteraram o escopo. Não apresentar atendimento de cobertura como certificado de exatidão, segurança ou funcionamento.

## Verificação e parada

- Conferir se cada requisito vigente tem linha ou agrupamento explícito, se cada “atendido” tem evidência substantiva e se anexos e formatos exigidos foram incluídos. Revisar seções vazias, condições de aplicabilidade e alegações sem acesso.
- Relatar somente leituras, verificações e testes efetivamente observados; distinguir inspeção documental de execução. Não exigir testes que não façam parte dos requisitos.
- Encerrar quando todos os itens vigentes estiverem mapeados e as lacunas ou limitações registradas. Se faltarem fontes essenciais, entregar a cobertura possível e a pendência específica, sem prolongar buscas de baixo ganho, acionar outras meta-skills ou executar correções fora do escopo.
