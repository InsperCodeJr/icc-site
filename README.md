# ICC-Site

Site oficial da **Liga Insper Consulting Club**, desenvolvido com React (frontend) e Django (backend).

O site apresenta o ICC de maneira profissional e moderna para alunos e empresas: quem são os membros, os programas e cases, os parceiros, os artigos e o processo seletivo. Todo o conteúdo é mantido pelo próprio ICC na área administrativa, sem mexer no código.

| | Endereço |
|---|---|
| Site | https://icc-site.onrender.com |
| Área administrativa | https://icc-backend-4b38.onrender.com/admin/ (também pelo link "Área administrativa" no rodapé do site) |
| API | https://icc-backend-4b38.onrender.com/api/ |

## O problema

O ICC não tinha um site que pudesse usar. A versão feita no semestre anterior foi abandonada porque o banco de dados ficava num arquivo SQL na máquina de um desenvolvedor: a entidade não tinha acesso aos dados, não conseguia atualizar nada sozinha e o site nunca foi ao ar.

Este projeto resolve isso com:
- um site público e responsivo, com a identidade visual do ICC;
- uma área administrativa com login, em que o próprio ICC cadastra e edita membros, cargos, projetos, parceiros, artigos e o processo seletivo;
- banco de dados e imagens na nuvem, em contas que podem ser transferidas para a entidade;
- documentação para quem usa o admin e para quem assumir a manutenção.

## Stack

| Parte | Tecnologias |
|---|---|
| Frontend | React 19, TypeScript, Vite 8, React Router 7, CSS próprio com design tokens |
| Backend | Python, Django 6, Django REST Framework, Django Admin, gunicorn, WhiteNoise |
| Banco | PostgreSQL (Neon em produção; container do Docker localmente) |
| Imagens | Cloudinary |
| Hospedagem | Render: web service com Docker (backend) e site estático (frontend), deploy automático a cada merge na `main` |
| Monitoramento | UptimeRobot chamando `/api/health/` |
| Ambiente local | Docker Compose (Postgres, backend e frontend) |

As versões exatas estão em [`ICC-backend/requirements.txt`](ICC-backend/requirements.txt) e [`ICC-frontend/package.json`](ICC-frontend/package.json); as licenças, em [`docs/DEPENDENCIAS.md`](docs/DEPENDENCIAS.md).

## Status (29/10/2026)

**No ar e em uso.** Pronto para a entrega final do case 2026.2.

| | Situação |
|---|---|
| Site público | ✅ No ar, com os dados reais do ICC (16 membros, 15 parceiros, 4 programas, 4 cases, 4 projetos e os números da Home) e aprovado pelo ICC |
| Área administrativa | ✅ No ar, com login; CRUD de membros, cargos, projetos e demais conteúdos |
| Banco e imagens na nuvem | ✅ Neon e Cloudinary |
| Deploy | ✅ Automático a cada merge na `main` |
| Pendente | Transferir as contas para a entidade, pedido ao GitHub Support para apagar as cópias do histórico antigo, testes automatizados, domínio próprio |

O que está pronto, com critérios de aceite e evidências, e o que ficou para depois está em [`backlog.md`](backlog.md). As conversas com o ICC e o que mudou a partir delas estão em [`docs/FEEDBACK_CLIENTE.md`](docs/FEEDBACK_CLIENTE.md).

