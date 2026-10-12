
# Backlog de tarefas do time

> Atualizado em 12/10/2026 — Entrega intermediária 2 (marco da metade do projeto).
> Legenda: ✅ concluído · 🟡 em andamento · ⬜ não iniciado
> O registro de feedback do cliente e das alterações feitas a partir dele é mantido fora do repositório.

## Resumo

| # | Tarefa | Área | Status |
|---|--------|------|--------|
| A | Site público (frontend) | Front | ✅ |
| B | API pública de leitura | Back | ✅ |
| C | Gestão de conteúdo pelo Django Admin | Back | ✅ |
| D | Formulário de contato com envio de e-mail | Back e Front | ✅ |
| E | Calendário do semestre (import `.ics`) | Back e Front | ✅ |
| F | Ambiente local com Docker e dados mock | Infra | ✅ |
| G | Preparação do backend para produção | Back e Infra | ✅ |
| 1 | Padronizar importação e manutenção de membros reais | Back | 🟡 |
| 2 | Painel administrativo (frontend) | Back e Front | ⬜ |
| 3 | Atualizar página do PS para 26.2 | Front | 🟡 |
| 4 | Completar APIs administrativas | Back | ⬜ |
| 5 | Remover CSS duplicado/sobrescrito | Front | 🟡 |
| 6 | Atualizar documentação | Docs | 🟡 |
| 7 | Testes automatizados | Back e Front | ⬜ |
| 8 | Deploy efetivo em hospedagem | Infra | ⬜ |
| 9 | Limpeza do repositório | Infra | ⬜ |

---

## Funcionalidades concluídas e critérios de aceite

### A. ✅ [Front] Site público

**Escopo:** páginas Home, Equipe (com perfil de membro), Atividades (com categorias, detalhe e item), Projetos (com detalhe), Parceiros (com perfil), Notícias, Processo Seletivo, Contato, Política de Privacidade e página 404. Carregamento sob demanda das rotas e tela de carga inicial.

**Critérios de aceite:**
- [x] Todas as rotas abrem e consomem dados da API (`VITE_API_URL`).
- [x] Rota inexistente exibe a página 404.
- [x] Títulos de página e metadados definidos por página.
- [x] Subir com `docker-compose up --build` expõe o site em `http://localhost:5173`.

### B. ✅ [Back] API pública de leitura

**Escopo:** endpoints públicos documentados no README (membros, diretorias, parceiros, projetos, categorias, atividades, calendário, cases de sucesso, notícias, estatísticas e processo seletivo).

**Critérios de aceite:**
- [x] Cada endpoint de listagem retorna JSON; os de detalhe retornam um registro por `id`.
- [x] `/api/members/` retorna só membros sem data de saída; `?all=true` inclui quem já saiu.
- [x] Membros ordenados pela ordem da diretoria, depois por cargo e nome.
- [x] `/api/selection-process/` retorna o processo seletivo ativo com etapas, requisitos e materiais.

### C. ✅ [Back] Gestão de conteúdo pelo Django Admin

**Escopo:** cadastro e edição, em `/admin`, de membros (com diretorias e cargos), diretorias, parceiros e categorias, projetos (imagens, linha do tempo e blocos de conteúdo), atividades (imagens e blocos), cases de sucesso, estatísticas, notícias, processo seletivo e contatos recebidos.

**Critérios de aceite:**
- [x] Superusuário criado com `createsuperuser` consegue cadastrar e editar todos os conteúdos acima.
- [x] Alterações feitas no admin aparecem na API pública.
- [x] Busca por nome de membro habilitada (usada no autocomplete de participantes de cases).

> Limitação conhecida: a exclusão no admin é definitiva. O soft delete está previsto nas tarefas 1 e 2.

### D. ✅ [Back e Front] Formulário de contato

**Escopo:** formulário em `/contato`, endpoint `POST /api/contact/` e notificação por e-mail via SendGrid.

**Critérios de aceite:**
- [x] O envio grava o contato no banco, visível no admin.
- [x] O endpoint aceita apenas JSON e tem limite de requisições (throttle).
- [x] Campos preenchidos pelo visitante são escapados antes de entrar no e-mail.
- [x] Sem `SENDGRID_API_KEY` ou `EMAIL_DESTINATARIO`, o contato é salvo e nenhum e-mail é enviado, sem erro para o usuário.

### E. ✅ [Back e Front] Calendário do semestre

**Escopo:** exibição do calendário na página de Atividades e comando `import_calendar_ics` para importar eventos de um `.ics` exportado do Google Calendar.

**Critérios de aceite:**
- [x] Eventos importados aparecem em `/api/calendar/`, agrupados por mês.
- [x] Eventos recorrentes são expandidos dentro do período importado.
- [x] A página de Atividades exibe o calendário e o próximo evento.

