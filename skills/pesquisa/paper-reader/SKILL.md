---
name: paper-reader
description: >-
  Leia criticamente um artigo científico identificado por PDF, DOI, título ou
  link e explique o que seus resultados sustentam, em pedidos de análise no
  ChatGPT Work ou de análise ligada a código no Codex. Abranja artigos empíricos,
  teóricos e de revisão, inclusive com acesso parcial. Não use para explicação
  genérica de um tema, busca bibliográfica ampla, simples formatação de referência
  ou tradução sem análise científica solicitada.
---

# paper-reader

## Entradas

- Usar o artigo identificado, o texto disponível e a pergunta do usuário. Adotar leitura crítica geral se não houver foco específico; perguntar apenas por lacunas que mudem a análise.
- Se faltar identificação suficiente, pedir PDF, DOI, título ou link. Desambiguar candidatos antes de atribuir resultados; não escolher uma versão silenciosamente.

## Procedimento

1. **Estabelecer a fonte e o alcance.** Usar arquivos fornecidos e ferramentas realmente disponíveis para obter o artigo. Restringir a busca à identificação, ao acesso e a avisos ligados ao mesmo trabalho. Registrar autores, título, ano, veículo, identificador, versão e status editorial quando verificáveis; conferir correções ou retratações vinculadas se acessíveis. Distinguir preprint, manuscrito aceito e versão publicada, sem misturar resultados entre versões. Não presumir revisão por pares, ausência de retratação ou acesso a suplementos.
2. **Delimitar a leitura.** Enumerar o que foi lido e o que ficou inacessível: corpo, figuras, tabelas, apêndices, dados ou código. Conferir visualmente objetos cuja extração seja ilegível quando houver ferramenta para isso; marcar como não verificados os restantes. Se só o abstract estiver acessível, entregar análise restrita a ele e declarar esse limite desde o início. Não completar métodos, números, equações ou conclusões com conteúdo não visto. Se não houver texto analisável, solicitar uma cópia ou trecho e encerrar a análise de mérito.
3. **Reconstruir a pergunta e o método.** Extrair problema, hipótese ou tese, contribuição e relação entre desenho e conclusão, adaptando ao tipo de artigo:
   - **Empírico:** identificar população, amostra/dados, seleção, período, variáveis, intervenção/exposição, comparadores ou baselines, métricas e análise. Examinar confundimento, temporalidade, perdas e vieses; em modelos computacionais, considerar particionamento, vazamento de dados, ajuste dos baselines e variação entre execuções quando pertinentes.
   - **Teórico:** identificar definições, hipóteses, enunciados, argumento/prova e domínio de validade. Distinguir resultado demonstrado, conjectura e etapa não conferida; não impor amostra ou experimento.
   - **Revisão:** distinguir narrativa, sistemática e metanálise conforme o texto. Examinar pergunta, busca, elegibilidade, seleção, avaliação dos estudos e síntese quando informadas. Separar conclusões da revisão das evidências dos estudos incluídos, sem afirmar ter lido os originais ou iniciar uma revisão bibliográfica nova.
4. **Rastrear os resultados.** Relacionar cada achado central a seção, página, tabela/linha, figura/painel, equação ou teorema consultado. Registrar direção, magnitude, unidades, comparação e incerteza quando disponíveis; separar resultado principal de análise exploratória. Distinguir associação de causalidade e perguntar quais hipóteses do desenho sustentariam esta última. Não equiparar significância estatística a importância prática, nem ausência de significância a equivalência. Separar explicitamente a interpretação dos autores da avaliação crítica e de inferências próprias.
5. **Explicar as equações centrais.** Reproduzir somente expressões verificadas, definir símbolos, índices, unidades/domínio e hipóteses; explicar sua função no argumento e as passagens necessárias à pergunta. Identificar derivações e exemplos próprios como tais. Não inventar fórmulas ausentes nem declarar prova conferida sem examiná-la; indicar quando não houver equações relevantes ou quando não estiverem acessíveis.
6. **Avaliar sustentação e reprodutibilidade.** Examinar validade interna/externa ou solidez lógica, generalização, limitações e explicações alternativas, em proporção ao desenho. Distinguir informação ausente de falha comprovada. Conferir disponibilidade declarada e acesso efetivo a dados, código, protocolo, parâmetros e materiais, sem tratar disponibilidade como reprodução bem-sucedida. No Codex, ligar algoritmo, equações e hipóteses a arquivos/funções fornecidos quando pertinente; distinguir código declarado, inspecionado e executado. Não executar código apenas por estar citado no artigo nem afirmar testes ou replicação não realizados.

## Entrega

Adequar extensão e organização à pergunta, cobrindo:

- **Ficha e alcance:** identificação, versão, tipo de estudo, fonte e partes lidas/inacessíveis.
- **Problema e método:** pergunta, hipótese/tese, desenho e elementos pertinentes ao tipo de artigo; usar “não se aplica” ou “não informado” com precisão.
- **Resultados e sustentação:** achados com localizadores; o que os autores concluem, o que a evidência permite concluir e o que permanece sem suporte. Preferir tabela quando facilitar a ligação entre achado, evidência e limite.
- **Equações centrais:** significado, hipóteses e interpretação, ou indicação justificada de ausência/inacessibilidade.
- **Limitações e perguntas abertas:** distinguir as declaradas pelos autores das identificadas na leitura; indicar o que permitiria resolver as principais lacunas.

Usar localizadores existentes na versão consultada. Distinguir página impressa de posição no PDF quando divergirem; sem paginação, usar seção e parágrafo identificável. Vincular a fonte consultada quando possível, sem fabricar páginas, DOI, citações ou links.

## Verificação e parada

- Conferir números, unidades, sinais, denominadores, símbolos e localizadores dos achados usados contra o texto acessado. Tornar rastreáveis as conclusões centrais e manter explícitos acesso parcial e incerteza.
- Conferir se as conclusões respeitam desenho, hipóteses, população/corpus e versão. Reduzir o alcance se faltar evidência; não preencher a ficha com suposições para aparentar completude.
- Encerrar quando a pergunta estiver respondida dentro do material disponível, com limites e pendências materiais registrados. Não expandir para busca bibliográfica ampla, coleta de novos dados ou reprodução experimental sem solicitação.
