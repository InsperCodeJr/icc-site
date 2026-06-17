import { useEffect, useMemo, useState } from "react"
import { Link, useParams } from "react-router-dom"
import { api } from "../../api"
import iconMala from "../../images/icon_mala.png"
import "./index.css"

type PartnerProject = {
  id: number
  title: string
  description?: string
  start_date?: string
  end_date?: string | null
  category?: string
  images?: { image_url?: string }[]
}

type PartnerDetail = {
  id: number
  name: string
  description: string
  category?: string
  contato?: string
  site?: string | null
  logo_url?: string | null
  projects_count?: number
  projects?: PartnerProject[]
}

function formatDateBR(dateString?: string | null) {
  if (!dateString) return ""
  const date = new Date(dateString)
  if (Number.isNaN(date.getTime())) return dateString

  return new Intl.DateTimeFormat("pt-BR", {
    day: "2-digit",
    month: "long",
    year: "numeric",
  }).format(date)
}

export default function ParceiroDetalhe() {
  const { id } = useParams<{ id: string }>()
  const [partner, setPartner] = useState<PartnerDetail | null>(null)
  const [loading, setLoading] = useState(true)
  const [openIndex, setOpenIndex] = useState<number | null>(0)

  useEffect(() => {
    if (!id) return

    setLoading(true)
    api
      .getPartner(id)
      .then((data: PartnerDetail) => {
        setPartner(data)
        setOpenIndex(0)
      })
      .catch((err) => {
        console.error("Erro ao buscar parceiro:", err)
        setPartner(null)
      })
      .finally(() => setLoading(false))
  }, [id])

  const successCases = useMemo(() => {
    const projects = partner?.projects || []
    return projects
      .filter((project) => Boolean(project.end_date))
      .map((project) => ({
        ...project,
        dateLabel: formatDateBR(project.end_date),
      }))
  }, [partner])

  if (loading) {
    return <div className="partner-detail-page">Carregando...</div>
  }

  if (!partner) {
    return (
      <div className="partner-detail-page">
        <div className="partner-detail-container">
          <Link to="/parceiros" className="back-link">
            ← Voltar para parceiros
          </Link>

          <div className="partner-empty-state">
            Não foi possível carregar esse parceiro.
          </div>
        </div>
      </div>
    )
  }

  const projectsCount = partner.projects_count ?? successCases.length
  const heroImage = partner.logo_url || ""

  return (
    <div className="partner-detail-page">
      <div className="partner-detail-container">
        <Link to="/parceiros" className="back-link">
          ← Voltar para parceiros
        </Link>

        <section className="partner-hero-card">
          <div className="partner-hero-image">
            {heroImage ? (
              <img src={heroImage} alt={partner.name} />
            ) : (
              <div className="partner-hero-placeholder">
                {partner.name?.charAt(0)?.toUpperCase() || "?"}
              </div>
            )}
          </div>

          <div className="partner-hero-content">
            <div className="partner-hero-top">
              <div className="partner-hero-left">
                <h1 className="partner-hero-title">{partner.name}</h1>
                <p className="partner-hero-category">
                  {partner.category || "Parceiro"}
                </p>

                <span className="partner-pill">Parceiro Estratégico</span>
              </div>

              <div className="partner-stat-box">
                <strong>{projectsCount}</strong>
                <span>Projetos</span>
              </div>
            </div>

            <p className="partner-hero-description">{partner.description}</p>

            <div className="partner-hero-actions">
              {partner.site ? (
                <a
                  href={partner.site}
                  target="_blank"
                  rel="noreferrer"
                  className="partner-site-btn"
                >
                  Visitar site ↗
                </a>
              ) : null}
            </div>
          </div>
        </section>

        <section className="partner-section-card">
          <div className="section-header">
            <img
              src={iconMala}
              alt="Casos de Sucesso"
              className="section-icon-img"
            />
            <h2>Casos de Sucesso</h2>
          </div>

          <div className="success-list">
            {successCases.length === 0 ? (
              <div className="success-empty">
                Nenhum projeto concluído encontrado para este parceiro.
              </div>
            ) : (
              successCases.map((project, index) => {
                const isOpen = openIndex === index

                return (
                  <div
                    key={project.id}
                    className={`success-card ${isOpen ? "is-open" : ""}`}
                  >
                    <button
                      type="button"
                      className="success-trigger"
                      onClick={() =>
                        setOpenIndex(isOpen ? null : index)
                      }
                      aria-expanded={isOpen}
                    >
                      <span className="success-number">
                        {index + 1}
                      </span>

                      <span className="success-trigger-text">
                        {project.title}
                      </span>

                      <span className="success-chevron">
                        {isOpen ? "−" : "+"}
                      </span>
                    </button>

                    {isOpen ? (
                      <div className="success-panel">
                        {project.description ? (
                          <p className="success-description">
                            {project.description}
                          </p>
                        ) : (
                          <p className="success-description muted">
                            Projeto concluído sem descrição detalhada.
                          </p>
                        )}

                        <div className="success-meta">
                          {project.dateLabel ? (
                            <span>
                              Concluído em {project.dateLabel}
                            </span>
                          ) : null}

                          {project.category ? (
                            <span>{project.category}</span>
                          ) : null}
                        </div>
                      </div>
                    ) : null}
                  </div>
                )
              })
            )}
          </div>
        </section>
      </div>
    </div>
  )
}