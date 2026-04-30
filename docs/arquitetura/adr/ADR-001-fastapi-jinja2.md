---
id: ADR-001
title: Uso de FastAPI com Jinja2 para renderização server-side
status: Aceito
data: 2026-04-29
---

## Contexto

O projeto DevNotes Local é uma aplicação web de uso individual e local. É necessário escolher como a camada web será construída: se com renderização server-side (SSR) ou com uma SPA separada comunicando-se via API JSON.

## Decisão

Usar FastAPI como framework web Python com Jinja2 para renderização de templates HTML no servidor. Não haverá SPA, frontend separado, build pipeline ou framework JavaScript.

## Justificativa

- FastAPI oferece rotas claras, validação de entrada com Pydantic, suporte nativo a upload de arquivos e servidor embutido via Uvicorn.
- Jinja2 renderiza páginas HTML no servidor sem necessidade de build, Node.js ou separação de API.
- Para um MVP local com uso individual, a complexidade de uma SPA não é justificada.
- A curva de aprendizado é menor, o que favorece o objetivo didático do projeto.

## Consequências

**Fica mais fácil:**
- Iniciar e executar a aplicação com um único comando (`uvicorn`).
- Manter o projeto como um único repositório e um único processo.
- Escrever templates sem depender de toolchain de frontend.

**Fica mais difícil:**
- Implementar interações ricas no cliente sem JavaScript adicional.
- Migrar para uma SPA no futuro exigiria refatoração das rotas para retornar JSON.

## Alternativas descartadas

| Alternativa | Motivo do descarte |
|---|---|
| React / Vue + API FastAPI | Exige Node.js, build pipeline, separação de projetos e dobra a complexidade |
| Flask + Jinja2 | FastAPI oferece validação de entrada e suporte a async nativamente |
| Django | Excesso de funcionalidades para um MVP local sem autenticação ou admin |
