---
id: RTM
tipo: Matriz de Rastreabilidade
projeto: DevNotes Local
versao: 1.0
status: atual
---

# Matriz de Rastreabilidade — DevNotes Local

Relaciona cada Requisito Funcional (RF) com os Casos de Teste (TC) que o cobrem.

**Legenda de cobertura:**
- **Completa** — todos os cenários principais cobertos por TCs
- **Boa** — cenário principal e ao menos um cenário negativo ou variação cobertos
- **Parcial** — apenas um cenário coberto ou cobertura indireta
- **Manual** — sem TC automatizado; verificação manual necessária
- **Não coberto** — nenhum TC associado

---

## Tabela Completa

| Requisito | Descrição (resumida) | TCs existentes | TCs novos | Cobertura |
|-----------|---------------------|----------------|-----------|-----------|
| RF-001 | Cadastrar conteúdo manualmente | TC-CNT-01, TC-RTE-03, TC-RTE-07 | TC-IFN-01, TC-IFN-02, TC-IFN-03 | Boa |
| RF-002 | Editar conteúdo | TC-CNT-03 | TC-CNT-06, TC-IFN-12, TC-IES-11 | Boa |
| RF-003 | Excluir conteúdo | TC-CNT-04 | TC-CNT-07, TC-IFN-13, TC-IES-08, TC-IES-09 | Boa |
| RF-004 | Pesquisar por texto livre | TC-FTS-01, TC-FTS-02, TC-RTE-04 | TC-SCH-04, TC-IFN-01, TC-IFN-05, TC-IFN-10 | Boa |
| RF-005 | Combinar busca com filtros | TC-FTS-03 | TC-SCH-05, TC-IFN-11, TC-IES-14 | Boa |
| RF-006 | Colar trechos manualmente | TC-CNT-01 (indireto) | — | Parcial |
| RF-007 | Fazer upload de arquivo | TC-RTE-05 | TC-UPL-05, TC-IFN-05, TC-IES-01, TC-IES-04, TC-IES-05 | Boa |
| RF-008 | Salvar arquivo localmente | — | TC-UPL-05 (indireto) | Parcial |
| RF-009 | Validar extensão de arquivo | TC-UPL-01, TC-UPL-02, TC-UPL-03, TC-UPL-ERR-01, TC-UPL-ERR-02 | TC-EXT-06, TC-IFN-07, TC-IES-02 | Completa |
| RF-010 | Validar tamanho máximo (12 MB) | — | TC-UPL-04, TC-IFN-09, TC-IES-03 | Boa |
| RF-011 | Extrair texto / encoding | TC-ENC-01, TC-ENC-02, TC-ENC-03 | TC-ENC-04, TC-IFN-08 | Boa |
| RF-012 | Registrar conteúdo no SQLite | TC-CNT-01 | TC-UPF-01 (indireto) | Parcial |
| RF-013 | Indexar com FTS5 | TC-FTS-01, TC-FTS-02, TC-FTS-03 | TC-FTS-04, TC-FTS-05, TC-IFN-12, TC-IFN-13, TC-IES-09 | Boa |
| RF-014 | Visualizar com `<pre><code>` | — | TC-RND-01, TC-IFN-01, TC-IES-07 | Boa |
| RF-015 | Highlight.js | — | — | Manual |
| RF-016 | Classificar por categoria | TC-CNT-01 | — | Parcial |
| RF-017 | Classificar por linguagem | TC-CLS-01, TC-CLS-02, TC-CLS-08, TC-CLS-09 | TC-IFN-05, TC-IFN-06 | Boa |
| RF-018 | Tags | TC-CNT-01 | TC-IFN-01 | Parcial |
| RF-019 | Sistema e domínio | TC-CNT-01 | TC-IES-14 | Boa |
| RF-020 | Marcar como regra de negócio | TC-CNT-05 | TC-SCH-05 (indireto), TC-IES-13 | Boa |
| RF-021 | Tipo PowerBuilder por extensão | TC-CLS-03, TC-CLS-04, TC-CLS-05, TC-CLS-06, TC-UPL-03 | TC-CLS-10, TC-CLS-11, TC-CLS-12, TC-IFN-06 | Completa |
| RF-022 | config.yaml | — | — | Manual |
| RF-023 | Listar conteúdos | TC-CNT-02, TC-RTE-01, TC-RTE-02 | TC-RTE-08, TC-RTE-09, TC-RTE-10, TC-RTE-11, TC-RTE-12, TC-IES-12 | Completa |
| RF-024 | Exibir detalhes | TC-RTE-07 | TC-RND-02, TC-IES-07 | Boa |
| RF-025 | Registrar metadados de upload | — | TC-UPF-01 | Boa |
| RF-026 | Tags pré-cadastradas | — | — | Manual |
| RF-027 | Múltiplas tags | TC-CNT-01 | — | Parcial |
| RF-028 | Busca sem termo textual | TC-FTS-03 | TC-SCH-05, TC-IFN-11, TC-IES-13 | Boa |
| RF-029 | Mensagens de erro amigáveis | TC-UPL-ERR-01, TC-RTE-06 | TC-UPL-04 (mensagem), TC-IFN-02, TC-IFN-04, TC-IFN-07, TC-IES-06, TC-IES-10 | Boa |
| RF-030 | Data de criação/atualização | — | — | Não coberto |

---

## RFs sem cobertura automatizada

| Requisito | Situação | Recomendação |
|-----------|----------|--------------|
| RF-015 | Manual | Verificar visualmente Highlight.js na tela de detalhe |
| RF-022 | Manual | Verificar que extensões e listas refletem o `config.yaml` |
| RF-026 | Manual | Verificar seleção de tags pré-cadastradas no formulário |
| RF-030 | Não coberto | Adicionar TC verificando `created_at` e `updated_at` no banco |

---

## Totais por cobertura

| Cobertura | Quantidade de RFs |
|-----------|------------------|
| Completa | 3 |
| Boa | 17 |
| Parcial | 6 |
| Manual | 3 |
| Não coberto | 1 |
| **Total** | **30** |
