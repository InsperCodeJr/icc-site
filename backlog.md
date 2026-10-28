
# Backlog de tarefas do time

> Atualizado em 28/10/2026 — entrega final (29/10/2026).
> Legenda: ✅ concluído · 🟡 em andamento · ⬜ não iniciado · ➖ fora do escopo desta entrega
> As conversas com o ICC e o que mudou a partir delas estão em [`docs/FEEDBACK_CLIENTE.md`](docs/FEEDBACK_CLIENTE.md). O planejamento por cartão (responsável, size e sprint) fica no Trello do projeto.

## Resumo

| # | Tarefa | Área | Status |
|---|--------|------|--------|
| A | Site público (frontend) | Front | ✅ |
| B | API pública de leitura | Back | ✅ |
| C | Gestão de conteúdo pelo Django Admin | Back | ✅ |
| D | Formulário de contato com envio de e-mail | Back e Front | ➖ removido do site a pedido do cliente |
| E | Calendário do semestre (import `.ics`) | Back e Front | ➖ saiu do site junto com a página de Atividades |
| F | Ambiente local com Docker e dados mock | Infra | ✅ |
| G | Preparação do backend para produção | Back e Infra | ✅ |
| H | Ajustes do feedback do cliente | Back e Front | ✅ |
| 1 | Padronizar importação e manutenção de membros reais | Back | ✅ |
| 2 | Painel administrativo próprio (frontend) | Back e Front | ➖ substituído pelo Django Admin |
| 3 | Página do PS para 2026.2 | Back e Front | ✅ |
| 4 | APIs administrativas | Back | ➖ não necessárias com o Django Admin |
| 5 | Remover CSS duplicado/sobrescrito | Front | 🟡 |
| 6 | Documentação | Docs | ✅ |
| 7 | Testes automatizados | Back e Front | ⬜ |
| 8 | Deploy em hospedagem | Infra | ✅ |
| 9 | Limpeza do repositório | Infra | ⬜ |
| 10 | Transferir contas para a entidade | Infra | 🟡 deploy automático feito; contas pendentes |
| 11 | Domínio próprio | Infra | ⬜ |
| 12 | Backend sempre acordado (health check e monitor de uptime) | Back e Infra | ✅ |
| 13 | Arquivar projetos (soft delete) | Back | ✅ |
| 14 | Link para a área administrativa no site | Front | ✅ |
| 15 | Remover dados pessoais do histórico do Git | Infra | 🟡 histórico reescrito; falta o pedido ao GitHub Support |

---

## Requisitos do case e evidências

Cada requisito do case 2026.2, onde ele foi atendido e como foi verificado. As verificações em produção foram feitas em 28/10/2026.

