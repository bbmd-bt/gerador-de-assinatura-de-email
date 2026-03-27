# Gerador de Assinatura de E-mail

API interna para geração padronizada de assinaturas HTML para e-mail – BT Blue.

## Visão Geral

Projeto FastAPI que fornece endpoints para geração e customização de assinaturas de e-mail em HTML. Utiliza templates Jinja2 e banco de dados PostgreSQL com SQLAlchemy para persistência.

**Status**: ![Python](https://img.shields.io/badge/Python-3.11+-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green)

## Pré-requisitos

- Python 3.11+
- PostgreSQL (ou Docker)
- pip

## Instalação

### Desenvolvimento

```bash
# Clonar repositório
git clone https://github.com/bbmd-bt/gerador-de-assinatura-de-email.git
cd gerador-de-assinatura-de-email

# Criar virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\Activate.ps1  # Windows

# Instalar em modo edível com dependências de dev
pip install -e ".[dev]"
```

## Execução

### Desenvolvimento com reload

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

Documentação interativa disponível em <http://localhost:8001/docs>.

### Docker

```bash
docker-compose up --build
```

## Testes

```bash
pytest
```

## Estrutura do Projeto

```
.
+-- app/               # Código principal da aplicação
+-- tests/             # Testes unitários e integração
+-- alembic/           # Migrações de banco de dados
+-- docs/              # Documentação
+-- Dockerfile         # Imagem Docker
+-- docker-compose.yml # Orquestração de containers
+-- pyproject.toml    # Configuração do projeto Python
+-- README.md         # Este arquivo
```

## Variáveis de Ambiente

Crie um arquivo `.env` baseado em `.env.example`:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/gerador_email
API_HOST=0.0.0.0
API_PORT=8000
```

## CI/CD

Workflows automáticos configurados em `.github/workflows/`:

- **ci.yml**: Testes, linting e build automático em cada push

## Contribuindo

1. Criar branch para feature: `git checkout -b feature/sua-feature`
2. Commit com mensagens claras: `git commit -am 'Add nova feature'`
3. Push para branch: `git push origin feature/sua-feature`
4. Abrir Pull Request

## Licença

Propriedade intelectual - BT Blue (2026)
