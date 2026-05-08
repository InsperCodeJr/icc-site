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
    return (
      <div className="parceiros-page parceiros-loading">
        Carregando...
      </div>
    )
  }

  return (
    <div className="parceiros-page">
      <section className="parceiros-hero">
        <p className="parceiros-eyebrow">Parceiros</p>
        <h1 className="parceiros-titulo">
          Quem caminha <span className="parceiros-highlight">conosco</span>
        </h1>
        <p className="parceiros-lead">
          Conheça as empresas que apoiam o Insper Consulting Club e contribuem
          para a formação dos futuros líderes em consultoria.
        </p>
      </section>

      <section className="parceiros-grid-section">
        {partners.length === 0 ? (
          <div className="parceiros-empty">
            Em breve, novos parceiros.
          </div>
        ) : (
          <div className="parceiros-grid">
            {partners.map((p) => (
              <Link
                key={p.id}
                to={`/parceiros/${p.id}`}
                className="parceiro-card"
              >
                <div className="parceiro-logo">
                  {p.logo_url ? (
                    <img src={p.logo_url} alt={p.name} />
                  ) : (
                    <span>{p.name?.charAt(0) || "?"}</span>
                  )}
                </div>

                <h3 className="parceiro-nome">{p.name}</h3>
                <span className="parceiro-saiba">Saiba mais →</span>
              </Link>
            ))}
          </div>
        )}
      </section>

      <section className="parceiros-cta">
        <h2>Quer ser nosso parceiro?</h2>
        <p>
          Conecte sua empresa aos melhores talentos do Insper e contribua para
          a formação em consultoria.
        </p>
        <Link to="/contato" className="parceiros-btn">
          Entre em contato →
        </Link>
      </section>
    </div>
  )
}
