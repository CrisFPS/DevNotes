---
id: TC-IFN
tipo: Casos de Teste
modulo: integracao-funcional
projeto: DevNotes Local
versao: 1.0
---

# Casos de Teste — Integração funcional das rotas

Arquivos de implementação: `backend/app/routes/content_routes.py`, `upload_routes.py`, `search_routes.py`
Arquivo de testes: `tests/test_integracao_funcional.py`
Prompts: `prompts/10.01_Prompt_de_Teste_de_Integracao_Funcional_v1.md`, `prompts/10.02_Prompt_de_Teste_de_Integracao_Funcional_v2.md`

A primeira versão do prompt, sem contrato, gerou quatro casos com rotas JSON inexistentes. Esse registro está em `docs/testes/casos/gerados/funcional_v1.py` e não entra na suíte: o nome do arquivo não começa com `test_`. Os casos abaixo são a versão ajustada, com o contrato HTTP do DevNotes.

| ID | Teste | O que verifica | Requisito |
|----|-------|----------------|-----------|
| TC-IFN-01 | `test_cadastro_valido_redireciona_e_fica_pesquisavel` | POST `/content/new` válido responde 303, o detalhe mostra título, tag e `<pre><code>`, e a busca encontra o texto | RF-001, RF-004, RF-013, RF-014 |
| TC-IFN-02 | `test_cadastro_sem_titulo_nao_persiste` | Sem o campo `title`, a resposta é 4xx e o texto não aparece na listagem | RF-001, RF-029 |
| TC-IFN-03 | `test_campos_opcionais_vazios_ainda_cadastram` | Só o título preenchido ainda cadastra | RF-001 |
| TC-IFN-04 | `test_detalhe_de_id_inexistente_exibe_pagina_404` | GET de id inexistente responde 404 com "não encontrado" | RF-024, RF-029 |
| TC-IFN-05 | `test_upload_sql_integra_arquivo_classificacao_e_busca` | Upload `.sql` responde 303, grava o texto, mostra SQL e a busca encontra | RF-007, RF-017 |
| TC-IFN-06 | `test_upload_powerbuilder_classifica_linguagem` | Upload `.srw` mostra a linguagem PowerBuilder | RF-021 |
| TC-IFN-07 | `test_upload_extensao_recusada_permanece_no_formulario` | Extensão `.xlsx` responde 400 no formulário e não entra na listagem | RF-009, RF-029 |
| TC-IFN-08 | `test_upload_latin1_preserva_texto` | Arquivo latin-1 preserva o acento no detalhe | RF-011 |
| TC-IFN-09 | `test_upload_acima_de_12_mb_e_recusado` | Arquivo de 12 MB + 1 byte responde 400 | RF-010 |
| TC-IFN-10 | `test_busca_sem_resultado_nao_mostra_outro_titulo` | Termo inexistente não mostra outra nota | RF-004 |
| TC-IFN-11 | `test_filtro_de_linguagem_exclui_outra_particao` | `language=SQL` exclui a nota Python | RF-005, RF-028 |
| TC-IFN-12 | `test_editar_atualiza_o_que_a_busca_encontra` | Depois da edição, a busca encontra o texto novo | RF-002, RF-013 |
| TC-IFN-13 | `test_excluir_remove_da_busca` | Depois da exclusão, a busca não encontra o texto | RF-003, RF-013 |

Pré-condição comum: fixtures `client` e, nos uploads, `upload_dir`. O banco é SQLite em memória.
