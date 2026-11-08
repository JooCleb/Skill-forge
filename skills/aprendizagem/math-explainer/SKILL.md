---
name: math-explainer
description: >-
  Ensine por que uma fórmula funciona, derive resultados e conecte representações
  matemáticas em pedidos de estudo ou de compreensão de código no ChatGPT Work
  e no Codex. Use quando o usuário pedir uma demonstração, a origem de uma
  fórmula ou a relação entre suas formas algébrica, geométrica e física,
  explicitando domínio, hipóteses, unidades e regras de cada passagem.
  Não use para cálculo numérico simples, revisão textual, exposição geral sem
  derivação ou conexão matemática como foco, nem quando o usuário pedir
  explicitamente tutoria em modo socrático.
---

# math-explainer

## Entradas

- Identifique a fórmula ou o resultado, o objetivo, o nível, a notação conhecida e a extensão desejada pelo contexto. Aproveite o conhecimento já demonstrado; introduza apenas os pré-requisitos necessários.
- Pergunte somente se faltar uma informação que mude materialmente a explicação, como uma expressão ambígua ou o conjunto numérico pretendido. Nos demais casos, avance com uma hipótese simples e explícita, como trabalhar nos reais, sem presumir familiaridade avançada.
- Confira se a afirmação é verdadeira antes de tentar demonstrá-la. Se for falsa ou incompleta, mostre o problema por um contraexemplo ou caso excluído e formule a versão válida.

## Procedimento

1. **Comece pelo significado.** Use uma situação ou exemplo pequeno para mostrar o que se quer calcular ou provar. Defina os conceitos necessários antes de empregá-los na derivação; o exemplo pode ser retomado na resolução final.
2. **Fixe as condições.** Defina símbolos, índices, conjuntos, domínio e hipóteses. Declare unidades quando houver grandezas, identifique parâmetros adimensionais e confira a coerência dimensional. Diferencie grandezas e suas variações quando isso alterar o sentido das operações. Atualize essas condições ao introduzir variáveis ou modelos auxiliares, incluindo denominadores não nulos e argumentos positivos de logaritmos. Em matemática abstrata, não invente unidades ou fenômenos físicos.
3. **Derive com justificativas.** Parta de definições ou resultados prévios declarados, sem usar a conclusão como premissa. Mostre cada passagem e a regra que a permite, agrupando apenas passos elementares compatíveis com o nível. Distinga igualdade, equivalência, implicação e aproximação. Ao dividir, aplicar logaritmos, extrair raízes, elevar potências ou trocar limites e operações, explicite as condições relevantes e verifique perda ou introdução de soluções. Se usar um teorema prévio, explique seu papel; desenvolva-o somente se necessário ao objetivo.
4. **Conecte representações válidas.** Explique a leitura algébrica e acrescente a geométrica ou física quando ajudarem e houver correspondência legítima. Identifique o que cada elemento representa e preserve domínio, sinais e hipóteses. Se uma representação não se aplicar ou depender de um modelo adicional, diga isso brevemente; não fabrique uma analogia física. Diferencie uma interpretação intrínseca de uma aplicação possível: se introduzir um modelo útil, declare suas novas hipóteses e restrinja a interpretação a ele. Diferencie intuição visual de demonstração.
5. **Resolva e explore.** Desenvolva um exemplo com substituição, cálculo e interpretação. Examine casos especiais, fronteiras do domínio, parâmetros nulos, sinais ou paridade conforme forem relevantes. Indique onde a fórmula deixa de valer e por quê, sem impor uma lista de casos desconectados do problema.
6. **Adapte ao código quando solicitado.** Relacione variáveis e operações à expressão matemática. Considere tipos, índices, inicialização, entradas inválidas, arredondamento e limites numéricos pertinentes. Separe a identidade matemática do comportamento da implementação. Use o código fornecido ou os arquivos acessíveis no escopo autorizado; não suponha acesso a repositórios. Produza ou execute um trecho mínimo apenas quando ajudar a explicar ou conferir o resultado, respeitando o pedido e as permissões disponíveis.

## Entrega

Construa uma explicação progressiva com conceitos e condições, derivação verificável, interpretações pertinentes, exemplo resolvido, limites de aplicação e uma pergunta curta de compreensão. Use notação legível e explique o vínculo entre texto e equações. A pergunta final deve verificar uma ideia central sem transformar a exposição em uma sessão socrática.

Ajuste o tamanho ao pedido: comprima exemplos e passos familiares em respostas curtas, preservando condições que mudem a validade. Respeite restrições explícitas de formato ou ausência de exercícios. Não force títulos, gráficos ou código quando não acrescentarem compreensão.

## Verificação

- Releia as passagens, o domínio de cada expressão, as hipóteses, os sinais, os índices e as unidades. Verifique se uma generalização do resultado exige uma fórmula diferente.
- Faça ao menos uma conferência adequada: substituição de valores admissíveis, cálculo por outra via ou representação gráfica pertinente. Inclua um caso especial relevante quando ele puder revelar um erro. Uma amostra ou gráfico confere plausibilidade, mas não prova uma identidade geral.
- Use ferramentas somente se disponíveis e úteis. Em gráficos, respeite descontinuidades, escala e domínio; em cálculos aproximados, informe a precisão relevante. Registre apenas verificações realmente feitas e não apresente código sugerido como executado.
- Se uma dúvida factual ou teórica exigir consulta, use fontes confiáveis acessíveis e cite apenas as efetivamente lidas. Se não puder verificar, declare o ponto incerto em vez de inventar demonstração, referência ou resultado de ferramenta.

## Condição de parada

Encerre quando a pergunta matemática estiver respondida no nível e na extensão solicitados, com derivação justificada, exemplo conferido, restrições claras e a pergunta breve de compreensão. Não responda à própria pergunta nem inicie outra aula. Se faltar um dado indispensável ou restar uma lacuna que impeça concluir, identifique-a e solicite somente o necessário, sem alegar que o resultado foi demonstrado.
