---
id: TASK-015
titulo: Classificar automaticamente por extensão
feature: FEAT-001
user_story: US-001
status: a_fazer
dependencias: TASK-006, TASK-014
---

# TASK-015 — Classificar automaticamente por extensão

## Descrição

Implementar classificação automática de linguagem e tipo de objeto com base na extensão do arquivo.

---

## Critérios de aceitação

- Arquivos `.py` são classificados como Python.
- Arquivos `.java` são classificados como Java.
- Arquivos `.sql` são classificados como SQL.
- Arquivos `.md` são classificados como Markdown.
- Arquivos `.txt` são classificados como Texto.
- Arquivos PowerBuilder são classificados como linguagem PowerBuilder.
- Arquivos PowerBuilder recebem tipo de objeto conforme extensão:
  - `.srw` → PowerBuilder Window
  - `.sru` → PowerBuilder User Object
  - `.srd` → PowerBuilder DataWindow
  - `.srm` → PowerBuilder Menu
  - `.srf` → PowerBuilder Function
  - `.sra` → PowerBuilder Application
  - `.srs` → PowerBuilder Structure

---

## Dependências

TASK-006, TASK-014.

---

## Observações técnicas

O mapeamento deve vir do `config.yaml`.
