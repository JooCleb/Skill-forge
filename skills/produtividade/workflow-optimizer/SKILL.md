---
name: workflow-optimizer
description: >-
  Melhore a eficiência de processos recorrentes existentes, como produção de
  relatórios, rotinas operacionais e pipelines de código, preservando qualidade e
  requisitos. Use mediante pedido explícito de otimização baseado em objetivos e
  evidências, ou etapa nomeada de otimização em workflow já autorizado. Não use
  para simples execução da tarefa, diagnóstico sem pedido de melhoria, revisão
  textual, criação de processo do zero, redesenho de fluxo ainda não entendido ou
  eliminação de verificações essenciais apenas para reduzir etapas.
---

# workflow-optimizer

## Entradas e escopo

- Identificar o fluxo autorizado, resultado desejado, frequência, início/fim,
  etapas, dependências e responsáveis relevantes. Usar artefatos e registros
  fornecidos ou acessíveis dentro da autorização existente.
- Fixar requisitos de qualidade, segurança, prazo e correção que a mudança deve
  preservar, além do objetivo de eficiência. Perguntar apenas pelo que altere
  materialmente a proposta; explicitar suposições nos demais pontos.
- Não ampliar o trabalho para outros processos nem chamar outras meta-skills
  automaticamente. Pedir evidências observáveis e justificativas verificáveis,
  sem solicitar deliberação interna privada.

## Procedimento

1. **Entender o estado atual.** Mapear sequência, entradas/saídas, decisões,
   esperas, retrabalho e verificações. Associar gargalos a registros, tempos,
   versões ou exemplos concretos; separar observação de causa presumida. Se o
   fluxo não estiver entendido, entregar lacunas e coleta mínima necessária antes
   de propor redesenho.
2. **Estabelecer baseline.** Quando houver dados, registrar período, volume,
   complexidade dos casos e fonte; medir tempo total e trabalho ativo, custo por
   unidade, erros materiais e retrabalho. Marcar métricas ausentes. Sem baseline,
   formular hipóteses e um plano de medição; não inventar números nem anunciar
   economia comprovada. Estimativas devem expor premissas e incerteza.
3. **Comparar alternativas.** Examinar simplificação, agrupamento, reutilização,
   automação e paralelismo seguro, incluindo manter o fluxo atual. Para cada
   mudança relevante, ligar evidência → alteração → efeito esperado; considerar
   esforço de implantação/manutenção, custo adicional, riscos e qualidade.
   - Reutilizar resultados apenas com parâmetros, versão/fonte, permissões e
     validade compatíveis; definir expiração ou invalidação. Evitar consultas
     repetidas sem introduzir dados obsoletos ou acesso indevido.
   - Agrupar passos sem esconder falhas ou remover rastreabilidade. Automatizar
     somente regras suficientemente definidas, com tratamento de exceções e
     recuperação proporcional ao impacto.
   - Paralelizar apenas etapas independentes, após conferir dependências,
     recursos, limites do serviço e disputa por estado compartilhado.
   - Preservar controles essenciais. Substituir uma verificação somente com
     evidência de cobertura equivalente e dentro da autorização. Menos etapas ou
     menor tempo com aumento de erros materiais não basta para chamar a mudança
     de melhoria; rejeitar opções que violem os requisitos estabelecidos.
4. **Desenhar um piloto reversível.** Escolher a menor mudança útil; definir
   amostra/período, responsáveis, métricas, limites de aceitação de qualidade e
   eficiência, critérios de interrupção e como restaurar a versão anterior.
   Comparar antes/depois com volume e complexidade equivalentes; contabilizar
   implantação, manutenção e retrabalho. Quando possível, variar uma mudança por
   vez e registrar fatores que possam explicar diferenças.
5. **Aplicar somente no escopo autorizado.** Um pedido de análise autoriza a
   proposta, não implica alterar sistemas externos ou implantar automações.
   Executar piloto ou mudanças apenas quando abrangidos pela autorização e pelas
   capacidades disponíveis; caso contrário, entregar o plano pronto. Não prometer
   agentes, monitoramento, acesso, persistência ou execução futura inexistentes.
   No Codex, usar branch/diff ou alteração de configuração reversível quando
   disponível, preservar verificações relevantes e medir condições comparáveis
   de cache/ambiente. Distinguir testes executados de verificações propostas.

## Entrega

Apresentar, proporcionalmente à complexidade:

- Fluxo atual resumido e fluxo revisado, com requisitos preservados.
- Mudanças justificadas por evidências, alternativas descartadas e riscos.
- Baseline disponível; efeitos esperados separados de resultados medidos.
- Plano de piloto e medição: métrica, fonte, período/amostra, critério de sucesso,
  limite de qualidade e reversão. Se faltarem dados, indicar a coleta necessária
  para decidir, sem impor uma quantidade arbitrária de execuções.
- Alterações efetivamente realizadas, verificações observadas e pendências.

## Verificação e parada

Conferir que cada recomendação respeite requisitos e dependências, que reuso não
comprometa validade, que o paralelismo seja seguro e que a comparação considere
custo e erros além de tempo. Não tratar simulação como evidência de ganho real.
Encerrar ao entregar proposta e piloto verificáveis ou concluir a execução já
autorizada e relatar seus resultados. Se faltar entendimento ou acesso essencial,
parar a parte dependente, registrar a lacuna e entregar o plano de coleta. Não
continuar otimizando, criar outras skills nem iniciar acompanhamento recorrente
sem novo escopo autorizado.
