# Dependências e licenças

Bibliotecas usadas pelo projeto, com a versão e a licença declaradas por cada pacote (levantadas em 26/10/2026 a partir dos pacotes instalados). As versões exatas ficam em `ICC-backend/requirements.txt` e `ICC-frontend/package-lock.json`.

Todas as licenças são permissivas (MIT, BSD, Apache, PSF) ou LGPL. A LGPL permite usar a biblioteca, sem modificá-la, dentro de um projeto com outra licença, que é o nosso caso. Ao adicionar uma dependência nova, confira a licença e inclua uma linha aqui.

## Backend (Python)

| Pacote | Versão | Licença | Para quê |
|---|---|---|---|
| Django | 6.0.8 | BSD-3-Clause | Framework web, ORM e área administrativa |
| djangorestframework | 3.17.2 | BSD-3-Clause | API REST |
| django-cors-headers | 4.7.0 | MIT | Liberar a API só para o domínio do site |
| psycopg2-binary | 2.9.10 | LGPL (com exceções) | Driver do PostgreSQL |
| dj-database-url | 3.1.2 | BSD-3-Clause | Ler a conexão do banco de `DATABASE_URL` |
| gunicorn | 26.2.0 | MIT | Servidor de produção |
| whitenoise | 6.12.0 | MIT | Servir os arquivos estáticos do `/admin` |
| cloudinary | 1.42.1 | MIT | Cliente do Cloudinary |
| django-cloudinary-storage | 0.3.0 | MIT | Salvar os uploads do Django no Cloudinary |
| pillow | 12.3.0 | MIT-CMU | Validar e processar imagens |
| python-dotenv | 1.2.2 | BSD-3-Clause | Carregar o `.env` em desenvolvimento |
| requests | 2.33.0 | Apache-2.0 | Requisições HTTP (só no comando legado `download_photos`) |
| icalendar | 7.3.0 | BSD-2-Clause | Ler arquivos `.ics` do calendário |
| recurring-ical-events | 3.8.2 | LGPL-3.0-or-later | Expandir eventos recorrentes do calendário |
| sendgrid | 6.11.0 | MIT | E-mail do formulário de contato (sem uso desde a remoção do formulário) |
| asgiref | 3.11.1 | BSD-3-Clause | Dependência do Django |
| sqlparse | 0.6.0 | BSD | Dependência do Django |
| typing_extensions | 4.15.0 | PSF-2.0 | Dependência de tipagem |

## Frontend (JavaScript/TypeScript)

| Pacote | Versão | Licença | Para quê |
|---|---|---|---|
| react | 19.2.5 | MIT | Interface |
| react-dom | 19.2.5 | MIT | Renderização no navegador |
| react-router-dom | 7.18.4 | MIT | Rotas e navegação |
| vite | 8.3.4 | MIT | Servidor de desenvolvimento e build (dev) |
| @vitejs/plugin-react | 6.0.1 | MIT | Suporte a React no Vite (dev) |
| typescript | 5.9.3 | Apache-2.0 | Tipagem (dev) |
| eslint, @eslint/js | 9.39.4 | MIT | Lint (dev) |
| typescript-eslint | 8.59.1 | MIT | Regras de lint para TypeScript (dev) |
| eslint-plugin-react-hooks | 7.1.1 | MIT | Regras de lint para hooks (dev) |
| eslint-plugin-react-refresh | 0.5.2 | MIT | Regra de lint para recarregamento (dev) |
| globals | 17.6.0 | MIT | Variáveis globais para o lint (dev) |
| @types/node, @types/react, @types/react-dom | 24.12.2, 19.2.14, 19.2.3 | MIT | Tipos (dev) |

As dependências marcadas com "(dev)" só são usadas para desenvolver e gerar o site; não vão para o navegador do visitante.

## Outros recursos

| Recurso | Licença | Onde |
|---|---|---|
| Fonte Poppins (Google Fonts) | SIL Open Font License 1.1 | Tipografia do site |
| Ícone do GitHub (Simple Icons) | CC0 1.0 | `ICC-frontend/src/components/Icons.tsx` |
| Logos dos parceiros e do ICC | Pertencem às respectivas empresas e ao ICC | Fornecidos pelo ICC |

## Serviços externos

| Serviço | Uso | Plano |
|---|---|---|
| Render | Hospedagem do backend e do frontend | Gratuito |
| Neon | Banco PostgreSQL | Gratuito |
| Cloudinary | Armazenamento de imagens | Gratuito |
| GitHub | Código-fonte | Gratuito |

Detalhes de acesso e de deploy estão na seção "Produção" do [README](../README.md#produção).
