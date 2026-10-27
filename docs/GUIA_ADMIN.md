# Guia da área administrativa

Este guia é para quem cuida do conteúdo do site no ICC. Nada aqui exige mexer em código.

**Endereço:** https://icc-backend-4b38.onrender.com/admin/

Entre com o seu usuário e a sua senha. Um monitor mantém o servidor acordado, então o admin deve abrir rápido. Se um dia demorar uns 30 segundos, o site continua funcionando: avise o responsável técnico, porque provavelmente o monitor parou.

Tudo o que você salva aparece no site na hora. Basta recarregar a página do site.

**Atalho:** a [rotina de cada semestre](#rotina-de-cada-semestre), no fim deste guia, resume o que precisa ser atualizado a cada troca de semestre.

---

## Como a tela está organizada

Na página inicial do admin, tudo fica no quadro **"Website"**. Cada linha é um tipo de conteúdo. Em todas as telas, o padrão é o mesmo:
- **Adicionar** (botão no canto superior direito da lista) cria um registro novo.
- Clicar no nome de um registro abre a edição.
- **Salvar** grava e volta para a lista. **Salvar e continuar editando** grava e fica na mesma tela.
- Na lista, a caixa de busca e os filtros da direita ajudam a achar o que procura.

### Esconder × apagar
Parceiros, programas e cases têm o campo **"Exibir no site"**. Desmarcado, o item some do site, mas continua guardado e pode voltar quando quiser. **Prefira esconder a apagar**: apagar é definitivo.

### Logins para outras pessoas do ICC
Cada pessoa que mexe no site deve ter o próprio login. Não compartilhe senha.

**Para dar acesso:** no quadro **Autenticação e Autorização**, abra **Usuários → Adicionar usuário**.
1. Crie o nome de usuário e a senha.
2. Na tela seguinte, marque **"Membro da equipe"**. Sem isso, a pessoa não consegue entrar no admin.
3. Escolha o nível de acesso:
   - marque **"Status de superusuário"** para acesso total, incluindo criar outros logins. Deixe isso para 1 ou 2 pessoas;
   - ou deixe desmarcado e, em **Permissões do usuário**, escolha só o que a pessoa pode mexer (por exemplo, todas as de "website", que é o conteúdo do site).

**Quando alguém sai da gestão:** abra o usuário dela e desmarque **"Ativo"**. Ela perde o acesso na hora.

---

## Membros

### Cadastrar uma pessoa
**Membros → Adicionar membro**
1. **Nome**, **Foto** (JPG ou PNG, de preferência quadrada), **Cargo principal**, **LinkedIn** e **Email**.
2. **Formação:** Curso e Período.
3. **No ICC:** Data de entrada, Biografia e, se quiser, Horas dedicadas.
4. Embaixo, em **Vínculos com Diretorias**, adicione uma linha por diretoria da pessoa: a diretoria, o cargo nela e a ordem em que ela aparece dentro da diretoria.
5. Salvar.

O **Cargo principal** define a ordem da pessoa no site e se ela aparece na Home. Os cargos ficam em **Cargos**, e cada um tem uma **Prioridade para exibição**: 0 = Presidência, 1 = Vice, 2 = Diretoria, 3 = Coordenação, 4 = Membro/Mentor, 5 = Trainee. Até 2 aparece na Home como liderança.

### Quando alguém sai do clube
Não apague. **Arquive**:
- na lista de Membros, marque a pessoa, escolha a ação **"Arquivar selecionados"** e clique em **Ir**; ou
- abra a pessoa e preencha a **Data de saída**.

A pessoa some da página Equipe, mas o histórico (cases, trajetória) continua guardado. Para trazê-la de volta, use **"Reativar selecionados"**. O filtro **Situação**, à direita, separa membros atuais de ex-membros.

**Excluir** fica só para cadastros feitos por engano.

### Diretorias
Em **Diretorias** você cria, renomeia e reordena as diretorias. A **Ordem de exibição** define a ordem das seções na página Equipe e no menu "Nossa Equipe".

---

## Parceiros

**Parceiros → Adicionar parceiro** (ou clique num existente para editar)
1. **Nome**, **Categoria**, **Site do parceiro** e **Descrição**.
2. **Logo:**
   - use **PNG com fundo transparente**, de preferência recortado rente ao logo (sem muita margem vazia em volta). Assim ele fica do tamanho certo no carrossel da Home e na página de parceiros;
   - **SVG não é aceito**: o admin recusa o arquivo.
3. **Ordem de exibição:** menor aparece primeiro.
4. Salvar. A miniatura na lista mostra o logo atual.

Para tirar um parceiro do site sem apagar, desmarque **"Exibir no site"**. Dá para fazer isso direto na lista.

---

## Programas e cases

**Programas** ficam em **Categorias de Atividades**. Cada programa aparece no menu "Projetos" e tem página própria. Campos principais: Nome, Subtítulo, Descrição, Tópicos (um por linha), Ícone do card, Frequência (badge) e **Exibir no site**.

**Cases de sucesso** ficam em **Cases de Sucesso → Adicionar**:
1. **Programa** a que o case pertence, **Semestre** (no formato `2025.1`), **Área**, **Tema**, **Banca avaliadora** (uma firma por linha), **Premiação** e **Link da publicação**, se houver.
2. Embaixo, em **Participantes do Case**, adicione os membros e o papel de cada um. Comece a digitar o nome para buscar.
3. Salvar.

A página **Projetos** do site mostra os programas e os cases de cada um.

**Projetos** (a linha "Projetos" do admin) são trabalhos feitos com um parceiro. Um projeto com **Data de conclusão** preenchida e um parceiro em **Parceiros envolvidos** aparece na página desse parceiro, em "Casos de sucesso".

---

## Artigos

Os artigos são escritos pelos membros do ICC e ficam **dentro do site**: cada um tem a própria página, com resumo, temas, o texto completo, "Como citar" e um botão para compartilhar no LinkedIn.

**Artigos → Adicionar artigo**
1. **Título** e **Autores** (separados por vírgula).
2. **Temas** (opcional, separados por vírgula, ex.: `Estratégia, Varejo`). Aparecem como etiquetas no topo do artigo.
3. **Resumo:** duas ou três frases. Aparece no card da lista e em destaque no topo do artigo.
4. **Texto do artigo:** o texto completo. **Deixe uma linha em branco entre os parágrafos**: é isso que separa os parágrafos no site. O campo aceita só texto, sem negrito, títulos ou imagens no meio. Para colar do Word ou do Google Docs, cole e confira as linhas em branco.
5. **Link externo** (opcional): se o artigo também saiu em outro lugar (revista, LinkedIn, um PDF no Drive do ICC com acesso "Qualquer pessoa com o link"). Aparece como o botão "Ver publicação original".
6. **Publicação** (opcional): o nome da revista ou do evento, se houver.
7. **Data de publicação** e, se quiser, **Imagem de capa** (horizontal). Sem imagem, o card mostra "ICC".
8. Salvar. No site, os mais recentes aparecem primeiro.

Os artigos que começam com **"[Exemplo]"** são só demonstração. Apague-os quando os artigos reais forem cadastrados.

---

## Processo seletivo

O site mostra **um processo seletivo por vez**: o que estiver marcado como **Ativo**. Ativar um processo desativa os outros sozinho.

### Cadastrar um processo
**Processos Seletivos → Adicionar**
1. **Título** (ex.: `Processo Seletivo 2027.1`) e **Ativo** marcado.
2. **Datas do Processo:** uma linha por fase, com nome, data ou período e ordem.
3. **Etapas Detalhadas** (opcional): descrição, duração e dicas de cada fase.
4. **Requisitos:** uma linha por requisito.
5. Salvar.

Os **materiais de preparação** (opcional) ficam em **Materiais de Preparação → Adicionar**: escolha o processo, dê um título e liste os itens.

### Abrir e fechar as inscrições
- **Para abrir:** no processo ativo, marque **"Inscrições abertas"** e cole o link do formulário (Google Forms) em **"Link de inscrição"**. O site passa a mostrar o botão **"Inscreva-se"**. O admin não deixa salvar com as inscrições abertas e sem link.
- **Para fechar:** desmarque **"Inscrições abertas"**. O site mostra **"Inscrições encerradas"** e um convite para seguir o Instagram.

**Entre um processo e outro:** deixe o último processo **ativo e com as inscrições fechadas**. Assim, quem visita o site vê as datas e etapas do último PS, que servem de referência. Quando o próximo começar, cadastre o novo processo: ele substitui o anterior ao ser ativado.

---

## Estatísticas da Home

**Estatísticas → Adicionar**: um **Valor/Número** (ex.: `120+`) e uma **Descrição** (ex.: `membros formados`). A faixa de números da Home só aparece quando existe pelo menos uma estatística.

---

## O que não fica no admin

Alguns itens fixos são alterados no código pelo time de desenvolvimento:
- textos institucionais da Home (missão, "Quem somos");
- links do Instagram, LinkedIn, GitHub e o e-mail de contato, que ficam no arquivo `ICC-frontend/src/redes.ts`.

Algumas linhas do admin **não aparecem mais no site** e podem ser ignoradas: **Atividades**, **Calendário do Semestre** e **Pedidos de contato**. Elas eram de páginas e do formulário que saíram do site a pedido do ICC.

---

## Rotina de cada semestre

| Quando | O quê | Onde |
|---|---|---|
| Antes do PS | Cadastrar o novo processo seletivo (datas, etapas, requisitos) e deixar **Ativo** | Processos Seletivos |
| Abertura do PS | Marcar **Inscrições abertas** e colar o link do formulário | Processos Seletivos |
| Fim das inscrições | Desmarcar **Inscrições abertas** (o processo continua ativo, com as datas visíveis) | Processos Seletivos |
| Entrada dos aprovados | Cadastrar os novos membros, com foto e diretoria | Membros |
| Troca de gestão | Arquivar quem saiu; atualizar cargos e diretorias | Membros, Cargos, Diretorias |
| Fim do semestre | Cadastrar os cases do semestre e atualizar os números da Home | Cases de Sucesso, Estatísticas |
| Sempre que houver | Novos artigos e parceiros | Artigos, Parceiros |
| Troca de gestão | Dar login a quem entrou e desativar o de quem saiu | Usuários |

Em caso de dúvida técnica (site fora do ar, erro ao salvar, algo que não aparece), procure o responsável técnico do site na Code Jr. As instruções para quem cuida da parte técnica estão no `README.md` do repositório.
