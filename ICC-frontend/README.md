# ICC-frontend

Site público da Liga Insper Consulting Club, em React 19 + TypeScript + Vite. Todo o conteúdo vem da API do backend; o que está fixo no código é só a estrutura, os textos institucionais da Home e os links das redes.

Para subir o projeto inteiro (banco, backend e frontend), siga o [README da raiz](../README.md). Para rodar só o frontend apontando para uma API já no ar:

```bash
cd ICC-frontend
npm install
VITE_API_URL=https://icc-backend-4b38.onrender.com/api npm run dev
```

## Scripts

| Comando | O que faz |
|---|---|
| `npm run dev` | Servidor de desenvolvimento em `http://localhost:5173` |
| `npm run build` | Checa os tipos (`tsc`) e gera o site em `dist/` |
| `npm run lint` | ESLint |
| `npm run preview` | Serve o `dist/` localmente, para conferir o build |

Antes de abrir um PR, rode `npm run lint` e `npm run build`: os dois precisam passar.

## Variável de ambiente

| Variável | Valor |
|---|---|
| `VITE_API_URL` | Endereço da API, terminando em `/api`. Local: `http://localhost:8000/api` (o `docker-compose.yml` já define). Produção: `https://icc-backend-4b38.onrender.com/api` |

Variáveis `VITE_*` entram no código **na hora do build**. Mudar o valor no Render exige um novo deploy do frontend.

## Estrutura

```
src/
├── main.tsx          # Rotas (cada página carrega sob demanda, exceto a Home)
├── App.tsx           # Layout: Header, conteúdo da rota e Footer
├── api.ts            # Todas as chamadas à API
├── types.ts          # Tipos dos dados que a API devolve
├── redes.ts          # E-mail e links do Instagram, LinkedIn e GitHub (um lugar só)
├── index.css         # Design tokens e estilos globais
├── components/       # Header, Footer, PageHero, MemberCard, ContentBlock, Icons...
├── hooks/            # usePageTitle, useProgramas, useDiretorias
├── images/           # Logo e imagens fixas
└── pages/            # Uma pasta por página, com index.tsx e index.css
```

Cada página fica em `pages/<Nome>/` com o seu próprio CSS. Os nomes das pastas nem sempre batem com a rota: a lista de artigos está em `pages/Noticias` (nome da versão anterior) e a página de um artigo em `pages/Artigo`.

### Adicionar uma página

1. Crie `pages/<Nome>/index.tsx` (com `export default`) e `index.css`.
2. Registre a rota em `main.tsx`, no mesmo formato `lazy` das outras.
3. Se ela precisar de dados novos, acrescente a chamada em `api.ts` e o tipo em `types.ts`.
4. Se for para o menu, acrescente o item em `NAV` (`components/Header`) e em `NAVEGACAO` (`components/Footer`).
5. Use `usePageTitle` para o título da aba e `PageHero` para o cabeçalho. Os estilos que valem para o site todo (botões, seções, grades, títulos) ficam em `index.css`.

### Rotas

| Rota | Página |
|---|---|
| `/` | Home (com o carrossel de parceiros) |
| `/equipe`, `/equipe/:id` | Equipe por diretoria e perfil do membro |
| `/parceiros`, `/parceiros/:id` | Parceiros e perfil do parceiro |
| `/projetos`, `/projetos/:slug` | Programas e detalhe com os cases |
| `/artigos`, `/artigos/:id` | Lista de artigos e página do artigo (resumo, temas, texto, "Como citar", compartilhar). `/news` redireciona para a lista |
| `/processo` | Processo seletivo ("Inscreva-se" ou "Inscrições encerradas", conforme o admin) |
| `/contato` | Canais oficiais |
| `/politica-de-privacidade` | Política de privacidade |
| qualquer outra | Página 404 |

As pastas `pages/Atividades`, `CategoriaAtividade`, `PerfilAtividade` e `PerfilAtividadeItem` não têm mais rota (a página saiu do site a pedido do ICC) e estão marcadas para remoção no [backlog](../backlog.md).

## Design tokens

Definidos em `:root`, no início de `src/index.css`, a partir do guia de marca do ICC. Use as variáveis em vez de valores soltos:

| Grupo | Tokens |
|---|---|
| Cores da marca | `--vermelho-icc` (#b20000), `--vermelho-escuro` (#7b001e), `--preto`, `--branco`, `--gradiente-icc`, `--vermelho-suave` |
| Cinzas | `--cinza-50` a `--cinza-800` |
| Tipografia | `--font-display` e `--font-body` (Poppins), `--fs-display`, `--fs-h1` a `--fs-h3`, `--fs-lead`, `--fs-body`, `--fs-small`, `--fs-xs` |
| Layout | `--container` (1200px), `--radius`, `--header-height` (calculada pelo Header) |

## Componentes reutilizáveis

| Componente | Uso |
|---|---|
| `PageHero` | Cabeçalho das páginas internas (título, subtítulo, eyebrow e link de voltar) |
| `MemberCard` | Card de membro (Home e Equipe) |
| `ContentBlock` | Bloco de texto e imagem (hoje só nas páginas de atividade, que estão sem rota) |
| `Icons` | Ícones SVG (setas, redes sociais, menu), herdando a cor do texto |
| `CargaInicial` | Tela exibida enquanto a primeira rota carrega |

Hooks: `usePageTitle(titulo, descricao)` define o título da aba e a descrição para compartilhamento; `useProgramas` e `useDiretorias` buscam uma vez e reaproveitam as listas usadas no menu.
