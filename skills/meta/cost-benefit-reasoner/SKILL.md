---
name: cost-benefit-reasoner
description: >-
  Use mediante pedido explícito de análise de custo-benefício para avaliar se uma
  mudança, automação ou investimento vale o esforço no ChatGPT Work ou Codex, ou
  em etapa nomeada dessa análise num workflow já autorizado. Não use para simples
  ordenação por preferência, análise financeira com números inventados, execução
  da opção escolhida ou edição de código sem pedido desta avaliação.
---

# cost-benefit-reasoner

Comparar benefícios adicionais com todos os custos relevantes da mudança em
relação à situação atual. Manter a recomendação condicionada às evidências.

## Entradas e escopo

Identificar situação atual, alternativas (incluindo manter ou adiar), objetivo,
horizonte, frequência/volume, requisitos, partes afetadas e evidências disponíveis.
Perguntar apenas sobre lacunas que possam mudar a decisão. Sem dados suficientes,
oferecer comparação qualitativa ou fórmulas com variáveis, sem preencher números.
Não transformar a análise em rotina universal nem chamar outras meta-skills
automaticamente. Pedir artefatos, registros e justificativas verificáveis, sem
solicitar deliberação interna privada.

## Procedimento

1. **Fixar a base.** Usar horizonte, unidades, volume e nível de serviço comparáveis.
   Explicitar o que acontece sem a mudança. Distinguir opções independentes de
   etapas que precisam ocorrer juntas; não agrupar abandonar e manter sem
   justificar. Eliminar ou condicionar opções que violem requisitos obrigatórios.
2. **Qualificar os dados.** Separar fatos e fontes, estimativas, hipóteses e lacunas.
   Ausência de custo não significa custo zero. Usar somente evidências acessíveis
   no escopo autorizado; conferir preços/condições mutáveis com recursos reais
   disponíveis ou registrar a impossibilidade e condicionar a conclusão.
3. **Inventariar custos futuros.** Para a base e cada alternativa, considerar
   implantação/construção, operação, manutenção, transição (treinamento, migração,
   interrupção e saída) e oportunidade da melhor alternativa viável preterida.
   Separar pagamentos, tempo e riscos; não somar unidades incompatíveis nem contar
   o mesmo recurso como tempo, salário e oportunidade. Registrar custos afundados
   irrecuperáveis à parte: eles não justificam continuar. Contabilizar despesas
   futuras de cancelamento, obrigações e valores recuperáveis quando pertinentes.
4. **Separar benefícios.** Registrar benefícios mensuráveis e qualitativos, sua
   evidência, quando começam e quem os recebe. Explicitar quem suporta cada custo.
   Não monetizar autonomia, qualidade ou tempo sem base explícita; tempo liberado
   não equivale automaticamente a redução de folha ou entrada de caixa. Evitar
   contar o mesmo efeito como economia de custo e benefício adicional.
5. **Comparar incrementos.** Apresentar totais por alternativa e diferenças para a
   base: `ΔC = custo da opção − custo da base`, `ΔB = benefício da opção − benefício
   da base`, `saldo incremental = ΔB − ΔC`. Registrar redução de despesa em ΔC,
   sem repeti-la em ΔB. Calcular separadamente por unidade; manter efeitos
   qualitativos visíveis. Definir fórmula e denominador se ROI for pertinente;
   não produzir percentual financeiro exato sem dados suficientes.
6. **Testar cenários e equilíbrio.** Variar hipóteses decisivas em cenários
   conservador, central e favorável quando houver base; sem valores defensáveis,
   formular condições qualitativas ou limiares simbólicos. Não inventar faixas,
   probabilidades ou taxa de desconto. Com ganho líquido recorrente constante e
   positivo, usar `prazo de equilíbrio = custo inicial adicional / ganho líquido
   por período`, na mesma unidade. Se o ganho for nulo/negativo, não há recuperação
   nesse modelo. Com fluxos variáveis, acumular os saldos por período e localizar
   a recuperação; declarar se não ocorrer no horizonte. Explicitar convenção de
   períodos e desconto quando material e sustentado pelos dados.
7. **Recomendar condicionalmente.** Indicar em quais condições compensa mudar,
   manter, adiar ou obter um dado decisivo. Mostrar o que inverte a conclusão,
   riscos, limitações e distribuição de ganhos/perdas, sem forçar uma vencedora.

No Codex, apoiar estimativas em código, diffs, registros ou medições reproduzíveis
disponíveis; considerar integração, revisão, testes, regressões e manutenção como
custos relevantes. Comparar medições sob carga e ambiente compatíveis. Distinguir
teste executado de proposta ou simulação. A análise não acrescenta autorização
para implementar, comprar ou alterar sistemas; respeitar o escopo já autorizado.

Exemplo de chamada: “Use cost-benefit-reasoner para avaliar se vale automatizar
uma rotina de 20 minutos semanais, considerando construção, manutenção e horizonte.”

## Entrega

Apresentar, proporcionalmente à decisão:

- Base, alternativas viáveis, horizonte e tabela de custos/benefícios totais e
  incrementais, com unidades, fontes ou hipóteses e partes que pagam/ganham.
- Benefícios qualitativos separados; cenários, equilíbrio ou motivo para não
  calculá-los; limitações e dados decisivos ausentes.
- Recomendação condicional e condição observável para reconsiderá-la.

## Verificação

Recalcular diferenças e equilíbrio; conferir unidades, horizonte, dependências,
custos omitidos, dupla contagem e beneficiários/pagadores. Conferir que gastos
afundados não comandem a decisão, hipóteses não apareçam como fatos e conclusões
não ultrapassem os cenários e evidências apresentados.

## Condição de parada

Encerrar com comparação suficiente e recomendação condicional. Se faltar dado
essencial, entregar conclusão provisória e a menor coleta necessária, sem ROI
preciso inventado. Não executar as alternativas nem iniciar outras análises,
skills ou acompanhamento fora do escopo autorizado.
