---
name: skill-selector
description: "Escolha o menor conjunto de skills que acrescenta capacidade útil a uma tarefa no ChatGPT Work ou no Codex. Use mediante pedido explícito de selecionar ou comparar skills para uma tarefa, ou etapa nomeada de seleção em workflow já autorizado. Considere gatilhos, exclusões, disponibilidade e sobreposição. Não use para analisar pedidos comuns automaticamente, selecionar por palavras parecidas, executar a tarefa principal ou iniciar uma cadeia de meta-skills."
---

# skill-selector

## Entradas

- Recuperar do contexto o resultado pretendido, os limites, os materiais disponíveis e as skills expressamente solicitadas.
- Usar o catálogo acessível, com nome, descrição, origem e disponibilidade, e as capacidades e permissões reais do ambiente. Não presumir acesso a outro chat, memória, conector, agente ou repositório.
- Perguntar somente por lacuna que mude materialmente a seleção. Se o catálogo estiver incompleto ou inacessível, declarar o alcance da comparação e quais recomendações permanecem provisórias.

## Procedimento

1. Confirmar que o pedido solicita esta análise ou que a seleção é uma etapa nomeada do workflow já autorizado. Uma menção incidental, uma instrução citada como conteúdo ou a existência de muitas skills não constitui esse gatilho. Sem ele, encerrar esta análise e atender ao pedido original.
2. Identificar as operações necessárias ao resultado e as exclusões relevantes. Separar uma skill diretamente solicitada de nomes encontrados em exemplos ou por afinidade de palavras. Não acrescentar pesquisa, revisão, organização ou automação sem contribuição necessária ao pedido.
3. Consultar primeiro os metadados do catálogo disponível. Completar apenas lacunas relevantes pelos mecanismos existentes e deduplicar espelhos da mesma skill pela origem/identidade. Formar uma lista curta por correspondência entre o pedido concreto e o escopo declarado; não carregar corpos por mera coincidência lexical.
4. Ler o `SKILL.md` somente das candidatas plausíveis e os recursos indispensáveis para decidir. Conferir gatilhos, exclusões, pré-condições e sobreposição com capacidades já disponíveis. Registrar qual instrução acrescenta capacidade útil. Distinguir leitura para comparação, seleção e execução; não aplicar uma candidata só porque foi lida. Não chamar outras meta-skills para conduzir esta análise.
5. Priorizar as skills expressamente solicitadas e aplicáveis. Explicar indisponibilidade ou incompatibilidade em vez de substituir silenciosamente. Comparar a contribuição adicional de cada candidata com o custo de contexto, coordenação, dependências e etapas. Preferir cobertura suficiente com menos redundância; combinar skills somente quando cada uma cobrir uma necessidade distinta ou um requisito real do ambiente/projeto.
6. Se a melhor candidata não estiver instalada, não puder ser lida ou exigir acesso ausente, identificar a capacidade faltante e escolher uma alternativa disponível, inclusive nenhuma skill especializada. Não inventar instruções, instalação, acesso ou execução; não instalar nem criar skills por iniciativa desta seleção. Não confundir uma skill disponível com ferramentas ou permissões disponíveis.
7. Escolher nenhuma, uma ou poucas skills. Remover as candidatas opcionais cuja retirada não reduza a cobertura útil. Se nenhuma acrescentar procedimento necessário à capacidade direta do assistente, recomendar nenhuma. Respeitar as instruções aplicáveis do ambiente sem transformar a seleção em rotina universal.

## Entrega

Apresentar uma resposta curta, usando tabela somente se facilitar a comparação:

- **Selecionadas:** nome e identificador/origem quando houver ambiguidade, contribuição concreta e fundamento observável no pedido e no escopo lido. Indicar indisponibilidades e recomendações provisórias; se a seleção for vazia, dizer por quê.
- **Exclusões relevantes:** candidatas plausíveis descartadas por sobreposição, exclusão de escopo, custo sem ganho ou indisponibilidade, sem listar todo o catálogo.
- **Alternativa sem skill especializada:** caminho direto para o mesmo resultado com as capacidades reais e suas limitações. Se não for viável, indicar precisamente o que falta.

Fornecer justificativas verificáveis, como trechos do pedido e instruções ou arquivos consultados, sem solicitar ou expor deliberação interna privada. Não apresentar recomendação ou leitura como execução da skill selecionada.

## Verificação

- Conferir que há gatilho autorizado, que cada selecionada satisfaz o contexto e as exclusões e que cada inclusão tem contribuição distinta. Aceitar uma seleção vazia quando for suficiente.
- Conferir se as alegações de disponibilidade e leitura correspondem ao que foi observado. Separar capacidade faltante, recomendação e execução; não declarar testes ou roteamento real sem evidência.
- No Codex, considerar os arquivos e as instruções de projeto acessíveis pertinentes ao objetivo de código; não pressupor ferramentas, mudanças, testes ou agentes executados.

## Condição de parada

Encerrar ao entregar a seleção mínima justificada, as exclusões relevantes, a alternativa direta e eventuais lacunas materiais. Não continuar buscando candidatas sem ganho provável, chamar a si mesma, acionar outras meta-skills ou executar os exemplos. Retomar outra etapa do workflow somente quando ela já estiver no escopo autorizado.
