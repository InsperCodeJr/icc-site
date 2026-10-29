# Feedback do cliente

Registro das conversas com o **Insper Consulting Club (ICC)** sobre o site: o que foi apresentado, o que aprovaram, o que pediram e o que mudou a partir disso. O feedback das avaliações da Insper Code aparece só como contexto; o resumo técnico das mudanças está em [`DECISOES.md`](DECISOES.md#6-mudanças-a-partir-do-feedback-do-cliente).

> **Campos marcados com ⚠️ ainda precisam ser preenchidos pelo time** (data exata e participantes). Não deixe este arquivo com ⚠️ na entrega final.

---

## Contexto

A Coordenadora Tech do ICC, Ana Beatriz da Cunha, participou da reunião da entrega intermediária 1 (07/10/2026). Depois dela, o coordenador do projeto levou o site ao Diretor Tech do ICC, Gabriel Ávila, e o time passou a orientar as mudanças pelos pedidos do cliente, registrados abaixo.

**Contatos com o ICC**

| Pessoa | Cargo no ICC | Canal |
|---|---|---|
| Diretoria do ICC, incluindo Gabriel Ávila (Gabs) | Diretor Tech | Canal oficial: Matteo Rosso, coordenador do projeto, fala direto com a diretoria |
| Ana Beatriz da Cunha | Coordenadora Tech | Canal informal: colega de sala de Cynthia Yasutake (desenvolvedora). Tira dúvidas rápidas e leva assuntos ao Gabriel Ávila |

Decisões sobre o site (aprovações, conteúdo, contas) passam pelo canal oficial; o canal informal agiliza dúvidas do dia a dia.

## 1. Feedback sobre a versão do site em desenvolvimento

| | |
|---|---|
| **Data** | 16/10/2026, segundo o coordenador (conversa com o ICC); repassado ao time em 21/10/2026 |
| **Formato** | Conversa do coordenador do projeto com o Diretor Tech do ICC; os pedidos foram repassados ao time numa reunião interna da Code Jr |
| **Participantes do ICC** | Gabriel Ávila (Gabs), Diretor Tech |
| **Participantes da Code Jr** | Matteo Rosso (coordenador); Cynthia Yasutake, Sophia Kalil, Luan Ferreira (desenvolvedores) |
| **O que foi apresentado** | O site em produção, com os dados reais do ICC: Home, Equipe, Parceiros, Projetos, Atividades, Notícias, Contato e Processo Seletivo. Os links do site e da API em produção foram enviados ao coordenador em 13/10/2026 (⚠️ confirmar com o Matteo se foi isso que ele mostrou) |

**O que aprovaram**
- O carrossel com os logos dos patrocinadores na página inicial.

**O que pediram e o que mudou**

| Pedido do ICC | O que foi feito | PR |
|---|---|---|
| A página de Atividades repetia o que já está em Projetos | Página removida do site e do menu | #10 (21/10) |
| Parceiros mais perto de Equipe no menu | Menu reordenado: Equipe → Parceiros → Projetos → Artigos → Contato | #10 (21/10) |
| O contato já tem e-mail; o formulário não tinha uso | Formulário removido; o Contato mostra só os canais oficiais | #11 (22/10) |
| A seção de notícias seria usada para artigos científicos | Ver a seção 2 | #16 (27/10) |
| Não pedir "cadastre-se para receber atualizações", porque não há mailing; mandar para um Google Forms | Controle manual das inscrições no admin: aberto, botão "Inscreva-se" com o link do formulário; fechado, "Inscrições encerradas" | #12 (25/10) |
| Manter as datas do último processo seletivo no site | Só um processo ativo por vez; o último fica visível, com as inscrições fechadas, até o próximo | #12 (25/10) |
| GitHub do ICC junto com Instagram e LinkedIn | Link no header, no rodapé e no Contato | #13 (26/10) |
| Carrossel de patrocinadores na Home | Carrossel contínuo dos logos dos parceiros; logos recortados e caixas maiores depois de revisão | #14, #15 (26/10) e #17 (27/10) |

---

## 2. Seção de artigos

| | |
|---|---|
| **Data** | 26/10/2026 (referências repassadas ao time) |
| **Formato** | Mensagens: o Diretor Tech do ICC enviou o exemplo ao coordenador do projeto, e a Coordenadora Tech comentou a seção com a desenvolvedora |
| **Participantes do ICC** | Gabriel Ávila (Gabs), Diretor Tech; Ana Beatriz da Cunha, Coordenadora Tech |
| **Participantes da Code Jr** | Matteo Rosso (coordenador), Cynthia Yasutake |

**O que pediram**
- A seção "Notícias" deve ser usada para **artigos de autoria dos membros do ICC**, não para notícias externas.
- Como referência, o ICC enviou a aba de artigos de outro consulting club universitário. Uma integrante do ICC também sugeriu um working paper do NBER como exemplo de formato.

**O que mudou** (PR #16, 27/10)
- "Notícias" virou "Artigos". Cada artigo tem página própria (`/artigos/<id>`) com autores, temas, resumo, texto completo, "Como citar" e compartilhamento no LinkedIn.
- Os 3 artigos que começam com "[Exemplo]" eram só demonstração do formato. O primeiro artigo real depende da definição do formato (seção 3); sem ele, os exemplos são apagados antes da entrega.

---

## 3. Site no ar e área administrativa enviados ao ICC (13/10 e 26/10)

| | |
|---|---|
| **Datas** | 13/10/2026: link do site em produção (https://icc-site.onrender.com). 26/10/2026: link da área administrativa (https://icc-backend-4b38.onrender.com/admin/) com as credenciais de acesso |
| **Formato** | Mensagens |
| **Participantes do ICC** | Ana Beatriz da Cunha, Coordenadora Tech |
| **Participantes da Code Jr** | Cynthia Yasutake |

**Retorno do ICC**

| Data | Pedido ou sugestão do ICC | O que foi feito | PR |
|---|---|---|---|
| 26/10/2026 | O backend no plano gratuito do Render "dorme" depois de 15 minutos sem acesso, e o primeiro acesso fica lento. Sugestão: fazer requisições periódicas (a cada 14 minutos) para mantê-lo acordado, já que as 750 horas mensais grátis cobrem um único serviço ligado o mês inteiro | Endpoint `/api/health/`, que responde sem consultar o banco, e monitor no UptimeRobot chamando-o a cada 5 minutos; também avisa por e-mail se o site cair | #16 (27/10) |
| 29/10/2026 | **Aprovação geral:** "as pessoas do ICC para as quais mostrei o site aprovaram o site" | — | — |
| 29/10/2026 | **Crítico:** os artigos precisam aceitar Markdown em vez de texto simples, principalmente para ter imagens no meio do texto. A Coordenadora Tech escreve um artigo assim que o formato estiver definido | Em definição com o ICC. O coordenador do projeto sugeriu aceitar o artigo em PDF, exibido dentro do site; a proposta do time é oferecer os dois formatos: Markdown no texto (negrito, títulos, listas, links) e PDF para artigos com imagens, tabelas e gráficos. Implementação após a confirmação do ICC (tarefa 16 do backlog) | — |
| 29/10/2026 | **Desejável:** filtrar os artigos por autor ou tema (por exemplo, nome do autor clicável levando à lista de artigos filtrada) | Registrado no backlog para uma próxima gestão (tarefa 17) | — |
| 29/10/2026 | **Projetos a cadastrar:** o challenge com a Galeazzi & Associados (Pedagógico, valendo fast pass); as visitas à Bain e à McKinsey e participações em challenges de business case, que não se encaixam nas 4 categorias. Tudo o que está no Instagram e no LinkedIn do ICC pode ser usado | 4 projetos cadastrados no admin de produção a partir dos posts do ICC: Challenge Insper com a Galeazzi (Pedagógico), capacitação de trainees na McKinsey, Interclubs Challenge com a Bain e visita à Bain. Para eles aparecerem no site, cada projeto ganhou página própria, os programas passaram a listar os seus projetos, e a página Projetos ganhou a seção "Outros projetos" para os que não pertencem a nenhum programa | #25, #26, #27 (29/10) |
| 29/10/2026 | **Números da Home:** 31 membros atuais, 15 parceiros, fundado em 2020 | Cadastrados em Estatísticas no admin de produção; a faixa de números da Home voltou a aparecer | — |

**Acesso ao admin:** em 28/10/2026, o login enviado em 26/10 passou a ser de uso exclusivo do ICC, e a equipe de desenvolvimento passou a usar logins próprios. A troca de senha foi recomendada à Coordenadora Tech, para que só o ICC a conheça. Novos acessos do ICC são criados por ela, um por pessoa, como explica o [guia do admin](GUIA_ADMIN.md#logins-para-outras-pessoas-do-icc).

---

## 4. Apresentação do MVP no ar

| | |
|---|---|
| **Data** | 29/10/2026 (⚠️ a confirmar) |
| **Formato** | Encontro do coordenador do projeto com o Diretor Tech do ICC (⚠️ presencial ou chamada) |
| **Participantes do ICC** | Gabriel Ávila (Gabs), Diretor Tech |
| **Participantes da Code Jr** | Matteo Rosso (coordenador) (⚠️ e quem mais for) |
| **O que foi apresentado** | O site em produção (https://icc-site.onrender.com) e a área administrativa (link "Área administrativa" no rodapé): cadastrar e arquivar um membro, cadastrar um projeto, abrir e fechar as inscrições do PS, publicar um artigo |

**Perguntas a levar** (vêm da lista "Dúvidas ao cliente" do Trello)
- [ ] Os textos institucionais da Home e da página de Parceiros estão aprovados ou o ICC quer reescrever?
- [ ] Quais números entram nas estatísticas da Home?
- [ ] Quais projetos com parceiros devem ser cadastrados?
- [ ] Os links do LinkedIn de todos os membros estão certos?
- [ ] Quem do ICC recebe login de superusuário do admin?
- [ ] Para qual conta do ICC as contas de Render, Neon, Cloudinary e UptimeRobot serão transferidas?

**O que aprovaram**
- ⚠️

**O que pediram e o que muda**

| Pedido do ICC | O que vai ser feito | Prazo |
|---|---|---|
| ⚠️ | ⚠️ | ⚠️ |
