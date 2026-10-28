# Feedback do cliente

Registro das conversas com o **Insper Consulting Club (ICC)** sobre o site: o que foi apresentado, o que aprovaram, o que pediram e o que mudou a partir disso. O feedback das avaliações da Insper Code fica fora deste arquivo; o resumo técnico das mudanças está em [`DECISOES.md`](DECISOES.md#6-mudanças-a-partir-do-feedback-do-cliente).

> **Campos marcados com ⚠️ ainda precisam ser preenchidos pelo time** (data exata e participantes). Não deixe este arquivo com ⚠️ na entrega final.

---

## 1. Feedback sobre a versão do site em desenvolvimento

| | |
|---|---|
| **Data** | ⚠️ DD/MM/2026 (antes de 21/10/2026, quando os primeiros ajustes entraram na `main`) |
| **Formato** | ⚠️ reunião presencial / chamada / mensagens no grupo |
| **Participantes do ICC** | ⚠️ nomes e cargos |
| **Participantes da Code Jr** | ⚠️ nomes |
| **O que foi apresentado** | O site rodando com os dados reais do ICC: Home, Equipe, Parceiros, Projetos, Atividades, Notícias, Contato e Processo Seletivo |

**O que aprovaram**
- ⚠️ ex.: identidade visual, página da Equipe com as diretorias, perfis de parceiros

**O que pediram e o que mudou**

| Pedido do ICC | O que foi feito | PR |
|---|---|---|
| A página de Atividades repetia o que já está em Projetos | Página removida do site e do menu | #10 (21/10) |
| Parceiros mais perto de Equipe no menu | Menu reordenado: Equipe → Parceiros → Projetos → Artigos → Contato | #10 (21/10) |
| O contato já tem e-mail; o formulário não tinha uso | Formulário removido; o Contato mostra só os canais oficiais | #11 (22/10) |
| Não pedir "cadastre-se para receber atualizações", porque não há mailing | Controle manual das inscrições no admin: aberto, botão "Inscreva-se" com o link do formulário; fechado, "Inscrições encerradas" | #12 (25/10) |
| Manter as datas do último processo seletivo no site | Só um processo ativo por vez; o último fica visível, com as inscrições fechadas, até o próximo | #12 (25/10) |
| GitHub do ICC junto com Instagram e LinkedIn | Link no header, no rodapé e no Contato | #13 (26/10) |
| Carrossel de patrocinadores na Home | Carrossel contínuo dos logos dos parceiros; logos recortados e caixas maiores depois de revisão | #14, #15 (26/10) e #17 (27/10) |

---

## 2. Seção de artigos

| | |
|---|---|
| **Data** | ⚠️ DD/MM/2026 |
| **Formato** | ⚠️ mensagens (o exemplo foi enviado ao coordenador do projeto) |
| **Participantes do ICC** | ⚠️ nomes (inclui quem enviou o exemplo e a integrante do ICC que comentou a seção) |
| **Participantes da Code Jr** | ⚠️ Matteo Rosso (coordenador), Cynthia Naoko |

**O que pediram**
- A seção "Notícias" deve ser usada para **artigos de autoria dos membros do ICC**, não para notícias externas.
- Como referência, o ICC enviou a aba de artigos de outro consulting club universitário. Uma integrante do ICC também sugeriu um working paper do NBER como exemplo de formato.

**O que mudou** (PR #16, 27/10)
- "Notícias" virou "Artigos". Cada artigo tem página própria (`/artigos/<id>`) com autores, temas, resumo, texto completo, "Como citar" e compartilhamento no LinkedIn.
- Os 3 artigos que começam com "[Exemplo]" são só demonstração do formato. ⚠️ Aguardando o ICC enviar o primeiro artigo real; se não chegar até a entrega, os exemplos são apagados.

---

## 3. Apresentação do MVP no ar

| | |
|---|---|
| **Data** | ⚠️ DD/MM/2026 |
| **Formato** | ⚠️ |
| **Participantes do ICC** | ⚠️ |
| **Participantes da Code Jr** | ⚠️ |
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
