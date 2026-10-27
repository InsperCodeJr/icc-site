import { useEffect, useState } from "react"
import { Link, useParams } from "react-router-dom"
import { api } from "../../api"
import type { NewsItem } from "../../types"
import PageHero from "../../components/PageHero"
import { ArrowLeftIcon, ExternalIcon, LinkedInIcon } from "../../components/Icons"
import usePageTitle from "../../hooks/usePageTitle"
import "./index.css"

function formatDate(date: string) {
  // Mesmo cuidado da lista: ano/mês/dia separados evitam o desvio de um dia do UTC.
  const [ano, mes, dia] = date.split("-").map(Number)
  return new Date(ano, mes - 1, dia).toLocaleDateString("pt-BR", { day: "2-digit", month: "long", year: "numeric" })
}

export default function Artigo() {
  const { id } = useParams<{ id: string }>()
  const [artigo, setArtigo] = useState<NewsItem | null>(null)
  const [loadedId, setLoadedId] = useState<string | undefined>()
  const [copiado, setCopiado] = useState(false)
  const loading = loadedId !== id
  usePageTitle(artigo?.title, artigo?.description)

  useEffect(() => {
    if (!id) return
    api
      .getNewsItem(Number(id))
      .then((data: NewsItem) => setArtigo(data && data.id ? data : null))
      .catch(() => setArtigo(null))
      .finally(() => setLoadedId(id))
  }, [id])

  if (loading) return <p className="loading">Carregando...</p>

  if (!artigo) {
    return (
      <section className="section">
        <div className="container">
          <Link to="/artigos" className="back-link">
            <ArrowLeftIcon size={14} />
            Voltar para artigos
          </Link>
          <p className="state-message">
            <strong>Artigo não encontrado</strong>
            Não foi possível carregar esse artigo.
          </p>
        </div>
      </section>
    )
  }

  // No admin, os parágrafos são separados por uma linha em branco. O React
  // escapa o texto, então nada digitado lá vira HTML na página.
  const paragrafos = artigo.content.split(/\n\s*\n/).map((p) => p.trim()).filter(Boolean)
  const temas = artigo.topics.split(",").map((t) => t.trim()).filter(Boolean)
  const url = window.location.href
  const ano = artigo.date?.slice(0, 4)
  const citacao = `${artigo.authors ? `${artigo.authors}. ` : ""}${artigo.title}. Insper Consulting Club${ano ? `, ${ano}` : ""}. Disponível em: ${url}.`

  function copiarCitacao() {
    navigator.clipboard.writeText(citacao).then(() => {
      setCopiado(true)
      setTimeout(() => setCopiado(false), 2000)
    })
  }

  return (
    <div className="artigo-page">
      <PageHero
        back={{ to: "/artigos", label: "Voltar para artigos" }}
        eyebrow={artigo.date ? formatDate(artigo.date) : undefined}
        title={artigo.title}
        lead={artigo.authors}
      />

      <section className="section">
        <article className="container artigo">
          {temas.length > 0 && (
            <ul className="artigo__temas">
              {temas.map((tema) => (
                <li key={tema}>{tema}</li>
              ))}
            </ul>
          )}
          {artigo.image_url && <img src={artigo.image_url} alt="" className="artigo__capa" />}
          {artigo.description && (
            <div className="artigo__resumo">
              <h2>Resumo</h2>
              <p>{artigo.description}</p>
            </div>
          )}
          {paragrafos.map((p, i) => (
            <p key={i}>{p}</p>
          ))}

          <div className="artigo__rodape">
            <h2>Como citar</h2>
            <p className="artigo__citacao">{citacao}</p>
            <div className="artigo__acoes">
              <button type="button" className="btn btn--secondary" onClick={copiarCitacao}>
                {copiado ? "Copiado!" : "Copiar citação"}
              </button>
              <a
                href={`https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(url)}`}
                target="_blank"
                rel="noopener noreferrer"
                className="btn btn--secondary"
              >
                <LinkedInIcon size={16} />
                Compartilhar
              </a>
              {artigo.link && (
                <a href={artigo.link} target="_blank" rel="noopener noreferrer" className="btn btn--secondary">
                  Ver publicação original
                  <ExternalIcon />
                </a>
              )}
            </div>
          </div>
        </article>
      </section>
    </div>
  )
}