| Requisito do case | Onde está | Evidência |
|---|---|---|
| Site institucional responsivo | Tarefa A; [`ICC-frontend/`](ICC-frontend/) | Site no ar em https://icc-site.onrender.com; todas as rotas respondem 200, inclusive ao recarregar uma página interna como `/equipe` (rewrite do SPA) |
| Área administrativa autenticada | Tarefa C; Django Admin em `/admin/` | `/admin/` em produção redireciona para a tela de login (HTTP 302) quando não há sessão; link "Área administrativa" no rodapé (tarefa 14) |
| CRUD de membros com cargos | Tarefa C; `TeamMemberAdmin`, `MemberPositionAdmin` e `DirectorateAdmin` em [`admin.py`](ICC-backend/website/admin.py) | Membros, cargos e diretorias criados, editados e arquivados pelo admin aparecem em `/api/members/` e na página Equipe; 16 membros reais em produção |
| CRUD de projetos | Tarefas C e 13; `ProjectAdmin` | Criar, editar, arquivar e reativar pelo admin; arquivados somem de `/api/projects/`. ⚠️ Nenhum projeto cadastrado em produção ainda (ver pendências) |
| Banco persistente na nuvem | Tarefas G e 8; Neon (`DATABASE_URL`) | Dados reais importados e servidos pela API de produção (16 membros, 15 parceiros, 4 programas, 4 cases, 3 artigos) |
| Imagens persistentes | Tarefa G; Cloudinary | Fotos e logos continuam no ar depois de vários deploys do backend; os 15 logos de produção conferidos com os arquivos recortados |
| Deploy público | Tarefa 8; Render | Backend e frontend no ar com HTTPS; deploy automático a cada merge (PR #20 publicou sozinho) |
| Backend disponível sem espera | Tarefa 12 | `/api/health/` responde 200; monitor do UptimeRobot verde, a cada 5 minutos |
| Documentação | Tarefa 6 | [README](README.md), [guia do admin](docs/GUIA_ADMIN.md), [decisões](docs/DECISOES.md), [dependências](docs/DEPENDENCIAS.md), [feedback do cliente](docs/FEEDBACK_CLIENTE.md) |
| Contas transferíveis | Tarefa 10 | Passo a passo em "Se você herdou o site", no README. ⚠️ Transferência ainda não feita |
| Justificar refatorar × reescrever | [`docs/DECISOES.md`](docs/DECISOES.md#1-refatorar-o-projeto-anterior-em-vez-de-reescrever-do-zero) | Tabela com cada problema do projeto anterior e como foi resolvido |
| Contato com o cliente | [`docs/FEEDBACK_CLIENTE.md`](docs/FEEDBACK_CLIENTE.md) | Pedidos do ICC ligados aos PRs que os atenderam (#10 a #17) |

---

## Funcionalidades concluídas e critérios de aceite

### A. ✅ [Front] Site público

**Escopo:** páginas Home (com carrossel de parceiros), Equipe (com perfil de membro), Projetos (programas e cases), Parceiros (com perfil), Artigos (com página de cada artigo), Processo Seletivo, Contato, Política de Privacidade e página 404. Carregamento sob demanda das rotas e tela de carga inicial.

**Critérios de aceite:**
- [x] Todas as rotas abrem e consomem dados da API (`VITE_API_URL`).
- [x] Rota inexistente exibe a página 404.
- [x] Títulos de página e metadados definidos por página.
- [x] Subir com `docker-compose up --build` expõe o site em `http://localhost:5173`.

### B. ✅ [Back] API pública de leitura

**Escopo:** endpoints públicos documentados no README (membros, diretorias, parceiros, projetos, programas, atividades, calendário, cases de sucesso, artigos com detalhe, estatísticas, processo seletivo e health check).

**Critérios de aceite:**
- [x] Cada endpoint de listagem retorna JSON; os de detalhe retornam um registro por `id`.
- [x] `/api/members/` retorna só membros sem data de saída.
- [x] Membros ordenados pela ordem da diretoria, depois por cargo e nome.
- [x] `/api/selection-process/` retorna o processo seletivo ativo com etapas, requisitos, materiais e o estado das inscrições.
- [x] Itens com "Exibir no site" desmarcado e projetos arquivados não aparecem.

### C. ✅ [Back] Gestão de conteúdo pelo Django Admin

**Escopo:** cadastro, edição e exclusão, em `/admin`, de membros (com diretorias e cargos), cargos, diretorias, parceiros e categorias, programas, projetos, cases de sucesso, artigos, estatísticas e processo seletivo (datas, etapas, requisitos, materiais e inscrições). Admin em português, com busca, filtros e miniaturas. Guia de uso em [`docs/GUIA_ADMIN.md`](docs/GUIA_ADMIN.md).

**Critérios de aceite:**
- [x] Superusuário consegue criar, ver, editar e excluir todos os conteúdos acima.
- [x] Alterações feitas no admin aparecem na API pública e no site.
- [x] Membros e projetos podem ser arquivados e reativados, preservando o histórico.
- [x] Parceiros, programas e cases podem ser escondidos do site sem serem apagados.
- [x] Só um processo seletivo fica ativo por vez; as inscrições abrem e fecham pelo admin, e não abrem sem link.

### D. ➖ [Back e Front] Formulário de contato

Removido do site a pedido do cliente: o ICC já atende pelo e-mail e pelas redes, listados na página de Contato. O endpoint `POST /api/contact/`, o model `Contact` e a integração com o SendGrid continuam no backend, sem uso (ver tarefa 9).

### E. ➖ [Back e Front] Calendário do semestre

O calendário era exibido na página de Atividades, que saiu do site a pedido do cliente. O comando `import_calendar_ics` e o endpoint `/api/calendar/` continuam no backend, sem uso no site (ver tarefa 9).

### F. ✅ [Infra] Ambiente local com Docker e dados mock

**Escopo:** `docker-compose.yml` com Postgres, backend e frontend, e comando `seed_mock_data`.

**Critérios de aceite:**
- [x] Seguindo o README, um novo dev sobe os três serviços com um comando.
- [x] As migrations são aplicadas automaticamente ao subir o backend.
- [x] `seed_mock_data` pode ser rodado mais de uma vez sem duplicar registros.
- [x] A porta do Postgres só é acessível pela própria máquina (`127.0.0.1`).

### G. ✅ [Back e Infra] Preparação do backend para produção

**Escopo:** `Dockerfile` do backend em modo produção (migrations, `collectstatic` e gunicorn na porta `PORT`), WhiteNoise para estáticos do admin, Cloudinary para imagens, `DATABASE_URL` para Postgres na nuvem, HTTPS/HSTS e cookies seguros fora do modo debug, CORS e CSRF configuráveis, `.env.example` documentado.

**Critérios de aceite:**
- [x] Com `DEBUG=False`, o backend força HTTPS, cookies seguros e HSTS.
- [x] Variáveis obrigatórias estão listadas no README e no `ICC-backend/.env.example`.
- [x] O `docker-compose.yml` continua usando o servidor de desenvolvimento localmente.
- [x] `.env` não é versionado (`.gitignore`).
- [x] Backend e frontend rodando em hospedagem real (tarefa 8).

### H. ✅ [Back e Front] Ajustes do feedback do cliente

**Escopo:** remoção da página de Atividades; menu reordenado (Parceiros ao lado de Equipe); formulário de contato removido; controle manual de inscrições do PS; carrossel de parceiros na Home (com logos recortados); Notícias transformada em Artigos de autoria dos membros, com página própria (autores, temas, resumo, texto, "Como citar" e compartilhar); link do GitHub do ICC nos canais oficiais. Cada pedido, com o PR correspondente, está em [`docs/FEEDBACK_CLIENTE.md`](docs/FEEDBACK_CLIENTE.md).

---

## Tarefas concluídas nesta entrega

### 1. ✅ [Back] Importação e manutenção de membros reais

- Dados reais importados do `site-data/` (não versionado) com `import_icc_data`, idempotente e com o LinkedIn como identificador.
- Depois que o site está no ar, a fonte oficial é o **admin de produção**. O `import_icc_data` fica para cargas iniciais, com o alerta, no README, de que ele sobrescreve edições feitas no admin.
- `import_members` e `download_photos` estão marcados como legados.

### 3. ✅ [Back e Front] Página do PS 2026.2

- Processo 2026.2 cadastrado em produção com as datas e o requisito oficiais, com as inscrições fechadas.
- CTA conforme o estado: "Inscreva-se" (link do formulário) ou "Inscrições encerradas" (Instagram).

### 6. ✅ [Docs] Documentação

- README com o problema, a stack, o status, setup local, API, dados, produção (serviços, deploy automático, monitor e domínio), passagem de gestão e manutenção (rotina, backup, dependências e problemas comuns).
- [`docs/GUIA_ADMIN.md`](docs/GUIA_ADMIN.md): guia de conteúdo para o ICC.
- [`docs/DECISOES.md`](docs/DECISOES.md): decisões técnicas e justificativas.
- [`docs/DEPENDENCIAS.md`](docs/DEPENDENCIAS.md): dependências, licenças e serviços externos.
- [`docs/FEEDBACK_CLIENTE.md`](docs/FEEDBACK_CLIENTE.md): conversas com o ICC.
- [`ICC-frontend/README.md`](ICC-frontend/README.md): estrutura, rotas, design tokens e componentes.

### 8. ✅ [Infra] Deploy em hospedagem

**Critérios de aceite:**
- [x] Site público acessível por URL com HTTPS (https://icc-site.onrender.com).
- [x] `/admin` acessível e login funcionando em produção.
- [x] Imagens enviadas persistem após um novo deploy (Cloudinary).
- [x] Banco persistente na nuvem (Neon), sem expirar por inatividade.
- [x] Deploy automático a cada merge na `main`, nos dois serviços.

### 12. ✅ [Back e Infra] Backend sempre acordado

- `GET /api/health/` responde sem consultar o banco.
- Monitor no UptimeRobot a cada 5 minutos, abaixo dos 15 minutos que o Render espera para desligar o backend.
- Pendente na tarefa 10: o monitor está numa conta pessoal e precisa ser recriado numa conta da entidade.

### 13. ✅ [Back] Arquivar projetos (PR #19)

- Campo "Ativo" no projeto, editável na lista, e ações "Arquivar selecionados" e "Reativar selecionados".
- Projetos arquivados somem da API pública (lista, detalhe com 404, perfil dos membros e números dos parceiros).

### 14. ✅ [Front] Link para a área administrativa (PR #20)

- Link "Área administrativa" no rodapé de todas as páginas, ao lado da Política de Privacidade.
- O endereço vem do `VITE_API_URL`, então funciona localmente (`localhost:8000/admin/`) e em produção.

---

## Fora do escopo desta entrega

### 2 e 4. ➖ Painel administrativo próprio e APIs administrativas

O case pede uma área administrativa autenticada com CRUD, e o Django Admin atende a isso com segurança e manutenção prontas (justificativa em [`docs/DECISOES.md`](docs/DECISOES.md#2-django-admin-como-área-administrativa-em-vez-de-um-painel-próprio)). Um painel próprio no frontend continua possível no futuro e exigiria APIs de escrita com autenticação.

---

## Até a entrega final

| Data | O quê | Responsável |
|---|---|---|
| 28/10 | Slides da apresentação | Matteo Rosso |
| 28/10 | Apresentar o MVP no ar ao ICC e registrar em `FEEDBACK_CLIENTE.md` | ⚠️ |
| 28/10 | Cadastrar estatísticas e pelo menos um projeto em produção; testar o CRUD de membros e projetos no admin de produção | ⚠️ |
| 28/10 | Trocar os 3 artigos "[Exemplo]" por um artigo real ou apagá-los; conferir os links do LinkedIn | ⚠️ |
| 29/10 | Alinhar o Trello com este backlog (size, sprint e responsável em cada cartão) | ⚠️ |
| 29/10 | E-mail de entrega (repositório e link de produção) | ⚠️ |
| 30/10 | Demo | Time |

---

## Pendentes (próximas gestões)

### 5. 🟡 [Front] Remover CSS duplicado/sobrescrito

- [ ] Auditar classes duplicadas ou sobrescritas e remover CSS morto (incluindo o das páginas sem rota).
- [ ] Padronizar botões, cards, estados vazios e headers internos com os tokens de `index.css`.
- [ ] Layout continua responsivo; `npm run lint` e `npm run build` passam.

### 7. ⬜ [Back e Front] Testes automatizados

`website/tests.py` está vazio.
- [ ] Testes dos endpoints públicos (listagem, detalhe, filtro de membros ativos, itens ocultos, projetos arquivados).
- [ ] Teste do processo seletivo com mais de um processo ativo e da validação de inscrições sem link.
- [ ] `python manage.py test` roda e passa.

### 9. ⬜ [Infra] Limpeza do repositório

- [ ] Apagar `pages/Atividades`, `CategoriaAtividade`, `PerfilAtividade` e `PerfilAtividadeItem` (sem rota).
- [ ] Decidir se o calendário (`/api/calendar/`, `import_calendar_ics`) e o formulário de contato (`FormContato`, `POST /api/contact/`, model `Contact`, SendGrid) saem do backend.
- [ ] Remover as imagens e prints de teste em `ICC-backend/images/` e o arquivo solto `ICC-frontend/import json.py`.
- [ ] Remover o `has_delete_permission` comentado no `ProjectAdmin`.

### 10. 🟡 [Infra] Transferir contas para a entidade

- [x] Deploy automático: os serviços do Render foram reconectados pelo GitHub.
- [ ] Mover Render, Neon e Cloudinary para contas da Code Jr ou do ICC e entregar as credenciais à entidade (passo a passo em "Se você herdou o site", no README).
- [ ] Manter o backend num workspace do Render sem outros web services gratuitos (limite de 750 horas por mês).
- [ ] Recriar o monitor de uptime numa conta do ICC e apagar o da conta pessoal.
- [ ] Trocar senhas e chaves conhecidas pela gestão anterior.

### 11. ⬜ [Infra] Domínio próprio

- [ ] Subdomínio do Insper ou `.com.br` em nome do ICC, configurado no Render (passo a passo no README).

### 15. 🟡 [Infra] Remover dados pessoais do histórico do Git

Um arquivo `.sql` com dados de membros (nomes, datas de entrada, fotos, cargos e descrições) foi versionado em 22/05/2026 e apagado em 29/05/2026, mas continuava no histórico do repositório, que é público.

**Responsável:** Cynthia Yasutake (execução); pedido ao GitHub Support pelo diretor de Tech da Code Jr, admin da organização `InsperCodeJr`. **Feito em:** 28/10/2026.

- [x] Reescrever o histórico removendo o arquivo (`git filter-repo --invert-paths --path "ICC-backend/membros_icc .sql"`) num clone espelho, e enviar todas as branches com force push (19 branches).
- [x] Conferir com `git log --all -- "ICC-backend/membros_icc .sql"` que não sobrou nada (nenhum commit encontrado).
- [x] Conferir que o deploy disparado pelo force push terminou e o site continua no ar.
- [ ] Avisar o time para apagar o clone local e clonar de novo, sem fazer push de branches antigas.
- [ ] Pedir ao GitHub Support a remoção das cópias guardadas nos PRs antigos: até isso, o commit antigo (`35d2b12`) ainda abre pelo link direto.