### F. ✅ [Infra] Ambiente local com Docker e dados mock

**Escopo:** `docker-compose.yml` com Postgres, backend e frontend, e comando `seed_mock_data`.

**Critérios de aceite:**
- [x] Seguindo o README, um novo dev sobe os três serviços com um comando.
- [x] As migrations são aplicadas automaticamente ao subir o backend.
- [x] `seed_mock_data` pode ser rodado mais de uma vez sem duplicar registros.
- [x] A porta do Postgres só é acessível pela própria máquina (`127.0.0.1`).

### G. ✅ [Back e Infra] Preparação do backend para produção (branch `feat/deploy-producao`)

**Escopo:** `Dockerfile` do backend em modo produção (migrations, `collectstatic` e gunicorn na porta `PORT`), WhiteNoise para estáticos do admin, Cloudinary para imagens, `DATABASE_URL` para Postgres na nuvem, HTTPS/HSTS e cookies seguros fora do modo debug, CORS e CSRF configuráveis, `.env.example` documentado.

**Critérios de aceite:**
- [x] Com `DEBUG=False`, o backend força HTTPS, cookies seguros e HSTS.
- [x] Variáveis obrigatórias estão listadas no README e no `ICC-backend/.env.example`.
- [x] O `docker-compose.yml` continua usando o servidor de desenvolvimento localmente.
- [x] `.env` não é versionado (`.gitignore`).
- [ ] Backend e frontend rodando em hospedagem real (ver tarefa 8).

---

## Tarefas em andamento e pendentes

### 1. 🟡 [Back] Padronizar importação e manutenção de membros reais

**Contexto:** hoje os dados de membros podem ser escritos por `seed_mock_data`, `import_members`, `download_photos` e `membros_icc.sql`.

**Objetivo:** definir um único fluxo recomendado para cadastrar, atualizar e desativar membros reais do ICC em desenvolvimento, homologação e produção.

**Já feito:**
- Membros que saíram ficam preservados no banco (`exit_date`) e somem da listagem pública.
- `seed_mock_data` é idempotente e está documentado como uso exclusivo de desenvolvimento.
- `import_members` e `download_photos` estão marcados como legados no README, pois dependem de um `.sql` que não está no repositório.

**Falta:**
- Definir a fonte oficial dos dados reais (painel admin, planilha validada pelo ICC, CSV versionado ou outro).
- Criar ou ajustar a importação para dados reais, idempotente, com identificador estável (e-mail institucional, LinkedIn ou outro campo único).
- Evitar operações destrutivas sem flag explícita.
- Garantir que `download_photos` só atualize fotos de membros existentes, ou removê-lo.

**Critérios de aceite:**
- [ ] Existe um fluxo documentado para popular o banco com membros reais do ICC.
- [x] `/api/members/` retorna apenas membros ativos.
- [ ] `/api/members/` retorna membros reais após a importação (depende do fluxo acima).
- [ ] `/api/members/<id>/` retorna detalhes completos de um membro real.
- [ ] Rodar a importação mais de uma vez não duplica membros ou cargos.
- [x] Membros inativos não aparecem nas listagens públicas, mas permanecem no banco.
- [x] README explica quando usar mock local.
- [ ] README explica quando usar dados reais.

### 2. ⬜ [Back e Front] Painel administrativo

**Objetivo:** criar uma experiência administrativa própria para manter o conteúdo do site sem depender do Django Admin.

**Situação atual:** a manutenção de conteúdo já é possível pelo Django Admin (item C). Esta tarefa cobre o painel no frontend.

**Escopo:**
- Editar membros: `POST`, `PUT` e soft delete.
- Adicionar/editar projetos: `POST`, `PUT` e soft delete.
- Adicionar/editar notícias: `POST`, `PUT` e soft delete.
- Criar telas/forms no frontend para as operações administrativas.
- Criar ou ajustar endpoints no backend com validação, permissão e respostas consistentes (ver tarefa 4).

**Critérios de aceite:**
- [ ] Admin consegue criar, editar e desativar membros sem remover histórico.
- [ ] Admin consegue criar, editar e desativar projetos.
- [ ] Admin consegue criar, editar e desativar notícias.
- [ ] Soft delete remove itens das listagens públicas, mas preserva registros no banco.
- [ ] Frontend exibe estados de loading, sucesso e erro.

### 3. 🟡 [Front] Editar página do PS de acordo com 26.2

**Objetivo:** atualizar a página de Processo Seletivo (`/processo`) com conteúdo, datas, etapas e comunicação do ciclo 2026.2.

**Já feito:**
- A página é alimentada pela API (`/api/selection-process/`): título, etapas, requisitos e materiais são cadastrados no admin, sem mexer no código.
- CTA "Cadastre-se para receber atualizações" leva ao formulário de contato.