> **Herdou o site?** Comece por [Se você herdou o site](#se-você-herdou-o-site) e pela [Manutenção](#manutenção), no fim deste arquivo.

**Documentação**

| Documento | Para quem | Conteúdo |
|---|---|---|
| [Guia da área administrativa](docs/GUIA_ADMIN.md) | ICC | Como cadastrar membros, parceiros, cases, artigos e o processo seletivo, e a rotina de cada semestre |
| Este README | Devs | Rodar localmente, API, dados, produção, passagem de gestão e manutenção |
| [Decisões técnicas](docs/DECISOES.md) | Devs e avaliação | Por que refatorar, por que o Django Admin, por que esses serviços |
| [Feedback do cliente](docs/FEEDBACK_CLIENTE.md) | Time e avaliação | Reuniões com o ICC: o que foi apresentado, aprovado e pedido, e o que mudou |
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
| GET | `/api/projects/` | Lista projetos ativos (arquivados não aparecem) |
| GET | `/api/projects/<id>/` | Detalhe de um projeto ativo; 404 se estiver arquivado |
| GET | `/api/categories/` | Lista programas (categorias) visíveis |
| GET | `/api/activities/` | Lista atividades |
| GET | `/api/activities/<id>/` | Detalhe de uma atividade |
| GET | `/api/calendar/` | Calendário do semestre |
| GET | `/api/success-cases/` | Lista cases de sucesso visíveis |
| GET | `/api/news/` | Lista os artigos publicados (título, autores, temas, resumo, texto em Markdown, imagens do texto, link externo, data), do mais recente para o mais antigo; rascunhos não aparecem |
| GET | `/api/news/<id>/` | Detalhe de um artigo publicado (usado pela página `/artigos/<id>`); rascunho responde 404 |
| GET | `/api/statistics/` | Estatísticas da home |
| GET | `/api/selection-process/` | Processo seletivo ativo (etapas, requisitos, materiais e se as inscrições estão abertas); 404 se não houver |
| GET | `/api/health/` | Responde `{"status": "ok"}` sem consultar o banco. Usado pelo [monitor de uptime](#monitor-de-uptime) |
| POST | `/api/contact/` | Grava um contato (JSON, com limite de requisições). O site não usa mais; ver [`backlog.md`](backlog.md) |

> As URLs usam `news` por compatibilidade com a versão anterior; no site e no admin, o nome é **Artigos**.

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
| [UptimeRobot](https://uptimerobot.com) | Chama `/api/health/` a cada 5 minutos para o backend não "dormir" e avisa por e-mail se o site cair | Gratuito |
| GitHub — organização `InsperCodeJr` | Código-fonte | Gratuito |

> **Donos das contas:** hoje Render, Neon, Cloudinary e UptimeRobot estão em contas pessoais de membros do time de desenvolvimento. Essas contas precisam ir para uma conta da Code Jr ou do ICC, e as credenciais precisam ser entregues à entidade (o case exige contas transferíveis). O passo a passo está em [Se você herdou o site](#se-você-herdou-o-site).
>
> **Nenhuma credencial fica neste repositório:** senhas, chaves e a `DATABASE_URL` ficam só no painel de cada serviço (no Render, em *Environment* do serviço) e com os responsáveis pela entidade. Se encontrar alguma no código ou num commit, troque-a no serviço imediatamente; apagar o arquivo não basta, porque o histórico do Git guarda tudo.

Limitações do plano gratuito, que não afetam os dados:
- **Horas do Render:** cada *workspace* tem 750 horas grátis de web service por mês, somando todos os serviços dele. Um backend sempre ligado gasta até 744 horas, então ele precisa ficar num workspace **sem outro web service gratuito**. O frontend é um site estático e não gasta essas horas.
- **Backend dormindo:** sem acessos por 15 minutos, o Render desliga o backend, e o próximo acesso leva cerca de 30 segundos. O [monitor de uptime](#monitor-de-uptime) evita isso. Se o monitor parar, o site continua funcionando, só fica lento no primeiro acesso.
- **Banco:** o Neon suspende o banco quando ele fica ocioso e o acorda sozinho no primeiro acesso, em menos de um segundo. Os dados não se perdem. O `/api/health/` não consulta o banco justamente para não mantê-lo acordado à toa.
- **Imagens:** o plano gratuito do Cloudinary tem limite mensal de uso, mais do que suficiente para fotos de membros e logos. O consumo aparece no painel do Cloudinary.

### Como publicar uma mudança (deploy)

O deploy é **automático**: os dois serviços do Render estão conectados ao repositório pelo GitHub, com o Auto-Deploy "On Commit" ligado. Cada merge na `main` publica o backend e o frontend sozinho, em poucos minutos.

Para acompanhar, abra o serviço no Render e veja a aba **Events**: o deploy aparece com o commit do merge e termina como **Live**. Se falhar, os **Logs** do deploy mostram o erro, e o site continua na versão anterior até um deploy dar certo.

O backend aplica as migrations sozinho a cada deploy (está no `CMD` do Dockerfile), então não é preciso rodar nada à mão em produção.

Para publicar de novo sem um commit novo (por exemplo, depois de mudar uma variável de ambiente), use **Manual Deploy → Deploy latest commit** no serviço.

Configuração do serviço do frontend (`icc-site`), caso precise ser recriado:

| Campo | Valor |
|---|---|
| Root Directory | `ICC-frontend` |
| Build Command | `npm run build` |
| Publish Directory | `dist` (relativo ao Root Directory) |
| Variável | `VITE_API_URL=https://icc-backend-4b38.onrender.com/api` |
| Redirects/Rewrites | `/*` → `/index.html` (Rewrite) |

Se a conexão com o GitHub se perder (por exemplo, ao transferir o repositório ou a conta), o Render para de publicar sozinho. Para reconectar: em **Settings → Build & Deploy → Repository**, escolha o repositório pela conta do GitHub com acesso à organização `InsperCodeJr` e confira se o Auto-Deploy está em "On Commit".

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

O `VITE_API_URL` entra no código no momento do build. Se ele mudar, o frontend precisa de um novo deploy. O link "Área administrativa" do rodapé é montado a partir dele (troca o `/api` do fim por `/admin/`), então também acompanha a mudança.

### Monitor de uptime

Um monitor HTTP(s) no UptimeRobot chama `https://icc-backend-4b38.onrender.com/api/health/` a cada 5 minutos. Como o Render só desliga o backend depois de 15 minutos sem acesso, ele nunca chega a dormir. O monitor também manda um e-mail se o backend parar de responder.

Para recriar o monitor (por exemplo, numa conta nova do ICC): **+ New Monitor → HTTP(s)**, a URL acima, intervalo de 5 minutos e o e-mail do ICC como contato de alerta. Qualquer serviço que faça uma requisição periódica serve (o cron-job.org é uma alternativa). Não use o agendamento do GitHub Actions: ele atrasa e é desligado depois de 60 dias sem commits.

Para conferir se está funcionando: o monitor aparece verde no UptimeRobot, e os Logs do backend no Render mostram `GET /api/health/` se repetindo.

### Domínio próprio (próximo passo)

O site usa os endereços gratuitos do Render (`*.onrender.com`). O Render aceita domínio próprio nos planos gratuitos, com HTTPS automático. O que costuma ter custo é o domínio em si. Caminhos sugeridos, sempre com o domínio em nome do ICC:
- pedir um subdomínio à TI do Insper (ex.: `icc.insper.edu.br`), sem custo;
- ou registrar um `.com.br` no registro.br.

Para configurar:
1. No Render, no serviço do frontend: **Settings → Custom Domains → Add**. O Render mostra o registro DNS a criar.
2. No painel do domínio, criar esse registro (`CNAME` para subdomínio, `A`/`ALIAS` para domínio raiz).
3. Atualizar as variáveis do backend (`CORS_ALLOWED_ORIGINS` com o domínio novo do site; se a API também ganhar domínio, `ALLOWED_HOSTS` e `CSRF_TRUSTED_ORIGINS`) e, nesse caso, o `VITE_API_URL` do frontend, seguido de novo deploy.

---

## Se você herdou o site

Esta seção é para quem assume o site numa nova gestão, do ICC ou da Code Jr.

### 1. Receba os acessos

Peça à gestão anterior acesso a cada item abaixo. Se ela não estiver mais disponível, procure a diretoria do ICC ou da Code Jr, que deve ter recebido as credenciais na entrega.

| Acesso | Para quê | Como passar para a nova gestão |
|---|---|---|
| GitHub (repositório `InsperCodeJr/icc-site`) | Mudar o código | Um admin da organização adiciona a pessoa |
| Render (`icc-backend` e `icc-site`) | Publicar mudanças, ver logs e variáveis | Convidar para o workspace (*Workspace Settings → Members*) ou transferir o workspace |
| Neon | Banco de dados | Convidar para o projeto ou transferir o projeto para outra conta |
| Cloudinary | Imagens | Convidar como usuário da conta (*Settings → Users*) |
| UptimeRobot | Monitor de uptime | Mais simples recriar o monitor numa conta da entidade (ver [Monitor de uptime](#monitor-de-uptime)) e apagar o antigo |
| Superusuário do `/admin` | Criar logins para o ICC | Ver abaixo |

Guarde todas as credenciais num lugar da entidade (um gerenciador de senhas ou um documento restrito da diretoria). **Nunca** no repositório, no Trello ou em grupos de mensagem.

### 2. Troque o que a gestão anterior conhecia

Quando quem saiu tinha acesso a senhas e chaves, troque-as:
1. **Logins do admin:** no `/admin`, em *Usuários*, desative ou apague os usuários de quem saiu e crie os novos. Cada pessoa deve ter o seu login; não compartilhe senha.
2. **Banco (Neon):** gere uma nova senha para o usuário do banco no painel do Neon e atualize a `DATABASE_URL` no serviço `icc-backend` do Render.
3. **Cloudinary:** gere uma nova API secret e atualize `CLOUDINARY_API_SECRET` no Render.
4. **`SECRET_KEY` do Django:** gere uma nova (comando no `.env.example`) e atualize no Render. Isso desloga todo mundo do admin, o que é esperado.
5. **Remova as pessoas que saíram** do workspace do Render, do projeto no Neon, da conta do Cloudinary e da organização no GitHub.

Toda variável alterada no Render só vale depois de um novo deploy do serviço (o Render costuma oferecer isso ao salvar).

### 3. Confira que tudo funciona

- [ ] O site abre e mostra membros, parceiros, artigos e o processo seletivo.
- [ ] O login no `/admin` funciona; uma edição de teste aparece no site depois de recarregar.
- [ ] Uma foto enviada pelo admin continua aparecendo depois de um novo deploy do backend (prova de que o Cloudinary está configurado).
- [ ] O monitor de uptime está verde.
- [ ] Você consegue rodar o projeto localmente seguindo [Como rodar o projeto](#como-rodar-o-projeto).

---

## Manutenção

### Como fazer uma mudança no código

1. Crie uma branch a partir da `main` atualizada (`git checkout main`, `git pull`, `git checkout -b feat/nome-da-mudanca`). Uma branch por assunto.
2. Teste localmente. Antes do PR, rode:
   ```bash
   docker-compose exec backend python manage.py check
   cd ICC-frontend && npm run lint && npm run build
   ```
3. Se mudou `models.py`, rode `makemigrations` e inclua a migration no commit.
4. Abra o PR, peça revisão e faça o merge.
5. O Render publica sozinho (ver [Como publicar uma mudança](#como-publicar-uma-mudança-deploy)). Acompanhe em **Events** até os serviços ficarem **Live**.
6. Confira no site.

### Rotina

| Quando | O quê | Quem |
|---|---|---|
| A cada semestre | Cadastrar o processo seletivo, arquivar quem saiu, cadastrar os novos membros, atualizar estatísticas e cases (ver o [guia do admin](docs/GUIA_ADMIN.md#rotina-de-cada-semestre)) | ICC |
| Todo mês | Olhar o UptimeRobot (algum alerta?) e o uso dos planos gratuitos no Render, no Neon e no Cloudinary | Dev |
| A cada semestre | Fazer um backup do banco (abaixo) | Dev |
| A cada semestre | Atualizar dependências com correções de segurança (abaixo) | Dev |
| Na troca de gestão | [Se você herdou o site](#se-você-herdou-o-site) | Dev |

### Backup do banco

O Neon guarda um histórico curto para restauração no plano gratuito, mas isso não substitui um backup. Para exportar o banco inteiro para um arquivo, com o Docker aberto:

```bash
docker run --rm postgres:17 pg_dump "COLE_AQUI_A_DATABASE_URL" > backup-icc-AAAA-MM-DD.sql
```

- A `DATABASE_URL` está em *Environment* do serviço `icc-backend` no Render, ou no painel do Neon (*Connection string*). O `pg_dump` precisa ser da mesma versão do Postgres do Neon ou mais nova (a versão aparece no painel do Neon; troque o `postgres:17` se for preciso).
- O arquivo tem os dados pessoais dos membros: guarde-o num lugar restrito da entidade e **nunca** faça commit dele.
- As imagens não entram nesse backup; elas ficam no Cloudinary, que tem a própria exportação.

### Atualizar dependências

- **Backend:** `docker-compose exec backend pip list --outdated`. Atualize as versões em `ICC-backend/requirements.txt`, rode `docker-compose up --build` e teste o site e o admin. Priorize as versões de correção do Django (ex.: `6.0.x`), que trazem correções de segurança.
- **Frontend:** `cd ICC-frontend && npm outdated`, depois `npm update` (dentro da mesma versão principal) e `npm run lint && npm run build`.
- Faça isso numa branch própria e, se adicionar ou trocar um pacote, atualize o [`docs/DEPENDENCIAS.md`](docs/DEPENDENCIAS.md).

### Problemas comuns

| Sintoma | Causa provável | O que fazer |
|---|---|---|
| Mudança com merge não aparece no site | O deploy falhou ou o Render perdeu a conexão com o GitHub | Ver **Events** e os Logs do deploy no Render; se nenhum deploy começou, reconectar o repositório (ver [Como publicar uma mudança](#como-publicar-uma-mudança-deploy)) |
| Deploy do frontend falha com "Publish directory … does not exist" | Build Command vazio ou Publish Directory errado | Build Command `npm run build` e Publish Directory `dist` (o Root Directory já é `ICC-frontend`) |
| Site ou admin demoram ~30 s para abrir | O backend dormiu (monitor parado) | Conferir o UptimeRobot e as horas do workspace no Render |
| Site abre, mas sem membros, parceiros etc. | Backend fora do ar ou bloqueado por CORS | Abrir `/api/health/`; se responder, conferir `CORS_ALLOWED_ORIGINS` no Render. Ver os Logs do backend |
| `column ... does not exist` (local) | Migration nova não aplicada | `docker-compose exec backend python manage.py migrate` |
| `Failed to resolve import "..."` no frontend (local) | Pacote novo no `package.json`; o container guarda o `node_modules` antigo | `docker-compose up --build -V frontend` (o `-V` recria o `node_modules` do container) |
| Erro 403/CSRF ao entrar no `/admin` | Domínio do backend fora de `CSRF_TRUSTED_ORIGINS` | Corrigir a variável no Render e fazer novo deploy |
| Recarregar `/equipe` (ou outra página) dá 404 | Falta a regra de rewrite no serviço do frontend | No Render, em *Redirects/Rewrites* do `icc-site`: `/*` → `/index.html` (Rewrite) |
| Imagens somem depois de um deploy | Variáveis `CLOUDINARY_*` ausentes ou erradas | Conferir no Render e reenviar as imagens |
| Logo pequeno no carrossel | Imagem com muita margem em volta | Reenviar o PNG recortado rente ao logo (ver o [guia do admin](docs/GUIA_ADMIN.md#parceiros)) |
| Backend parou no fim do mês | Acabaram as 750 horas do workspace | Tirar outros web services gratuitos do workspace ou mudar de plano |

Para investigar qualquer erro em produção, o primeiro lugar é **Logs** do serviço `icc-backend` no Render.

---
