# ICC-Site

Site oficial da **Liga Insper Consulting Club**, desenvolvido com React (frontend) e Django (backend).

O site apresenta o ICC de maneira profissional e moderna para alunos e empresas: quem são os membros, os programas e cases, os parceiros, os artigos e o processo seletivo. Todo o conteúdo é mantido pelo próprio ICC na área administrativa, sem mexer no código.

| | Endereço |
|---|---|
| Site | https://icc-site.onrender.com |
| Área administrativa | https://icc-backend-4b38.onrender.com/admin/ |
| API | https://icc-backend-4b38.onrender.com/api/ |

O que está pronto e o que ficou para depois está em [`backlog.md`](backlog.md).

**Documentação**

| Documento | Para quem | Conteúdo |
|---|---|---|
| [Guia da área administrativa](docs/GUIA_ADMIN.md) | ICC | Como cadastrar membros, parceiros, cases, artigos e o processo seletivo |
| Este README | Devs | Rodar localmente, API, dados e produção |
| [Decisões técnicas](docs/DECISOES.md) | Devs e avaliação | Por que refatorar, por que o Django Admin, por que esses serviços |
| [Dependências e licenças](docs/DEPENDENCIAS.md) | Devs | Bibliotecas usadas e licença de cada uma |
| [`ICC-frontend/README.md`](ICC-frontend/README.md) | Devs | Estrutura do frontend, design tokens e componentes |
| [`ICC-backend/.env.example`](ICC-backend/.env.example) | Devs | Todas as variáveis de ambiente, explicadas |

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
├── ICC-backend/    # Django + Django REST Framework
└── docs/           # Guia do admin, decisões técnicas e dependências
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

Cria membros, projetos, parceiros, artigos e um processo seletivo **fictícios**, só para desenvolvimento. Pode ser rodado mais de uma vez sem duplicar nada (mas desfaz edições feitas nesses registros de exemplo). Nunca rode em produção.

> As migrations já estão versionadas em `ICC-backend/website/migrations/` e são aplicadas automaticamente **quando o backend sobe**. Duas consequências:
> - Só rode `makemigrations` quando alterar `models.py`, e faça commit do arquivo gerado.
> - Se você puxar (ou gerar) uma migration nova com os containers já rodando, aplique-a na mão: `docker-compose exec backend python manage.py migrate`. Sem isso, aparecem erros como `column ... does not exist`.

---

### 5. Criar um superusuário para acessar o Admin

```bash
docker-compose exec backend python manage.py createsuperuser
```

---

## Acessos (local)

| Serviço | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| Backend (API) | http://localhost:8000/api |
| Django Admin | http://localhost:8000/admin |

---

## Endpoints da API

Todos são públicos e somente leitura, exceto o `POST /api/contact/`. Itens marcados como ocultos no admin ("Exibir no site" desmarcado) não aparecem.

| Método | URL | Descrição |
|--------|-----|-----------|
| GET | `/api/members/` | Lista membros ativos (quem tem data de saída não aparece) |
| GET | `/api/members/<id>/` | Detalhe de um membro (também de ex-membros, para links antigos) |
| GET | `/api/directorates/` | Lista diretorias |
| GET | `/api/partners/` | Lista parceiros visíveis |
| GET | `/api/partners/<id>/` | Detalhe de um parceiro |
| GET | `/api/projects/` | Lista projetos |
| GET | `/api/projects/<id>/` | Detalhe de um projeto |
| GET | `/api/categories/` | Lista programas (categorias) visíveis |
| GET | `/api/activities/` | Lista atividades |
| GET | `/api/activities/<id>/` | Detalhe de uma atividade |
| GET | `/api/calendar/` | Calendário do semestre |
| GET | `/api/success-cases/` | Lista cases de sucesso visíveis |
| GET | `/api/news/` | Lista artigos (título, autores, resumo, publicação, data e link) |
| GET | `/api/statistics/` | Estatísticas da home |
| GET | `/api/selection-process/` | Processo seletivo ativo (etapas, requisitos, materiais e se as inscrições estão abertas); 404 se não houver |
| POST | `/api/contact/` | Grava um contato (JSON, com limite de requisições). O site não usa mais; ver [`backlog.md`](backlog.md) |

---

## Cadastro de dados

O conteúdo do site (membros, parceiros, programas, cases, artigos, estatísticas e processo seletivo) é cadastrado no `/admin`. O passo a passo, escrito para o ICC, está no [guia da área administrativa](docs/GUIA_ADMIN.md).

Os links das redes sociais (Instagram, LinkedIn, GitHub) e o e-mail não ficam no banco: estão em [`ICC-frontend/src/redes.ts`](ICC-frontend/src/redes.ts), num lugar só.

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

> ⚠️ **Em produção, use com cuidado.** O comando sincroniza **tudo** a partir do `icc.json` (membros, diretorias, programas, cases e parceiros). O que alguém tiver editado direto no admin de produção pode ser sobrescrito, e membros podem ser arquivados. Depois que o site está no ar, o caminho normal para mudar conteúdo é o admin.

> Nunca coloque a `DATABASE_URL` de produção no `ICC-backend/.env`: com ela lá, o ambiente local inteiro passa a ler e gravar no banco do site no ar.

---