**Falta:**
- Cadastrar no admin o processo 2026.2 com datas, etapas e textos oficiais, substituindo placeholders.
- Revisar o CTA principal conforme o status do processo (aviso ou inscrição).

**Critérios de aceite:**
- [ ] Página `/processo` comunica corretamente o ciclo 2026.2.
- [ ] Datas e etapas estão consistentes com o material oficial.
- [ ] CTAs direcionam para inscrição ou aviso, conforme o status do processo.

### 4. ⬜ [Back] Completar APIs administrativas

**Objetivo:** preparar o backend para suportar o painel administrativo com segurança e consistência.

**Situação atual:** a API só tem rotas de leitura (e o `POST /api/contact/` público). Não há views de criação/edição nem autenticação de API.

**Escopo:**
- Criar serializers e views para criação/edição de membros, projetos e notícias.
- Definir autenticação e permissões para as rotas administrativas.
- Adicionar validações.

**Critérios de aceite:**
- [ ] APIs administrativas permitem listar, criar e editar registros.
- [ ] Operações administrativas exigem autenticação/permissão.
- [ ] Validações retornam erros consistentes.

### 5. 🟡 [Front] Remover CSS duplicado/sobrescrito

**Objetivo:** reduzir dívida técnica visual e evitar conflitos entre estilos globais, CSS legado e Tailwind.

**Escopo:**
- Auditar classes duplicadas ou sobrescritas.
- Consolidar estilos comuns em componentes/tokens.
- Remover CSS morto.
- Padronizar botões, cards, formulários, estados vazios e headers internos.

**Critérios de aceite:**
- [ ] Não há estilos duplicados óbvios para os mesmos componentes.
- [ ] Componentes principais usam tokens e padrões compartilhados.
- [ ] Layout continua responsivo em mobile e desktop.
- [ ] `npm run lint` e `npm run build` passam.

### 6. 🟡 [Docs] Atualizar documentação

**Objetivo:** manter a documentação alinhada com a arquitetura atual do projeto.

**Já feito:**
- README atualizado com setup local, Docker, seed, produção e variáveis de ambiente.
- Tabela de endpoints do README cobre todas as rotas atuais.
- Comandos legados identificados no README.
- `ICC-backend/.env.example` documenta cada variável.

**Falta:**
- Substituir o `ICC-frontend/README.md` (ainda é o texto padrão do template do Vite).
- Documentar o fluxo de conteúdo: membros, projetos, notícias, parceiros e processo seletivo.
- Documentar design tokens e componentes reutilizáveis.
- Documentar endpoints administrativos quando existirem (tarefa 4).

**Critérios de aceite:**
- [x] Um novo dev consegue subir o projeto e popular dados seguindo o README.
- [x] Documentação indica claramente quais comandos são legados.
- [x] Rotas principais da API estão descritas.
- [ ] Fluxo de conteúdo documentado.
- [ ] Frontend com README próprio.

### 7. ⬜ [Back e Front] Testes automatizados

**Objetivo:** dar segurança para evoluir o projeto, hoje sem testes (`website/tests.py` está vazio).

**Escopo:**
- Testes dos endpoints públicos (listagem, detalhe, filtro de membros ativos).
- Testes do formulário de contato (validação, throttle, falha de e-mail não quebra o envio).
- Testes das APIs administrativas após a tarefa 4.

**Critérios de aceite:**
- [ ] `python manage.py test` roda e passa.
- [ ] Endpoints públicos principais cobertos.
- [ ] Endpoint de contato coberto.

### 8. ⬜ [Infra] Deploy efetivo em hospedagem

**Objetivo:** colocar backend, banco e frontend no ar, usando a preparação de produção já feita (item G).

**Escopo:**
- Subir o backend (ex.: Render ou Railway) com as variáveis do `.env.example`.
- Provisionar o Postgres na nuvem e a conta Cloudinary.
- Gerar o frontend com `npm run build`, com `VITE_API_URL` apontando para o backend, e publicá-lo.
- Criar o superusuário de produção e cadastrar o conteúdo real.

**Critérios de aceite:**
- [ ] Site público acessível por URL com HTTPS.
- [ ] `/admin` acessível e login funcionando em produção.
- [ ] Imagens enviadas persistem após um novo deploy.
- [ ] Formulário de contato envia e-mail em produção.

### 9. ⬜ [Infra] Limpeza do repositório

**Objetivo:** remover do versionamento arquivos que não pertencem ao código.

**Escopo:**
- Remover (ou ignorar no `.gitignore`) as imagens e prints em `ICC-backend/images/`.
- Remover ou documentar o arquivo solto `ICC-frontend/import json.py`.

**Critérios de aceite:**
- [ ] Repositório sem prints e uploads de teste versionados.
- [ ] Nenhum script solto sem documentação.
