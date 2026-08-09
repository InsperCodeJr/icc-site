
## Backlog de tarefas do time

### 1. [Back] Padronizar importacao e manutencao de membros reais

**Contexto:** hoje os dados de membros podem ser escritos por `seed_mock_data`, `import_members`, `download_photos` e `membros_icc.sql`.

**Objetivo:** definir um unico fluxo recomendado para cadastrar, atualizar e desativar membros reais do ICC em ambiente de desenvolvimento, homologacao e producao.

**Escopo:**
- Definir a fonte oficial dos dados reais de membros: painel administrativo, planilha validada pelo ICC, CSV versionado ou outro fluxo aprovado pelo time.
- Criar ou ajustar o processo de importacao para usar dados reais, nao nomes mock.
- Garantir que a importacao seja idempotente: rodar mais de uma vez nao deve duplicar membros ou cargos.
- Usar um identificador estavel para atualizacao de membros, como e-mail institucional, LinkedIn ou outro campo unico aprovado.
- Evitar operacoes destrutivas sem flag explicita.
- Implementar soft delete ou campo de status para membros que sairam do clube, preservando historico.
- Deixar `seed_mock_data` documentado apenas como fallback local para ambiente sem dados reais.
- Deixar `import_members` marcado como legado ou adapta-lo para o novo fluxo de dados reais.
- Garantir que `download_photos` apenas atualize fotos de membros existentes e nao crie registros novos.

**Criterios de aceite:**
- Existe um fluxo documentado para popular o banco com membros reais do ICC.
- `/api/members/` retorna membros reais ativos apos a importacao.
- `/api/members/<id>/` retorna detalhes completos de um membro real.
- Rodar a importacao mais de uma vez nao duplica membros ou cargos.
- Membros inativos nao aparecem nas listagens publicas, mas permanecem preservados no banco.
- README explica claramente quando usar dados reais e quando usar mock local.
- Dados mock ficam restritos a desenvolvimento local e nao sao tratados como fonte oficial.

### 2. [Back e Front] Painel administrativo

**Objetivo:** criar uma experiencia administrativa para manter conteudo do site sem depender de edicao direta no banco.

**Escopo:**
- Editar membros: `POST`, `PUT` e soft delete.
- Adicionar/editar projetos: `POST`, `PUT` e soft delete.
- Adicionar/editar noticias: `POST`, `PUT` e soft delete.
- Criar telas/forms no frontend para operacoes administrativas.
- Criar ou ajustar endpoints no backend com validacao, permissao e respostas consistentes.

**Criterios de aceite:**
- Admin consegue criar, editar e desativar membros sem remover historico.
- Admin consegue criar, editar e desativar projetos.
- Admin consegue criar, editar e desativar noticias.
- Soft delete remove itens das listagens publicas, mas preserva registros no banco.
- Frontend exibe estados de loading, sucesso e erro.

### 3. [Front] Editar pagina do PS de acordo com 26.2

**Objetivo:** atualizar a pagina de Processo Seletivo com conteudo, datas, etapas e comunicacao do ciclo 2026.2.

**Escopo:**
- Atualizar textos, datas e status do processo.
- Revisar CTA principal e formulario de aviso.
- Garantir que a timeline reflita o processo 26.2.
- Substituir placeholders por conteudo oficial.

**Criterios de aceite:**
- Pagina `/processo-seletivo` comunica corretamente o ciclo 2026.2.
- Datas e etapas estao consistentes com o material oficial.
- CTAs direcionam para inscricao ou aviso, conforme status do processo.

### 4. [Back] Completar APIs administrativas

**Objetivo:** preparar o backend para suportar o painel administrativo com seguranca e consistencia.

**Escopo:**
- Criar serializers e views para criacao/edicao.
- Definir permissoes para rotas administrativas.
- Adicionar validacoes para membros, projetos e noticias.

**Criterios de aceite:**
- APIs administrativas permitem listar registros
- Operacoes administrativas exigem autenticacao/permissao.

### 5. [Front] Remover CSS duplicado/sobrescrito

**Objetivo:** reduzir divida tecnica visual e evitar conflitos entre estilos globais, CSS legado e Tailwind.

**Escopo:**
- Auditar classes duplicadas ou sobrescritas.
- Consolidar estilos comuns em componentes/tokens.
- Remover CSS morto.
- Padronizar botoes, cards, formularios, estados vazios e headers internos.

**Criterios de aceite:**
- Nao ha estilos duplicados obvios para os mesmos componentes.
- Componentes principais usam tokens e padroes compartilhados.
- Layout continua responsivo em mobile e desktop.
- `npm run lint` e `npm run build` passam.

### 6. [Docs] Atualizar documentacao

**Objetivo:** manter a documentacao alinhada com a arquitetura atual do projeto.

**Escopo:**
- Atualizar setup local, comandos Docker e seed de dados.
- Documentar endpoints publicos e administrativos.
- Documentar fluxo de conteudo: membros, projetos, noticias, parceiros e processo seletivo.
- Documentar design tokens e componentes reutilizaveis.

**Criterios de aceite:**
- Um novo dev consegue subir o projeto e popular dados seguindo o README.
- Documentacao indica claramente quais comandos sao legados.
- Rotas principais e endpoints estao descritos.
