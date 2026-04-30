---
id: TC-CLS
tipo: Casos de Teste
modulo: extension_classifier
projeto: DevNotes Local
versao: 1.0
---

# Casos de Teste — ExtensionClassifier

Arquivo de implementação: `backend/app/services/extension_classifier.py`
Arquivo de testes: `tests/test_extension_classifier.py`

---

## TC-CLS-01 — Classificar .py como Python

| Campo | Valor |
|-------|-------|
| **ID** | TC-CLS-01 |
| **Título** | Classificar .py como Python |
| **Módulo** | `backend/app/services/extension_classifier.py` |
| **Requisito** | RF-017 |
| **Pré-condição** | Nenhuma |
| **Passos** | 1. Chamar `classify(".py")` |
| **Entrada** | `".py"` |
| **Resultado Esperado** | `language == "Python"`, `object_type == "Python"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Alta |

**Docstring:** `"""TC-CLS-01 | Unitário | Classificar .py como Python."""`

---

## TC-CLS-02 — Classificar .sql como SQL

| Campo | Valor |
|-------|-------|
| **ID** | TC-CLS-02 |
| **Título** | Classificar .sql como SQL |
| **Módulo** | `backend/app/services/extension_classifier.py` |
| **Requisito** | RF-017 |
| **Pré-condição** | Nenhuma |
| **Passos** | 1. Chamar `classify(".sql")` |
| **Entrada** | `".sql"` |
| **Resultado Esperado** | `language == "SQL"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Alta |

**Docstring:** `"""TC-CLS-02 | Unitário | Classificar .sql como SQL."""`

---

## TC-CLS-03 — Classificar .srw como PowerBuilder Window

| Campo | Valor |
|-------|-------|
| **ID** | TC-CLS-03 |
| **Título** | Classificar .srw como PowerBuilder Window |
| **Módulo** | `backend/app/services/extension_classifier.py` |
| **Requisito** | RF-021 |
| **Pré-condição** | Nenhuma |
| **Passos** | 1. Chamar `classify(".srw")` |
| **Entrada** | `".srw"` |
| **Resultado Esperado** | `language == "PowerBuilder"`, `object_type == "PowerBuilder Window"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Alta |

**Docstring:** `"""TC-CLS-03 | Unitário | Classificar .srw como PowerBuilder Window."""`

---

## TC-CLS-04 — Classificar .srd como PowerBuilder DataWindow

| Campo | Valor |
|-------|-------|
| **ID** | TC-CLS-04 |
| **Título** | Classificar .srd como PowerBuilder DataWindow |
| **Módulo** | `backend/app/services/extension_classifier.py` |
| **Requisito** | RF-021 |
| **Pré-condição** | Nenhuma |
| **Entrada** | `".srd"` |
| **Resultado Esperado** | `language == "PowerBuilder"`, `object_type == "PowerBuilder DataWindow"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Alta |

**Docstring:** `"""TC-CLS-04 | Unitário | Classificar .srd como PowerBuilder DataWindow."""`

---

## TC-CLS-05 — Classificar .srm como PowerBuilder Menu

| Campo | Valor |
|-------|-------|
| **ID** | TC-CLS-05 |
| **Título** | Classificar .srm como PowerBuilder Menu |
| **Módulo** | `backend/app/services/extension_classifier.py` |
| **Requisito** | RF-021 |
| **Entrada** | `".srm"` |
| **Resultado Esperado** | `object_type == "PowerBuilder Menu"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Média |

**Docstring:** `"""TC-CLS-05 | Unitário | Classificar .srm como PowerBuilder Menu."""`

---

## TC-CLS-06 — Classificar .srf como PowerBuilder Function

| Campo | Valor |
|-------|-------|
| **ID** | TC-CLS-06 |
| **Título** | Classificar .srf como PowerBuilder Function |
| **Módulo** | `backend/app/services/extension_classifier.py` |
| **Requisito** | RF-021 |
| **Entrada** | `".srf"` |
| **Resultado Esperado** | `object_type == "PowerBuilder Function"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Média |

**Docstring:** `"""TC-CLS-06 | Unitário | Classificar .srf como PowerBuilder Function."""`

---

## TC-CLS-07 — Retornar "Outro" para extensão desconhecida

| Campo | Valor |
|-------|-------|
| **ID** | TC-CLS-07 |
| **Título** | Retornar "Outro" para extensão desconhecida |
| **Módulo** | `backend/app/services/extension_classifier.py` |
| **Requisito** | RF-021 |
| **Entrada** | `".xyz"` |
| **Resultado Esperado** | `language == "Outro"`, `object_type == ""` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Baixa |

**Docstring:** `"""TC-CLS-07 | Unitário | Retornar Outro para extensão desconhecida."""`

---

## TC-CLS-08 — Classificar .md como Markdown

| Campo | Valor |
|-------|-------|
| **ID** | TC-CLS-08 |
| **Título** | Classificar .md como Markdown |
| **Módulo** | `backend/app/services/extension_classifier.py` |
| **Requisito** | RF-017 |
| **Entrada** | `".md"` |
| **Resultado Esperado** | `language == "Markdown"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Baixa |

**Docstring:** `"""TC-CLS-08 | Unitário | Classificar .md como Markdown."""`

---

## TC-CLS-09 — Classificar .java como Java

| Campo | Valor |
|-------|-------|
| **ID** | TC-CLS-09 |
| **Título** | Classificar .java como Java |
| **Módulo** | `backend/app/services/extension_classifier.py` |
| **Requisito** | RF-017 |
| **Entrada** | `".java"` |
| **Resultado Esperado** | `language == "Java"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Baixa |

**Docstring:** `"""TC-CLS-09 | Unitário | Classificar .java como Java."""`

---

## TC-CLS-10 — Classificar .sru como PowerBuilder User Object *(novo)*

| Campo | Valor |
|-------|-------|
| **ID** | TC-CLS-10 |
| **Título** | Classificar .sru como PowerBuilder User Object |
| **Módulo** | `backend/app/services/extension_classifier.py` |
| **Requisito** | RF-021 |
| **Entrada** | `".sru"` |
| **Resultado Esperado** | `language == "PowerBuilder"`, `object_type == "PowerBuilder User Object"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Baixa |

**Docstring:** `"""TC-CLS-10 | Unitário | .sru deve classificar como PowerBuilder User Object."""`

---

## TC-CLS-11 — Classificar .sra como PowerBuilder Application *(novo)*

| Campo | Valor |
|-------|-------|
| **ID** | TC-CLS-11 |
| **Título** | Classificar .sra como PowerBuilder Application |
| **Módulo** | `backend/app/services/extension_classifier.py` |
| **Requisito** | RF-021 |
| **Entrada** | `".sra"` |
| **Resultado Esperado** | `object_type == "PowerBuilder Application"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Baixa |

**Docstring:** `"""TC-CLS-11 | Unitário | .sra deve classificar como PowerBuilder Application."""`

---

## TC-CLS-12 — Classificar .srs como PowerBuilder Structure *(novo)*

| Campo | Valor |
|-------|-------|
| **ID** | TC-CLS-12 |
| **Título** | Classificar .srs como PowerBuilder Structure |
| **Módulo** | `backend/app/services/extension_classifier.py` |
| **Requisito** | RF-021 |
| **Entrada** | `".srs"` |
| **Resultado Esperado** | `object_type == "PowerBuilder Structure"` |
| **Resultado Obtido** | |
| **Status** | |
| **Tipo** | Unitário |
| **Prioridade** | Baixa |

**Docstring:** `"""TC-CLS-12 | Unitário | .srs deve classificar como PowerBuilder Structure."""`
