---
name: skill-composer
description: >-
  Projete a composição de skills específicas mediante pedido explícito de combiná-las
  ou etapa nomeada de composição em workflow autorizado, no Work ou no Codex.
  Não use para mera seleção, tarefa comum sem essa análise ou execução automática
  do catálogo. O desenho não autoriza executar etapas nem alterar as skills.
---

# skill-composer

## Entradas

Recuperar objetivo, entrega, skills indicadas, formatos, critérios de aceite e limites de autorização. Ler os contratos atuais e somente recursos necessários; registrar origem e versão disponível. Pedir apenas lacunas que mudem o desenho. Acesso necessário só na execução futura pode ficar como pendência; contrato inacessível torna a compatibilidade provisória.

## Procedimento

1. **Delimitar responsabilidades.** Extrair de cada contrato entradas, saídas, pré-condições, efeitos, exclusões e término. Ler não significa executar. Atribuir um responsável por transformação; retirar redundâncias sem eliminar verificações complementares exigidas. Resolver conflitos pelas instruções vigentes; obrigações incompatíveis bloqueiam a combinação, sem enfraquecê-las silenciosamente.
2. **Definir a passagem.** Vincular conteúdo e formato/schema a ID e revisão do artefato, fontes/localizações, contexto temporal, incertezas, estado de verificação e pendências. Mapear cada saída à entrada seguinte. Preservar a associação entre afirmação e evidência após reordenação ou reescrita; aprovação sem evidência não basta.
3. **Ordenar.** Construir dependências com IDs, distinguindo obrigatórias e opcionais. Examinar também chamadas internas: A → B → A e autochamadas impedem o desenho executável. Propor remoção de dependência opcional ou mudança autorizada de contrato; um limite de rodadas não resolve ciclo obrigatório. Prever paralelismo só com independência, capacidade real e ausência de disputa por estado.
4. **Adaptar interfaces.** Especificar conversão de campos, tipos, unidades e precisão; listar informação preservada, transformada, perdida ou não verificada. Usar artefato complementar ligado ao mesmo ID/revisão para dados não representáveis no destino. Conferir contagens/IDs e reconstrução quando aplicável. Bloquear passagem com perda material sem preservação rastreável.
5. **Fixar critérios de avanço.** Associar cada verificação a requisito de qualidade, compatibilidade, atualidade ou autorização realmente pendente. Aproveitar autorização já dada e evidências ainda válidas. Separar desenho compatível, execução habilitada e execução comprovada; não inserir confirmações rituais.
6. **Planejar retomada.** Registrar último artefato válido, revisão, etapa, efeitos e falha. Após mudança, invalidar apenas saídas/verificações dependentes. Antes de repetir ação de resultado desconhecido, conferir efeitos já aplicados; prever reversão viável e parada por falta de progresso. Correções locais devem ter limite e critério de término, sem invocação recíproca de skills.
7. **Oferecer alternativa mínima.** Remover dependências opcionais ou executar diretamente a capacidade com ferramentas existentes, explicitando limites de equivalência. Falta de capacidade obrigatória permanece bloqueio.

No Work, usar referências reais aos documentos; no Codex, ligar evidências a arquivos, revisão/diff, comandos e resultados. Não presumir acesso, memória entre chats, ferramentas ou testes. Não chamar outras meta-skills automaticamente nem solicitar deliberação interna privada.

## Entrega

Apresentar objetivo/premissas e uma tabela proporcional ao trabalho:

`Etapa/responsável | Dependências/entrada | Saída/evidências | Critério de avanço | Falha/retomada`

Incluir contratos consultados, adaptações/perdas, alternativa mínima e critérios finais. Classificar o desenho como compatível, provisório ou inviável, separadamente de sua execução.

## Verificação e parada

Conferir ausência de ciclos, responsabilidades, interfaces, rastreabilidade, retomada finita e cobertura da entrega. Distinguir inspeção, simulação e execução; não afirmar roteamento observado sem registro.

Encerrar com o workflow e pendências. Executar etapas apenas se a execução também estiver no pedido autorizado; não criar skills, publicar ou iniciar acompanhamento por consequência do desenho.
