# Testar skills

Um teste descreve entrada, contexto e comportamento observável esperado. Prepare pelo menos casos pertinentes de acionamento positivo, não acionamento e fronteira; adicione falha de ferramenta, conteúdo incompleto ou instruções conflitantes quando forem riscos reais. O [modelo de casos](../templates/skill/test-cases.md) ajuda a registrar o desenho.

Execute os casos no ambiente em que a skill será usada. Registre versão ou commit, data, modelo e configuração quando disponíveis, entrada, saída observada, critério e resultado. Compare comportamento com o resultado esperado sem exigir formulações idênticas quando várias respostas corretas forem possíveis.

Reexecute casos afetados por mudanças e mantenha regressões para falhas reais. Um caso documentado e não executado permanece «planejado». A verificação de YAML, por si só, não testa seleção, execução ou qualidade.
