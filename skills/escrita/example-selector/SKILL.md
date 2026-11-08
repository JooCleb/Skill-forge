---
name: example-selector
description: >-
  Selecione ou melhore exemplos de uma explicação mediante pedido explícito dessa
  análise ou etapa nomeada de workflow já autorizada, em materiais de estudo no
  ChatGPT Work ou explicações de código no Codex. Escolha casos que revelem o
  mecanismo, evitem um erro de compreensão e esclareçam limites conforme os
  pré-requisitos do público. Não use para acrescentar variações redundantes a um
  exemplo suficiente, criar listas de exercícios, produzir uma aula inteira ou
  inventar analogias sem correspondência verificável; um pedido genérico de
  explicação não autoriza esta análise separada.
---

# example-selector

## Entradas e escopo

- Identificar conceito, definição ou regra válida, objetivo didático, erro a evitar, exemplos existentes e pré-requisitos pelo material acessível. Registrar hipóteses de nível apenas quando relevantes; perguntar somente por informação que mude materialmente a seleção.
- Confirmar o pedido explícito de selecionar, avaliar ou melhorar exemplos, ou a etapa nomeada no workflow autorizado. Fora disso, atender ao pedido original sem impor esta análise. Não chamar outras meta-skills automaticamente nem ampliar a tarefa para currículo, bateria de exercícios ou revisão integral.
- Trabalhar com trechos, entradas, saídas e justificativas observáveis. Não solicitar deliberação interna privada nem presumir acesso a outros chats, memória, arquivos ou ferramentas.

## Procedimento

1. **Fixar o alvo.** Expressar brevemente a relação que o exemplo precisa tornar visível e a confusão a evitar. Conferir a definição de referência antes de escolher casos; não selecionar apenas resultados que confirmem uma afirmação falsa ou incompleta.
2. **Reaproveitar o suficiente.** Avaliar o exemplo existente. Mantê-lo se já cumpre o objetivo, sem inventar defeitos ou novas variações. Se precisar de ajuste, localizar o problema e alterar somente o necessário.
3. **Escolher o conjunto mínimo.** Começar por um caso pequeno e concreto. Acrescentar um contraste quando ele distinguir interpretações ou revelar uma condição relevante, mudando preferencialmente uma variável por vez. Incluir caso-limite ou contraexemplo somente quando prevenir uma generalização indevida. Essas funções podem compartilhar um caso; não impor três exemplos por rotina.
4. **Controlar pré-requisitos.** Usar dados, notação e operações já conhecidos. Retirar contexto, números e detalhes que não contribuam para o mecanismo. Se um caso curto depender de conceito avançado ainda não ensinado, preferir outro acessível; introduzir o pré-requisito mínimo apenas se indispensável ao objetivo, sem abrir uma nova aula.
5. **Conferir os casos.** Verificar entradas, resultados, condições de validade e o contraste pretendido por cálculo, inspeção, fonte acessível ou execução disponível, conforme o domínio. Separar um limite real de uma entrada simplesmente inválida. Em analogias fornecidas, exigir correspondências explícitas com o conceito e indicar onde falham; substituí-las por exemplos diretos se distorcerem o mecanismo.
6. **Ordenar e conectar.** Apresentar primeiro o caso mínimo, depois o contraste e o limite pertinentes. Explicar o que cada caso evidencia e reconectar à definição correta. Distinguir ilustração de prova: poucos exemplos não demonstram uma afirmação geral.

## Adaptação ao Codex

Usar linguagem, versão, tipos e arquivos acessíveis apenas quando afetarem o conceito. Preferir trechos mínimos completos e dados sintéticos, sem dependências desnecessárias. Separar a regra matemática da semântica da linguagem e de comportamento indefinido ou dependente de implementação. Executar somente quando útil, permitido e disponível; não alterar o projeto nem executar ações externas para obter um exemplo. Informar se a saída foi executada ou conferida por inspeção/simulação; não inventar resultados de testes.

## Entrega

Entregar exemplos ordenados em lista curta ou tabela, com **função didática**, **situação/entrada**, **resultado**, **o que revela** e **limite relevante**, sem forçar campos repetidos quando a prosa for mais clara. Mostrar o contraste ou a correção da confusão em uma frase. Ao revisar, informar o que foi mantido, substituído ou simplificado e por quê. Se o exemplo existente bastar, confirmar isso brevemente e encerrar sem acrescentar variações.

## Verificação e parada

Conferir correção dos resultados, alinhamento com a definição, contribuição distinta de cada caso, pré-requisitos e ausência de complexidade acidental. Declarar incertezas ou verificações não executadas que afetem a confiança; omitir ou qualificar um caso sem suporte. Encerrar quando os exemplos suficientes e conferidos revelarem o mecanismo e os limites pertinentes. Não iniciar exercícios ou outra aula. Se faltar dado indispensável, indicar a lacuna e solicitar somente esse dado, sem alegar conclusão.
