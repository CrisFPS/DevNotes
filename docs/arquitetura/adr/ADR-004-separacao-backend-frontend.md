---
id: ADR-004
title: Separação física backend/frontend sem dois projetos independentes
status: Aceito
data: 2026-04-29
---

## Contexto

A aplicação é monolítica, mas precisa de organização clara entre a lógica de servidor e a camada de apresentação. É necessário decidir como estruturar os diretórios sem criar dois projetos separados.

## Decisão

Separar fisicamente `backend/` e `frontend/` como diretórios distintos dentro de um único projeto. O FastAPI em `backend/` serve tanto as rotas quanto os arquivos estáticos de `frontend/static/`. Os templates em `frontend/templates/` são renderizados pelo Jinja2 configurado no FastAPI.

## Justificativa

- A separação física deixa claro onde está cada tipo de artefato (lógica de servidor vs. apresentação).
- Não cria dois processos, dois `requirements.txt`, dois repositórios ou duas pipelines.
- Mantém o projeto didático: o aluno consegue identificar onde cada camada está sem confundir responsabilidades.
- É compatível com a decisão de usar Jinja2 para renderização server-side (ADR-001).

## Consequências

**Fica mais fácil:**
- Localizar templates, CSS e JS sem misturá-los com código Python.
- Entender a separação de responsabilidades sem a complexidade de múltiplos projetos.

**Fica mais difícil:**
- Migrar para uma SPA no futuro exigiria mover `frontend/` para um projeto separado com seu próprio toolchain.

## O que não é esta decisão

Esta decisão **não** significa que backend e frontend são projetos independentes. Não há dois servidores, dois processos nem duas pipelines. É uma única aplicação Python com organização de diretórios clara.

## Alternativas descartadas

| Alternativa | Motivo do descarte |
|---|---|
| Tudo dentro de `app/` sem separação | Mistura lógica de servidor com templates; dificulta leitura |
| Dois repositórios separados | Excesso de complexidade para um MVP local monolítico |