## Comandos úteis

```bash
# Parar os containers
docker-compose down

# Ver logs do backend
docker-compose logs backend

# Aplicar migrations novas com os containers já rodando
docker-compose exec backend python manage.py migrate

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

### Serviços

| Serviço | Para quê | Plano |
|---|---|---|
| [Render](https://render.com) — serviço `icc-backend` | Backend Django (API e `/admin`), a partir do `ICC-backend/Dockerfile` | Gratuito |
| [Render](https://render.com) — serviço `icc-site` | Frontend (site estático gerado pelo Vite) | Gratuito |
| [Neon](https://neon.tech) | Banco PostgreSQL | Gratuito |
| [Cloudinary](https://cloudinary.com) | Fotos dos membros, logos dos parceiros e demais imagens enviadas pelo admin | Gratuito |
| GitHub — organização `InsperCodeJr` | Código-fonte | Gratuito |

> **Donos das contas:** hoje Render, Neon e Cloudinary estão na conta pessoal de um membro do time de desenvolvimento. Antes de encerrar o projeto, essas contas precisam ir para uma conta da Code Jr ou do ICC, e as credenciais precisam ser entregues à entidade (o case exige contas transferíveis). As credenciais **não** ficam neste repositório.

Limitações do plano gratuito, que não afetam os dados:
- O backend "dorme" depois de um tempo sem acesso. O primeiro acesso depois disso leva cerca de 30 segundos; os seguintes são rápidos. Antes de uma apresentação, abra o site e o admin uns minutos antes.
- O Neon também suspende o banco quando ele fica ocioso e o acorda sozinho no primeiro acesso. Os dados não se perdem.

### Como publicar uma mudança (deploy)

Os dois serviços do Render foram conectados ao repositório como **"Public Git Repository"**, porque quem fez o deploy não é dono do repositório. Nesse modo, **o Render não publica sozinho a cada merge**. Depois de cada merge na `main`:

1. Entre no Render, abra o serviço que mudou (`icc-backend`, `icc-site` ou os dois).
2. Clique em **Manual Deploy → Deploy latest commit**.
3. Espere o status ficar **Live** e confira o site.

O backend aplica as migrations sozinho a cada deploy (está no `CMD` do Dockerfile), então não é preciso rodar nada à mão em produção.

Para o deploy voltar a ser automático, alguém com acesso de admin à organização `InsperCodeJr` precisa liberar o app do Render no repositório `icc-site` e reconectar os serviços pela conta do GitHub (não pela URL pública). Com isso, o Auto-Deploy "On Commit" passa a funcionar.

### Backend

O `Dockerfile` do backend já sobe em modo de produção: aplica as migrations, prepara os arquivos estáticos do `/admin` (servidos pelo WhiteNoise) e inicia o servidor com o gunicorn na porta definida pela variável `PORT`. O `docker-compose.yml` substitui esse comando pelo servidor de desenvolvimento.

Variáveis obrigatórias no serviço do backend (detalhes em [`ICC-backend/.env.example`](ICC-backend/.env.example)):

| Variável | Para quê |
|----------|----------|
| `SECRET_KEY` | Chave secreta do Django |
| `DATABASE_URL` | Conexão com o Postgres do Neon |
| `ALLOWED_HOSTS` | Domínio do backend (`icc-backend-4b38.onrender.com`) |
| `CORS_ALLOWED_ORIGINS` | Domínio do site, com `https://` |
| `CSRF_TRUSTED_ORIGINS` | Domínio do backend com `https://`, para o login do `/admin` |
| `BEHIND_PROXY=True` | O Render fornece o HTTPS na frente do Django |
| `CLOUDINARY_*` | Armazenamento das imagens; sem isso, as imagens se perdem a cada deploy |

Para criar um superusuário em produção, use o **Shell** do serviço no Render: `python manage.py createsuperuser`.

### Frontend

O frontend é gerado com `npm run build` (pasta `ICC-frontend/dist`), com a variável `VITE_API_URL` apontando para `https://icc-backend-4b38.onrender.com/api`. Como é um site de página única (SPA), o serviço estático precisa de uma regra de rewrite de `/*` para `/index.html`; sem ela, recarregar uma página como `/equipe` dá 404.

### Domínio próprio (próximo passo)

O site usa os endereços gratuitos do Render (`*.onrender.com`). O Render aceita domínio próprio nos planos gratuitos, com HTTPS automático. O que costuma ter custo é o domínio em si. Caminhos sugeridos, sempre com o domínio em nome do ICC:
- pedir um subdomínio à TI do Insper (ex.: `icc.insper.edu.br`), sem custo;
- ou registrar um `.com.br` no registro.br.

Para configurar:
1. No Render, no serviço do frontend: **Settings → Custom Domains → Add**. O Render mostra o registro DNS a criar.
2. No painel do domínio, criar esse registro (`CNAME` para subdomínio, `A`/`ALIAS` para domínio raiz).
3. Atualizar as variáveis do backend (`CORS_ALLOWED_ORIGINS` com o domínio novo do site; se a API também ganhar domínio, `ALLOWED_HOSTS` e `CSRF_TRUSTED_ORIGINS`) e, nesse caso, o `VITE_API_URL` do frontend, seguido de novo deploy.

---
