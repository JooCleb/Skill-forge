---
name: uncertainty-calibrator
description: Calibre a certeza de conclusões e comunique limites de evidência mediante pedido explícito dessa análise ou etapa nomeada em workflow já autorizado, no ChatGPT Work ou no Codex quando houver código. Aplica-se a generalizações de amostras, inferências, estimativas, hipóteses e conclusões limitadas por dados, modelos ou acesso. Não use para acrescentar ressalvas a fatos simples e conferidos, traduzir ou revisar apenas o estilo de textos sobre incerteza, nem fabricar percentuais de confiança sem base justificável.
---

# uncertainty-calibrator

## Entradas

- Identificar a conclusão a calibrar, o público e o alcance pretendido: população, período, condições ou ambiente.
- Usar evidências e artefatos disponíveis, com sua origem, método e limitações relevantes. Perguntar apenas pelo que mudaria materialmente a avaliação; se faltar, explicitar o limite e avançar até onde for possível.

## Procedimento

1. **Delimitar a análise.** Confirmar o pedido explícito ou a etapa nomeada no escopo autorizado. Separar alegações compostas quando tiverem bases diferentes. Não transformar uma revisão comum em auditoria geral nem chamar outras meta-skills automaticamente.
2. **Separar os tipos de afirmação.** Distinguir fato observado ou verificado, inferência derivada, estimativa dependente de método e hipótese ainda não estabelecida. Vincular cada afirmação material à evidência identificável; preservar fatos confirmados mesmo quando a extrapolação for incerta.
3. **Localizar as incertezas materiais.** Examinar as categorias abaixo sem exigir que todas apareçam na entrega nem contá-las duas vezes:
   - **Dados:** medição, registros incompletos, qualidade, procedência e atualidade.
   - **Modelo:** pressupostos, especificação, simplificações e transferência para outras condições.
   - **Amostra:** tamanho, variabilidade, seleção, representatividade e dependência entre observações. Distinguir imprecisão de viés: aumentar a amostra não corrige por si só seleção inadequada.
   - **Acesso:** fontes, arquivos, sistemas ou ambientes indisponíveis. Ausência de acesso não demonstra ausência do fenômeno nem falsidade da conclusão.
4. **Ajustar a linguagem à evidência.** Considerar relevância, qualidade, independência, convergência, evidência contrária e alternativas plausíveis. Usar qualificadores com motivo e alcance: “observado nestas condições”, “os dados sugerem”, “estimativa sob estas premissas” ou “ainda não é possível concluir”. Reservar afirmações categóricas para o que foi sustentado; evitar ressalvas vagas e igualdade artificial entre alternativas com suportes distintos. Separar a força da evidência da importância ou do risco da decisão.
5. **Quantificar somente com fundamento.** Usar probabilidades ou intervalos apenas com método identificável, dados ou limites justificáveis e pressupostos explícitos; declarar o evento ou parâmetro, a população e o significado da medida. Não converter rótulos qualitativos em percentuais nem confundir intervalo de confiança, intervalo de predição e probabilidade da hipótese. Se pedirem um percentual sem base, dizer que o número não é justificável e oferecer formulação qualitativa, indicando o que permitiria quantificar. Preservar contagens e taxas descritivas observadas, sem tratá-las como taxas universais ou probabilidades para novos casos.
6. **Tornar o limite útil.** Dizer qual evidência ou resultado mudaria a conclusão, em que direção e por quê. Propor poucas formas viáveis de reduzir as incertezas materiais, proporcionais à necessidade. Não prometer eliminar toda incerteza nem iniciar pesquisa, coleta ou ação externa fora do escopo autorizado.

No Codex, vincular afirmações aos arquivos, versões, logs e resultados realmente disponíveis. Diferenciar inspeção de código, teste executado e comportamento inferido; limitar conclusões às condições cobertas. Testes locais aprovados não estabelecem correção em produção ou para todas as entradas. Não afirmar acessos ou testes que não ocorreram.

## Entrega

Apresentar uma conclusão reescrita com qualificadores precisos. Acrescentar apenas as incertezas que alterem sua interpretação e as evidências correspondentes, distinguindo o estabelecido do inferido, estimado ou hipotético. Indicar formas de reduzir os limites e o que mudaria a conclusão. Usar parágrafo curto ou lista conforme a complexidade, sem formulário vazio ou dúvida artificial.

## Verificação e parada

- Conferir se cada qualificador decorre de evidência ou lacuna observável; retirar ressalvas genéricas e números sem base.
- Conferir se o alcance foi preservado, alternativas relevantes foram consideradas e nenhuma falta de acesso foi apresentada como refutação. Fornecer justificativas verificáveis, sem solicitar ou expor deliberação interna privada.
- Encerrar quando a conclusão, seus limites materiais e as condições de revisão estiverem claros. Se faltar evidência decisiva, registrar o que permanece indeterminado e o mínimo necessário para avançar; não prolongar a avaliação por investigação indefinida.
