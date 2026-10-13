# ICC-Site

Site oficial da **Liga Insper Consulting Club**, desenvolvido com React (frontend) e Django (backend).

O site do Liga ICC foi feito com o objetivo de apresentar o site da Liga ICC de maneira profissional e moderna, além de seus membros, projetos e parceiros para pessoas e empresas interessadas no trabalho do ICC.

As funcionalidades previstas para o projeto são:
 - Página de início que apresenta a Liga ICC e seus ideais, resumo de sua história e empresas parceiras.
 - Área de membros com todos os membros registrados da organização estudantil, incluindo seus cargos e perfis profissionais, além de seu histórico dentro da Liga ICC.
 - Área de projetos com todos os projetos registrados da organização estudantil, incluindo membros participantes e informações adicionais.
 - Área administrativa que permite a alteração de perfis de membros e projetos já existentes, adição de novos projetos e perfis, e exclusão visando o uso futuro do site pela Liga ICC.

> **Status:** a área administrativa funciona hoje pelo Django Admin (`/admin`); o painel próprio no frontend ainda está no backlog. O que já foi entregue, com critérios de aceite, e o que falta estão em [`backlog.md`](backlog.md).

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
git clone https://github.com/InsperCodeJr/icc-site.git
cd icc-site
```

---

### 2. Criar o arquivo de variáveis de ambiente do backend

```bash
echo "SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_urlsafe(50))')" > ICC-backend/.env
```

As demais variáveis são opcionais no ambiente local. A lista completa, com explicação de cada uma, está em [`ICC-backend/.env.example`](ICC-backend/.env.example).

---

### 3. Subir os containers

```bash
docker-compose up --build
```

Isso irá subir três serviços:
- **db** — banco de dados PostgreSQL (porta `5432`)
- **backend** — Django (porta `8000`), já roda as migrations automaticamente
- **frontend** — React + Vite (porta `5173`)

---

### 4. Popular o banco com dados de exemplo (opcional)

```bash
docker-compose exec backend python manage.py seed_mock_data
```

Cria membros, projetos, parceiros e notícias **fictícios**, só para desenvolvimento. Pode ser rodado mais de uma vez sem duplicar nada (mas desfaz edições feitas nesses registros de exemplo). Nunca rode em produção.

> As migrations já estão versionadas em `ICC-backend/website/migrations/` e são aplicadas automaticamente ao subir o backend. Só rode `makemigrations` quando alterar `models.py`, e faça commit do arquivo gerado.

---

### 5. Criar um superusuário para acessar o Admin

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
| GET | `/api/members/` | Lista membros ativos (`?all=true` inclui quem já saiu) |
| GET | `/api/members/<id>/` | Detalhe de um membro |
| GET | `/api/directorates/` | Lista diretorias |
| GET | `/api/partners/` | Lista parceiros |
| GET | `/api/partners/<id>/` | Detalhe de um parceiro |
| GET | `/api/projects/` | Lista projetos |
| GET | `/api/projects/<id>/` | Detalhe de um projeto |
| GET | `/api/categories/` | Lista categorias de atividades |
| GET | `/api/activities/` | Lista atividades |
| GET | `/api/activities/<id>/` | Detalhe de uma atividade |
| GET | `/api/calendar/` | Calendário do semestre |
| GET | `/api/success-cases/` | Lista cases de sucesso |
| GET | `/api/news/` | Lista notícias |
| GET | `/api/statistics/` | Estatísticas da home |
| GET | `/api/selection-process/` | Processo seletivo ativo (etapas, requisitos e materiais) |
| POST | `/api/contact/` | Envia o formulário de contato (JSON, com limite de requisições) |

---

## Cadastro de dados

Com os containers rodando, acesse `http://localhost:8000/admin` e faça login com o superusuário criado. Por lá é possível cadastrar membros, parceiros, projetos e estatísticas.

### Importar os dados reais do ICC

Os dados reais (membros, diretorias, programas, cases e parceiros) ficam em `site-data/`, na raiz do repositório. A pasta **não é versionada**, porque tem dados pessoais dos membros: peça-a a alguém do time. Estrutura esperada:

```
site-data/
├── icc.json      # dados institucionais
├── members/      # fotos, com o id da pessoa no icc.json (ex.: ana-luisa-farinha.jpg)
└── partners/     # logos (ex.: bain.png casa com "Bain & Company")
```

```bash
# Banco local
docker compose exec backend python manage.py import_icc_data

# Banco de produção: passe também as variáveis do Cloudinary, senão o comando se recusa a rodar
docker compose run --rm -e DATABASE_URL='...' -e CLOUDINARY_CLOUD_NAME='...' -e CLOUDINARY_API_KEY='...' -e CLOUDINARY_API_SECRET='...' backend python manage.py import_icc_data
```

O comando pode ser rodado mais de uma vez: atualiza os registros em vez de duplicar (membros são identificados pelo LinkedIn). Quem sai de todas as diretorias no `icc.json` recebe data de saída e some da Equipe, sem ser apagado. Fotos já cadastradas só são substituídas com `--atualizar-fotos`.

> Nunca coloque a `DATABASE_URL` de produção no `ICC-backend/.env`: com ela lá, o ambiente local inteiro passa a ler e gravar no banco do site no ar.

---

## Comandos úteis

```bash
# Parar os containers
docker-compose down

# Ver logs do backend
docker-compose logs backend

# Importar eventos de um .ics (Google Calendar) para o calendário do semestre
docker-compose exec backend python manage.py import_calendar_ics --help

# Rodar qualquer comando Django
docker-compose exec backend python manage.py <comando>

# Para popular o site local com dados mock completos
docker compose exec backend python manage.py seed_mock_data

```

> **Comandos legados:** `import_members` e `download_photos` dependem do arquivo `membros_icc.sql` da gestão anterior, que não está no repositório. Não funcionam e não são mais executados ao subir o backend.

---

## Produção

O `Dockerfile` do backend já sobe em modo de produção: aplica as migrations, prepara os arquivos estáticos do `/admin` (servidos pelo WhiteNoise) e inicia o servidor com o gunicorn na porta definida pela variável `PORT`. O `docker-compose.yml` substitui esse comando pelo servidor de desenvolvimento.

Variáveis obrigatórias na hospedagem do backend (detalhes em [`ICC-backend/.env.example`](ICC-backend/.env.example)):

| Variável | Para quê |
|----------|----------|
| `SECRET_KEY` | Chave secreta do Django |
| `DATABASE_URL` | Conexão com o Postgres na nuvem |
| `ALLOWED_HOSTS` | Domínio do backend |
| `CORS_ALLOWED_ORIGINS` | Domínio do site (frontend) |
| `CSRF_TRUSTED_ORIGINS` | Domínio do backend com `https://`, para o login do `/admin` |
| `BEHIND_PROXY=True` | Quando a hospedagem fornece o HTTPS (Render, Railway...) |
| `CLOUDINARY_*` | Armazenamento das fotos; sem isso, as imagens se perdem a cada deploy |

O frontend é gerado com `npm run build` (pasta `ICC-frontend/dist`), com a variável `VITE_API_URL` apontando para `https://<domínio-do-backend>/api`.

---
