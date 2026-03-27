# Gerador de Assinatura de E-mail

API interna para geração padronizada de assinaturas HTML para e-mail — BT Blue.

## Instalação

```bash
pip install -e ".[dev]"
```

Instala o projeto em modo editável junto com todas as dependências de desenvolvimento (`pytest`, `httpx`, `pytest-asyncio`).

## Executando

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

Documentação interativa disponível em <http://localhost:8000/docs>.

## Testando

```bash
pytest
```
