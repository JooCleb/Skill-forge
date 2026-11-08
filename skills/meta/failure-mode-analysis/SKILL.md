---
name: failure-mode-analysis
description: Analise preventivamente como um processo ou sistema definido pode falhar, com efeitos, detecção, contenção e recuperação, no ChatGPT Work ou no Codex quando envolver código. Use mediante pedido explícito de análise estruturada de falhas antes de operar ou modificar esse sistema, ou etapa nomeada dessa análise em workflow já autorizado, como importação de pedidos ou alteração de um fluxo operacional. Não use para depurar um defeito específico, corrigir erro de digitação, elaborar checklist abstrato sem sistema definido ou acrescentar análise preventiva a uma implementação sem solicitação.
---

# failure-mode-analysis

## Entradas e limites

- Delimite sistema, finalidade, mudança/operação planejada, etapas, interfaces, dependências e consequências relevantes. Identifique a unidade de exposição e o horizonte de análise, quando conhecidos.
- Use artefatos acessíveis e pertinentes: descrição do usuário, fluxos, procedimentos, especificações, registros, código ou testes existentes. Distinga fato observado, controle apenas documentado, hipótese e dado desconhecido; registre a origem por referência, trecho ou caminho.
- Pergunte apenas por lacuna que altere materialmente a análise. Se faltar o próprio sistema ou sua função, peça essa definição e suspenda a tabela; não gere checklist genérico. Sem frequência histórica, avance qualitativamente com incerteza explícita.
- Analise dentro do escopo solicitado. Não chame outras meta-skills automaticamente, não solicite deliberação interna privada e não presuma pesquisa, memória, ferramentas, agentes ou acesso a fontes. Apresente evidências e justificativas observáveis.

## Procedimento

1. **Mapeie funções.** Descreva entradas, saídas e resultado esperado de cada etapa/componente. Inclua transições, intervenção humana e dependências externas pertinentes ao sistema.
2. **Identifique falhas concretas.** Para cada função, examine omissão, resultado incorreto, duplicação, execução parcial, atraso, ordem inadequada e perda de integridade, quando aplicáveis. Separe modo de falha (como a função deixa de cumprir seu papel), causa, efeito local e propagação até o impacto final. Inclua falhas combinadas ou de causa comum quando puderem anular vários controles.
3. **Examine controles existentes.** Registre mecanismo, alcance, momento de atuação e evidência de funcionamento. Não trate controle proposto como instalado, ausência de registro como ausência comprovada de controle, nem alarme sem resposta definida como contenção.
4. **Avalie G, O e D separadamente.** Use a escala abaixo ou uma escala do usuário com âncoras explícitas. Justifique cada classificação por evidência ou cenário identificado; marque classificações provisórias. Compare itens na mesma unidade/horizonte e declare limitações de comparação.

   | Nível | Gravidade (G): efeito final plausível | Ocorrência (O): na exposição definida | Dificuldade de detecção (D): antes de propagar o efeito |
   | --- | --- | --- | --- |
   | 1 | Incômodo ou retrabalho pequeno, sem perda relevante | Excepcional, sustentada por histórico ou mecanismo demonstrado | Detecção e resposta tempestivas demonstradas, antes do efeito relevante |
   | 2 | Interrupção local ou perda reversível com esforço limitado | Ocasional em condições identificadas | Detecção provável por controle evidenciado, com tempo para conter |
   | 3 | Perda relevante, indisponibilidade prolongada ou inconsistência em etapas seguintes | Recorrente sob condições conhecidas | Cobertura parcial ou detecção tardia/manual, com propagação possível |
   | 4 | Dano irreversível, impacto amplo ou consequência crítica de segurança | Frequente ou esperada na operação considerada | Falha alcança o efeito final sem sinal útil a tempo, conforme evidência/cenário |
   | ND | Consequências insuficientemente definidas | Base insuficiente para estimar | Capacidade de detecção desconhecida |

   Trate os níveis como ordinais, sem probabilidades implícitas. Para O, registre contagens e denominador/período quando disponíveis; não invente taxas nem use ausência de incidentes como O=1 sem exposição conhecida. Sem base, use O=ND e cenários qualitativos de menor/maior ocorrência, identificando condições e dados que mudariam a prioridade. Para D, diferencie detectar uma anomalia de detectá-la a tempo de responder. Não multiplique G×O×D como verdade objetiva ou ranking suficiente; se o usuário exigir esse índice, identifique-o como heurística e preserve a análise separada das dimensões.

