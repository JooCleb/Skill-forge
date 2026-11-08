---
name: stop-condition-manager
description: >-
  Defina ou aplique critérios de encerramento e reabertura de pesquisa,
  investigação, testes exploratórios ou ciclos de revisão no ChatGPT Work e,
  quando envolver código, no Codex. Use mediante pedido explícito desta análise
  ou etapa nomeada de controle de parada em workflow já autorizado. Não use para
  interromper trabalho incompleto por conveniência, encerrar por contagem de
  fontes ou rodadas, impor limites arbitrários a tarefas críticas, fazer apenas
  uma conferência de completude ou transformar o controle em rotina universal.
---

# stop-condition-manager

## Entradas e escopo

- Identificar objetivo, decisão ou entrega, versão e recorte; requisitos mínimos vigentes, evidências disponíveis, lacunas e riscos residuais.
- Recuperar o orçamento real de tempo, custo, tentativas e acesso, quando informado, distinguindo limite firme de estimativa. Sem orçamento definido, registrar a ausência; não inventar um prazo nem usar recursos ilimitados como premissa. Perguntar somente pelo dado que altere materialmente os critérios ou o veredito.
- Distinguir **definir critérios** de **avaliar o estado atual**. No primeiro caso, entregar condições propostas e marcar o atendimento como ainda não avaliado. Usar apenas materiais, ferramentas e permissões disponíveis; não presumir acesso a outros chats, memória ou monitoramento em segundo plano.
- Restringir esta análise ao pedido explícito ou à etapa nomeada autorizada. Usar artefatos, evidências e justificativas observáveis, sem pedir deliberação interna privada. Não chamar outras meta-skills automaticamente nem iniciar pesquisa, testes, correções ou ações externas apenas para preencher lacunas; prosseguir com ações que já estejam autorizadas no workflow.

## Procedimento

1. **Fixar os mínimos antes do veredito.** Traduzir o objetivo em poucos critérios observáveis, com origem, evidência necessária e condição de atendimento. Separar lacunas críticas, que impedem a conclusão pretendida, de melhorias opcionais. Ajustar o rigor às consequências de erro; não acrescentar exigências enciclopédicas nem reduzir mínimos para acomodar um resultado ou orçamento. Registrar mudanças de escopo autorizadas sem apresentar cobertura reduzida como conclusão do escopo original.
2. **Definir cobertura, saturação e ganho marginal.** Cobrir os critérios decisivos, cenários relevantes e contradições que possam mudar a resposta. Exigir evidência adequada, não apenas presença de tópicos. Considerar saturação quando incrementos pertinentes, com diversidade e procura por contraevidência adequadas à questão, deixam de alterar a decisão ou revelar lacunas materiais. Sem histórico observável, marcar saturação como não demonstrada. Comparar o próximo incremento concreto ao seu custo e à chance qualitativamente justificada de mudar a decisão ou reduzir risco relevante; não inventar probabilidades, porcentagens de cobertura ou limiares universais. Contagem de fontes, testes ou rodadas não prova suficiência; falta de resultado pode decorrer de busca estreita ou falha da ferramenta.
3. **Confrontar critérios e evidências.** Mapear cada critério a fonte, trecho, artefato, versão, resultado ou registro disponível. Classificar como **atendido**, **não atendido**, **não comprovado** ou **não aplicável com motivo**. Distinguir relato fornecido de observação própria e falta de acesso de falha comprovada. Reutilizar evidências suficientes ainda válidas; reavaliar somente o que uma mudança relevante possa invalidar.
4. **Monitorar o que afeta a decisão.** Nos pontos de controle autorizados, atualizar mínimos, contradições materiais, riscos, orçamento restante e próximo incremento útil. Não compensar um requisito essencial pendente com abundância em outros aspectos. Resolver contradições materiais ou delimitar seu efeito com evidência; ignorá-las não demonstra saturação. Melhorias opcionais não impedem encerramento quando já não oferecem ganho proporcional. Risco residual só pode permanecer se não violar mínimos e for compatível com o objetivo e a tolerância autorizada; não presumir aceitação de risco crítico.
5. **Escolher o estado real.** Aplicar as regras abaixo. Se o orçamento terminar ou faltar acesso antes dos mínimos, preservar o estado parcial, as lacunas e a ação necessária para retomar; não fingir saturação, conclusão ou segurança. Não exceder um limite real por inércia nem impor um limite arbitrário para abandonar tarefa crítica.
6. **Registrar a reabertura.** Vincular cada gatilho ao critério ou conclusão afetada e à próxima verificação: nova evidência contraditória relevante, mudança de requisito, versão ou ambiente que invalide evidência, risco material identificado ou recurso recuperado para sanar lacuna crítica. Retomar apenas a parte afetada. Não reabrir por preferência cosmética ou passagem do tempo sem efeito pertinente; quando os dados envelhecem, definir validade com justificativa. Registrar gatilhos não cria automação nem promessa de acompanhamento futuro.

