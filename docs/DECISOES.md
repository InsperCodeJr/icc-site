# Decisões técnicas

Registro das principais escolhas do projeto em 2026.2 e do porquê de cada uma, para quem for manter o site depois.

## 1. Refatorar o projeto anterior em vez de reescrever do zero

O case permitia as duas coisas. Optamos por **refatorar**, porque os problemas que impediram a adoção do site no semestre anterior estavam em pontos específicos, não na base inteira:

| Problema do projeto anterior | Como foi resolvido |
|---|---|
| Banco SQL local, inacessível à entidade | O backend passou a ler a conexão de `DATABASE_URL` e usa um Postgres na nuvem (Neon). Os dados reais do ICC foram importados com o comando `import_icc_data`. |
| Imagens salvas no disco do servidor | Upload para o Cloudinary: as imagens sobrevivem a novos deploys. |
| Interface que não representava o ICC | O frontend foi reconstruído página a página (Header, Footer, Home, Equipe, Projetos, Parceiros, Processo Seletivo), com design tokens nas cores, na tipografia e na logo do ICC. |

Já a estrutura de dados (membros, cargos, diretorias, projetos, parceiros), a API em Django REST Framework e o React com Vite estavam adequados. Reescrever tudo gastaria o semestre refazendo o que já funcionava, em vez de resolver o que impedia o uso.

## 2. Django Admin como área administrativa, em vez de um painel próprio

O case pede uma área administrativa autenticada, com CRUD de membros (com cargos) e de projetos. Usamos o **Django Admin**, personalizado:
- **Segurança pronta e mantida pelo Django:** login, sessões, proteção CSRF, senhas com hash e permissões por usuário. Um painel próprio exigiria criar autenticação de API, permissões e validações do zero, aumentando a superfície de ataque.
- **CRUD completo para todos os conteúdos**, inclusive os relacionados (diretorias de um membro, participantes de um case, datas de um processo seletivo), sem escrever telas.
- **Conteúdo novo sem código:** um campo ou model novo aparece no admin com poucas linhas.
- **Personalizações para o ICC:** tudo em português, miniaturas de fotos e logos, busca e filtros, "Exibir no site" para esconder sem apagar, ações de arquivar e reativar membros, e o controle de abertura das inscrições do processo seletivo.

O painel próprio no frontend ficou registrado como possibilidade futura no [`backlog.md`](../backlog.md).

## 3. Arquivar × excluir

Membros que saem do clube são **arquivados** (data de saída): somem do site, mas o histórico de cases e a trajetória continuam guardados. A **exclusão** continua disponível para cadastros feitos por engano, como pede o CRUD do case. Parceiros, programas e cases têm "Exibir no site" com o mesmo objetivo.

## 4. Hospedagem: Render, Neon e Cloudinary

| Serviço | Por quê |
|---|---|
| **Render** (backend e frontend) | Roda o backend direto do `Dockerfile` do repositório e publica o frontend como site estático, com HTTPS, no plano gratuito. |
| **Neon** (PostgreSQL) | Banco gerenciado e gratuito que não expira por inatividade (o case exige que o banco não caia com a falta de uso). O Postgres gratuito do próprio Render tem prazo de validade. |
| **Cloudinary** (imagens) | O disco dos serviços do Render é apagado a cada deploy; sem um armazenamento externo, as fotos enviadas pelo admin se perderiam. |

Limitações conhecidas e próximos passos (deploy manual, contas a transferir para a entidade, domínio próprio) estão na seção "Produção" do [README](../README.md#produção).

## 5. Segurança e configuração

- Nenhuma credencial fica no código: tudo vem de variáveis de ambiente (`ICC-backend/.env.example`), e o `.env` não é versionado.
- Em produção (`DEBUG=False`): HTTPS obrigatório, HSTS, cookies seguros e CORS liberado só para o domínio do site.
- O formulário de contato, que gravava dados de visitantes, saiu do site a pedido do cliente. Com isso, o site não coleta mais dados pessoais de visitantes.

## 6. Mudanças a partir do feedback do cliente

| Pedido do ICC | O que foi feito |
|---|---|
| A página de Atividades repetia o que já está em Projetos | Página removida do site e do menu |
| Parceiros mais perto de Equipe | Menu reordenado: Equipe → Parceiros → Projetos → Artigos → Contato |
| O contato já tem e-mail; o formulário não tinha uso | Formulário removido; o Contato mostra só os canais oficiais |
| Não pedir "cadastre-se para receber atualizações" (não há mailing) | Controle manual de inscrições no admin: aberto, "Inscreva-se" com o link do formulário; fechado, "Inscrições encerradas" |
| Manter as datas do último processo seletivo | Só um processo ativo por vez; o último fica visível, com as inscrições fechadas, até o próximo |
| Carrossel de patrocinadores na Home | Carrossel contínuo dos logos dos parceiros, que pausa no hover e respeita "reduzir movimento" |
| Seção de notícias usada para artigos científicos | Seção virou "Artigos", com autores, resumo, publicação e link |
| GitHub do ICC junto com Instagram e LinkedIn | Link no header, no rodapé e no Contato |