5. **Proponha respostas específicas.** Separe prevenção (reduzir causa/ocorrência), detecção (sinal, limiar ou condição e tempo útil), contenção (limitar propagação, gatilho e resposta) e recuperação (restaurar estado consistente, reconciliar perdas/duplicações e critério de retomada). Vincule cada ação ao modo e ao controle que falta. Informe responsável se conhecido, dependências e critério observável de conclusão; use “a definir” em vez de inventar nomes/prazos.
6. **Priorize e estime o residual.** Dê precedência a consequências críticas/irreversíveis e propagação sem contenção; considere recorrência sustentada por evidência e falhas de detecção. Explique conflitos entre dimensões. Trate desconhecimentos capazes de mudar a decisão como ações de obtenção de evidência, sem converter incerteza em risco baixo. Avalie o risco residual atual após os controles existentes evidenciados; apresente residual projetado separado e condicionado à implantação/verificação das ações. Não reduza G só por melhorar detecção, nem declare risco aceitável sem critério e autoridade de aceitação definidos.

### Quando envolver código no Codex

Inspecione os arquivos e instruções de projeto acessíveis no escopo autorizado e cite caminhos/símbolos pertinentes. Conecte modos de falha a interfaces, estados, persistência, concorrência e tratamento de erros que realmente existam. Use testes/logs disponíveis como evidência, distinguindo leitura de execução. Proponha verificações de idempotência, atomicidade, validação de entrada, interrupção e retomada apenas quando pertinentes. A análise não autoriza editar código, provocar falhas, executar testes destrutivos ou operar serviços; execute verificações somente se já autorizadas e com ambiente/efeitos conhecidos. Registre exatamente o que foi executado e observado.

## Entrega

Apresente brevemente escopo, mapa funcional, evidências/lacunas e legenda G/O/D. Quando houver O=ND, inclua, para os modos prioritários, cenários condicionais de ocorrência menos e mais propensa, as condições observáveis que os distinguem e a evidência que permitiria revisar O; não lhes atribua probabilidades inventadas. Entregue uma tabela rastreável; divida-a em tabelas ligadas por ID se a largura prejudicar a leitura:

| ID / etapa e função | Modo e causas | Efeito local → propagação/impacto final | Controles existentes e evidência | G/O/D e justificativas | Risco residual atual | Ações de prevenção, detecção, contenção e recuperação | Prioridade, responsável e verificação / residual projetado |
| --- | --- | --- | --- | --- | --- | --- | --- |

Ordene as ações por prioridade justificada. Explicite sinais e condições de pausa/retomada para falhas relevantes, pendências decisórias e limitações; não substitua lacunas por controles fictícios.

## Verificação

Confira se cada função relevante tem seus modos examinados; se causas, efeitos e propagação estão distintos; se classificações têm âncoras, origem e incerteza; se O=ND tem os cenários de ocorrência exigidos; e se cada falha relevante tem resposta observável. Confira que controles atuais e propostas, risco atual e projetado estão separados. Revise prioridades para que um índice baixo não oculte consequência crítica. Declare inspeções, simulações e testes conforme o que realmente ocorreu; não afirme cobertura exaustiva ou certificação.

## Condição de parada

Encerre ao entregar a tabela e ações priorizadas com lacunas e condições de revisão explícitas, ou ao identificar a definição mínima de sistema que impede prosseguir. Reabra a avaliação apenas se surgirem evidências, mudanças de escopo ou verificação de controles que alterem o residual. Não execute as ações propostas nem estenda a análise a outros sistemas sem autorização.