| Estado | Regra |
| --- | --- |
| **Conclusão suficiente no recorte** | Mínimos aplicáveis comprovados, contradições materiais tratadas e riscos residuais compatíveis; ganho de esforço adicional não justifica continuar. Fundamentar saturação quando alegada, sem exigi-la por ritual se as evidências decisivas já bastarem. Encerrar sem consumir orçamento restante por obrigação. |
| **Prosseguir** | Há lacuna crítica ou próximo incremento com ganho relevante, viável e autorizado. Indicar a próxima ação discriminante; não continuar indefinidamente apenas para acumular material. |
| **Interrompido por limite ou bloqueio** | Um limite real ou impedimento encerra a execução sem suficiência demonstrada. Informar motivo concreto e alcance parcial, sem converter pendência essencial em ressalva opcional. |

## Adaptação ao Codex

Relacionar critérios a requisitos, cenários de falha e riscos do código; usar arquivos, diff, versão, configuração, comando e resultado observados. Uma suíte aprovada ou percentual de cobertura não compensa cenário essencial não verificado. Distinguir inspeção, simulação, execução real e teste apenas proposto; não alegar aprovação sem resultado. Definir reabertura quando mudanças relevantes invalidarem os testes, sem exigir repetição integral após alteração sem relação com eles. Não modificar código nem executar testes fora do escopo autorizado.

## Entrega

Apresentar, proporcionalmente ao pedido:

- **Critérios e atendimento:** `Critério e origem | mínimo ou opcional | evidência necessária/observada e versão | estado | lacuna e impacto`.
- **Decisão e motivo real:** critérios apenas definidos, conclusão suficiente no recorte, prosseguir ou interrompido por limite/bloqueio; justificar cobertura, saturação demonstrada ou não, ganho marginal e orçamento conhecido.
- **Pendências e riscos residuais:** separar críticos de opcionais, com próximo passo viável e limitação de acesso ou verificação. Não inventar pendências quando os mínimos bastarem.
- **Gatilhos de reabertura:** condição observável, parte afetada e evidência ou ação necessária para retomar.

Exemplo de chamada: “Defina quando encerrar esta pesquisa comparativa e quando reabri-la, considerando os requisitos, evidências e orçamento fornecidos.”

## Verificação e condição de parada

Conferir que cada mínimo tenha evidência ou lacuna explícita, que contradições materiais e limites reais estejam visíveis e que o motivo de encerramento corresponda ao estado observado. Remover quotas arbitrárias, alegações de execução não observada e mudanças silenciosas de exigência.

Encerrar esta análise ao entregar os critérios solicitados ou o estado fundamentado, pendências e gatilhos de reabertura. A entrega desta análise pode estar completa enquanto a investigação permanece incompleta; deixar essa distinção explícita. Retomar o controle somente diante de evidência nova pertinente ou ponto de controle já autorizado, sem ciclos de autoavaliação.
