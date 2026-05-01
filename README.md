# ICC-Site

Site oficial do **Insper Consulting Club**, desenvolvido com React (frontend) e Django (backend).

---

## Estrutura do Projeto

```
ICC-Site/
├── ICC-frontend/   # React + TypeScript + Vite
└── ICC-backend/    # Django + Django REST Framework
```

---

## Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- [Node.js LTS](https://nodejs.org/)
- [Git](https://git-scm.com/download/win)

---

## Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/R4f43lVB/ICC-Site.git
cd ICC-Site
```

---

### 2. Rodar o Backend (Django)

```bash
cd ICC-backend
```

Crie e ative o ambiente virtual:

```bash
# Windows
python -m venv .venv
.venv\Scripts\Activate.ps1

# Mac/Linux
python -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
pip install djangorestframework django-cors-headers
```

Rode as migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Crie um superusuário para acessar o Admin:

```bash
python manage.py createsuperuser
```

Inicie o servidor:

```bash
python manage.py runserver
---

### 3. Rodar o Frontend (React)

Em um **novo terminal**:

```bash
cd ICC-frontend
npm install
npm run dev
```

O frontend estará disponível em `http://localhost:5173`.

---

## Endpoints da API

| Método | URL | Descrição |
|--------|-----|-----------|
| GET | `/api/members/` | Lista membros ativos |
| GET | `/api/members/<id>/` | Detalhe de um membro |
| GET | `/api/partners/` | Lista parceiros |
| GET | `/api/partners/<id>/` | Detalhe de um parceiro |
| GET | `/api/projects/` | Lista projetos |
| GET | `/api/projects/<id>/` | Detalhe de um projeto |
| GET | `/api/statistics/` | Estatísticas da home |

---

## Cadastro de dados

Com o backend rodando, acesse `http://127.0.0.1:8000/admin` e faça login com o superusuário criado. Por lá é possível cadastrar membros, parceiros, projetos e estatísticas.

---

## Observações

- O backend e o frontend precisam estar rodando **simultaneamente** em terminais separados.
