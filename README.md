# ICC-Site

Site oficial da **Liga Insper Consulting Club**, desenvolvido com React (frontend) e Django (backend).

O site do Liga ICC foi feito com o objetivo de apresentar o site da Liga ICC de maneira profissional e moderna, além de seus membros, projetos e parceiros para pessoas e empresas interessadas no trabalho do ICC.

As funcionalidades previstas para o projeto são:
 - Página de inicio qu apresenta a Liga ICC e seus ideais, resumo de sua história e empresas parceiras.
 - Área de membros com todos os membros registrados da organização estudantil, incluindo seus cargos e perfis proficionais, além de seu histórico dentro da Liga ICC.
 - Área de projetos com todos os projetos registrados da organização estudantil, incluindo membros participantes e informações adicionis.
 - Área admnistrativa que permite a alteração de perfis de membros e projetos já existentes, adição de novos projetos e perfis, e exclusão visando o uso futuro do site pela Liga ICC.

Membros 2026.2:

Coordenador:
  - Matteo Rosso

Devs:
  - Cynthia Naoko
  - Sophia Kalil
  - Luan Ferreira
---

## Estrutura do Projeto

```
ICC-Site/
├── ICC-frontend/   # React + TypeScript + Vite
└── ICC-backend/    # Django + Django REST Framework
```

---

## Pré-requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

__Depois de baixar o Docker Desktop, os comandos do Docker devem ser realizados <br> na pasta raiz do repositório COM O DOCKER DESKTOP ABERTO__

---

## Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/R4f43lVB/ICC-Site.git
cd ICC-Site
```

---

### 2. Subir os containers

```bash
docker-compose up --build
```

Isso irá subir três serviços:
- **db** — banco de dados PostgreSQL (porta `5432`)
- **backend** — Django (porta `8000`), já roda as migrations automaticamente
- **frontend** — React + Vite (porta `5173`)

---

### 3. Criar as migrations do backend (primeira vez)

```bash
docker-compose exec backend python manage.py makemigrations website
docker-compose exec backend python manage.py migrate
```

---

### 4. Criar um superusuário para acessar o Admin

```bash
docker-compose exec backend python manage.py createsuperuser
```

---

## Acessos

| Serviço | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| Backend (API) | http://localhost:8000/api |
| Django Admin | http://localhost:8000/admin |

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

Com os containers rodando, acesse `http://localhost:8000/admin` e faça login com o superusuário criado. Por lá é possível cadastrar membros, parceiros, projetos e estatísticas.

---

## Comandos úteis

```bash
# Parar os containers
docker-compose down

# Ver logs do backend
docker-compose logs backend

# Rodar qualquer comando Django
docker-compose exec backend python manage.py <comando>

# Para popular o site local com dados mock completos
docker compose exec backend python manage.py seed_mock_data

# Para importar apenas o mock legado de membros
docker compose exec backend python manage.py import_members

```

---
