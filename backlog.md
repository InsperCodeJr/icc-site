
# Backlog de tarefas do time

> Atualizado em 27/10/2026 — entrega final (29/10/2026).
> Legenda: ✅ concluído · 🟡 em andamento · ⬜ não iniciado · ➖ fora do escopo desta entrega
> O registro de feedback do cliente e das alterações feitas a partir dele é mantido fora do repositório. O resumo das mudanças está em [`docs/DECISOES.md`](docs/DECISOES.md).

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
| 10 | Transferir contas e automatizar o deploy | Infra | ⬜ |
| 11 | Domínio próprio | Infra | ⬜ |
| 12 | Backend sempre acordado (health check e monitor de uptime) | Back e Infra | ✅ |

---

## Funcionalidades concluídas e critérios de aceite

### A. ✅ [Front] Site público

**Escopo:** páginas Home (com carrossel de parceiros), Equipe (com perfil de membro), Projetos (programas e cases), Parceiros (com perfil), Artigos, Processo Seletivo, Contato, Política de Privacidade e página 404. Carregamento sob demanda das rotas e tela de carga inicial.

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
- [x] Itens com "Exibir no site" desmarcado não aparecem.

### C. ✅ [Back] Gestão de conteúdo pelo Django Admin

**Escopo:** cadastro, edição e exclusão, em `/admin`, de membros (com diretorias e cargos), cargos, diretorias, parceiros e categorias, programas, projetos, cases de sucesso, artigos, estatísticas e processo seletivo (datas, etapas, requisitos, materiais e inscrições). Admin em português, com busca, filtros e miniaturas. Guia de uso em [`docs/GUIA_ADMIN.md`](docs/GUIA_ADMIN.md).

**Critérios de aceite:**
- [x] Superusuário consegue criar, ver, editar e excluir todos os conteúdos acima.
- [x] Alterações feitas no admin aparecem na API pública e no site.
- [x] Membros podem ser arquivados e reativados (data de saída), preservando o histórico.
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

**Escopo:** remoção da página de Atividades; menu reordenado (Parceiros ao lado de Equipe); formulário de contato removido; controle manual de inscrições do PS; carrossel de parceiros na Home (com logos recortados); Notícias transformada em Artigos de autoria dos membros, com página própria (autores, temas, resumo, texto, "Como citar" e compartilhar); link do GitHub do ICC nos canais oficiais. Detalhes em [`docs/DECISOES.md`](docs/DECISOES.md#6-mudanças-a-partir-do-feedback-do-cliente).

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

- README com setup local, API, dados, produção (serviços, deploy, monitor e domínio), passagem de gestão e manutenção (rotina, backup, dependências e problemas comuns).
- [`docs/GUIA_ADMIN.md`](docs/GUIA_ADMIN.md): guia de conteúdo para o ICC.
- [`docs/DECISOES.md`](docs/DECISOES.md): decisões técnicas e justificativas.
- [`docs/DEPENDENCIAS.md`](docs/DEPENDENCIAS.md): dependências, licenças e serviços externos.
- [`ICC-frontend/README.md`](ICC-frontend/README.md): estrutura, rotas, design tokens e componentes.

### 8. ✅ [Infra] Deploy em hospedagem

**Critérios de aceite:**
- [x] Site público acessível por URL com HTTPS (https://icc-site.onrender.com).
- [x] `/admin` acessível e login funcionando em produção.
- [x] Imagens enviadas persistem após um novo deploy (Cloudinary).
- [x] Banco persistente na nuvem (Neon), sem expirar por inatividade.

### 12. ✅ [Back e Infra] Backend sempre acordado

- `GET /api/health/` responde sem consultar o banco.
- Monitor no UptimeRobot a cada 5 minutos, abaixo dos 15 minutos que o Render espera para desligar o backend.
- Pendente na tarefa 10: o monitor está numa conta pessoal e precisa ser recriado numa conta da entidade.

---

## Fora do escopo desta entrega

### 2 e 4. ➖ Painel administrativo próprio e APIs administrativas

O case pede uma área administrativa autenticada com CRUD, e o Django Admin atende a isso com segurança e manutenção prontas (justificativa em [`docs/DECISOES.md`](docs/DECISOES.md#2-django-admin-como-área-administrativa-em-vez-de-um-painel-próprio)). Um painel próprio no frontend continua possível no futuro e exigiria APIs de escrita com autenticação.

---

## Pendentes (próximas gestões)

### 5. 🟡 [Front] Remover CSS duplicado/sobrescrito

- [ ] Auditar classes duplicadas ou sobrescritas e remover CSS morto (incluindo o das páginas sem rota).
- [ ] Padronizar botões, cards, estados vazios e headers internos com os tokens de `index.css`.
- [ ] Layout continua responsivo; `npm run lint` e `npm run build` passam.

### 7. ⬜ [Back e Front] Testes automatizados

`website/tests.py` está vazio.
- [ ] Testes dos endpoints públicos (listagem, detalhe, filtro de membros ativos, itens ocultos).
- [ ] Teste do processo seletivo com mais de um processo ativo e da validação de inscrições sem link.
- [ ] `python manage.py test` roda e passa.

### 9. ⬜ [Infra] Limpeza do repositório

- [ ] Apagar `pages/Atividades`, `CategoriaAtividade`, `PerfilAtividade` e `PerfilAtividadeItem` (sem rota).
- [ ] Decidir se o calendário (`/api/calendar/`, `import_calendar_ics`) e o formulário de contato (`FormContato`, `POST /api/contact/`, model `Contact`, SendGrid) saem do backend.
- [ ] Remover as imagens e prints de teste em `ICC-backend/images/` e o arquivo solto `ICC-frontend/import json.py`.

### 10. ⬜ [Infra] Transferir contas e automatizar o deploy

- [ ] Mover Render, Neon e Cloudinary para contas da Code Jr ou do ICC e entregar as credenciais à entidade (passo a passo em "Se você herdou o site", no README).
- [ ] Manter o backend num workspace do Render sem outros web services gratuitos (limite de 750 horas por mês).
- [ ] Recriar o monitor de uptime numa conta do ICC e apagar o da conta pessoal.
- [ ] Trocar senhas e chaves conhecidas pela gestão anterior.
- [ ] Liberar o app do Render na organização `InsperCodeJr` e reconectar os serviços pelo GitHub, para o deploy voltar a ser automático.

### 11. ⬜ [Infra] Domínio próprio

- [ ] Subdomínio do Insper ou `.com.br` em nome do ICC, configurado no Render (passo a passo no README).
