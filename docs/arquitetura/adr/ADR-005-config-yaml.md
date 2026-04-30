---
id: ADR-005
title: Uso de config.yaml para centralizar listas e mapeamentos
status: Aceito
data: 2026-04-29
---

## Contexto

A aplicação precisa manter listas de sistemas, domínios, linguagens, extensões aceitas, mapeamentos entre extensão e tipo de objeto PowerBuilder, e tags pré-cadastradas. Essas listas podem mudar sem necessidade de alterar o código Python.

## Decisão

Centralizar todas as listas e mapeamentos em um único arquivo `config.yaml` na raiz do projeto. O backend carrega esse arquivo na inicialização e expõe os dados via um módulo `config.py`.

## Justificativa

- Separar configuração de código é uma prática consolidada (12-factor app).
- `config.yaml` é legível por humanos e editável sem conhecimento de Python.
- Evita constantes espalhadas pelo código em múltiplos arquivos.
- Permite ao usuário adicionar um novo sistema ou linguagem sem tocar no código da aplicação.

## Consequências

**Fica mais fácil:**
- Adicionar novos sistemas, domínios ou linguagens sem alterar código Python.
- Revisar e auditar as listas em um único lugar.
- Versionar a configuração junto com o código via Git.

**Fica mais difícil:**
- Validar o arquivo YAML em runtime (um YAML malformado pode causar erro na inicialização).

## Mitigação

Adicionar validação mínima no `config.py` ao carregar o arquivo, com mensagem de erro clara se a estrutura estiver incorreta.

## Alternativas descartadas

| Alternativa | Motivo do descarte |
|---|---|
| Constantes em arquivos `.py` | Espalhadas pelo código; exige edição de Python para mudar uma lista |
| Banco de dados para listas | Excesso de complexidade para dados que raramente mudam |
| Variáveis de ambiente | Adequadas para credenciais, não para listas estruturadas |
| `.env` | Formato inadequado para listas e mapeamentos hierárquicos |
