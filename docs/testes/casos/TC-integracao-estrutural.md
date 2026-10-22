---
id: TC-IES
tipo: Casos de Teste
modulo: integracao-estrutural
projeto: DevNotes Local
versao: 1.0
---

# Casos de Teste — Integração estrutural das rotas

Arquivos de implementação: `backend/app/routes/content_routes.py`, `upload_routes.py`, `search_routes.py`
Arquivo de testes: `tests/test_integracao_estrutural.py`
Prompts: `prompts/10.03_Prompt_de_Teste_de_Integracao_Estrutural_v1.md`, `prompts/10.04_Prompt_de_Teste_de_Integracao_Estrutural_v2.md`

A primeira versão pedia cobertura de decisões, mas esperava códigos de API JSON (201, 406, 204). Esses quatro casos estão em `docs/testes/casos/gerados/estrutural_v1.py` e não entram na suíte. Os casos abaixo cobrem os desvios reais das rotas.

| ID | Teste | Desvio | Requisito |
|----|-------|--------|-----------|
| TC-IES-01 | `test_upload_com_sucesso_redireciona_303` | `save_upload` sem exceção responde 303 | RF-007 |
| TC-IES-02 | `test_upload_com_extensao_invalida_devolve_400` | Exceção de extensão responde 400 | RF-009 |
| TC-IES-03 | `test_upload_no_limite_passa_e_um_byte_acima_falha` | Tamanho igual ao limite passa; um byte acima responde 400. O limite do teste é 8 bytes | RF-010 |
| TC-IES-04 | `test_upload_sem_titulo_usa_nome_do_arquivo` | Título em branco usa o nome original do arquivo | RF-007 |
| TC-IES-05 | `test_upload_com_titulo_preserva_o_titulo_informado` | Título informado permanece; o nome do arquivo fica nos metadados | RF-007 |
| TC-IES-06 | `test_detalhe_inexistente_renderiza_404` | Item ausente no detalhe responde 404 | RF-029 |
| TC-IES-07 | `test_detalhe_existente_renderiza_codigo` | Item presente renderiza `<pre><code>` | RF-014, RF-024 |
| TC-IES-08 | `test_excluir_id_inexistente_redireciona_para_lista` | Exclusão sem item redireciona para `/content` | RF-003 |
| TC-IES-09 | `test_excluir_id_existente_sai_do_indice` | Exclusão com item tira o texto da busca | RF-003, RF-013 |
| TC-IES-10 | `test_falha_ao_excluir_renderiza_erro_500` | Exceção em `delete` responde 500 | RF-029 |
| TC-IES-11 | `test_editar_id_inexistente_redireciona` | Edição sem item redireciona para `/content` | RF-002 |
| TC-IES-12 | `test_pagina_abaixo_de_um_ainda_lista` | Página menor que 1 e página acima do total ainda mostram o item | RF-023 |
| TC-IES-13 | `test_busca_sem_texto_aplica_so_filtro_de_regra` | Busca sem texto, com regra de negócio, devolve só a regra | RF-020, RF-028 |
| TC-IES-14 | `test_busca_com_filtros_preenchidos_monta_o_dicionario` | Categoria, linguagem, sistema e domínio filtram juntos | RF-005, RF-019 |

Pré-condição comum: fixtures `client` e, nos uploads, `upload_dir`. O banco é SQLite em memória.
