import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import { api } from "../../api"
import type { Partner } from "../../types"
import "./index.css"

export default function Parceiros() {
  const [partners, setPartners] = useState<Partner[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api
      .getPartners()
      .then((data) => {
        setPartners(data || [])
      })
      .catch((err) => {
        console.error("Erro ao buscar parceiros:", err)
        setPartners([])
      })
      .finally(() => setLoading(false))
  }, [])

  if (loading) {
    return <div className="parceiros-page parceiros-loading">Carregando...</div>
  }

  return (
    <div className="parceiros-page">
      <section className="parceiros-hero">
        <div className="parceiros-heading">
          <p className="parceiros-eyebrow">PARCEIROS</p>
          <h1 className="parceiros-titulo">
            Quem caminha <span className="parceiros-highlight">conosco</span>
          </h1>
        </div>

        <p className="parceiros-lead">
          Conheça as empresas que apoiam o Insper Consulting Club e contribuem
          para a formação dos futuros líderes em consultoria.
        </p>
      </section>

      <section className="parceiros-grid-section">
        {partners.length === 0 ? (
          <div className="parceiros-empty">Em breve, novos parceiros.</div>
        ) : (
          <div className="parceiros-grid">
            {partners.map((p) => (
              <Link key={p.id} to={`/parceiros/${p.id}`} className="parceiro-card">
                <div className="parceiro-card-media">
                  {p.logo_url ? (
                    <img src={p.logo_url} alt={p.name} />
                  ) : (
                    <div className="parceiro-card-placeholder">
                      {p.name?.charAt(0)?.toUpperCase() || "?"}
                    </div>
                  )}

                  <div className="parceiro-card-badge">↗</div>
                </div>

                <div className="parceiro-card-content">
                  <div className="parceiro-card-text">
                    <h3 className="parceiro-nome">{p.name}</h3>

                    <p className="parceiro-categoria">
                      {p.category || "Parceiro"}
                    </p>

                    <p className="parceiro-descricao">
                      {p.description || "Saiba mais sobre esta parceria."}
                    </p>
                  </div>

                  <span className="parceiro-saiba">Ver detalhes →</span>
                </div>
              </Link>
            ))}
          </div>
        )}
      </section>
    </div>
  )
}