import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import { api } from "../../api"
import type { SelectionProcess } from "../../types"
import "./index.css"

export default function Processo() {
  const [process, setProcess] = useState<SelectionProcess | null>(null)
  const [loading, setLoading] = useState(true)
  const [notFound, setNotFound] = useState(false)

  useEffect(() => {
    api.getSelectionProcess()
      .then((data) => {
        if (data && data.id) {
          setProcess(data)
        } else {
          setNotFound(true)
        }
        setLoading(false)
      })
      .catch(() => {
        setNotFound(true)
        setLoading(false)
      })
  }, [])

  return (
    <div className="processo-page">

      {/* Header */}
      <section className="processo-header">
        <h1 className="processo-header__title">Processo Seletivo</h1>
        <p className="processo-header__subtitle">
          Participe do processo seletivo e faça parte do principal clube de consultoria do Brasil
        </p>
      </section>

      <section className="processo-section">
        {loading ? (
          <div className="processo-loading">
            <div className="processo-loading__spinner" />
            <span>Carregando...</span>
          </div>
        ) : notFound || !process ? (
          <div className="processo-card processo-card--empty">
            <p>Nenhum processo seletivo ativo no momento.</p>
            <p>Cadastre-se para receber atualizações quando abrirmos novas vagas.</p>
            <Link to="/mailing" className="processo-card__cta">
              Cadastre-se para receber atualizações →
            </Link>
          </div>
        ) : (
          <>
            {/* 1. Card vermelho com datas */}
            <div className="processo-card">
              <div className="processo-card__header">
                <span className="processo-card__icon">📅</span>
                <h2 className="processo-card__title">{process.title}</h2>
              </div>

              {process.stages.length > 0 && (
                <div className="processo-card__stages">
                  {process.stages.map((stage) => (
                    <div key={stage.id} className="processo-stage">
                      <span className="processo-stage__label">{stage.label}</span>
                      <span className="processo-stage__date">{stage.date}</span>
                    </div>
                  ))}
                </div>
              )}

              <Link to="/contato" className="processo-card__cta">
                Cadastre-se para receber atualizações →
              </Link>
            </div>

            {/* 2. Requisitos */}
            {process.requirements.length > 0 && (
              <div className="processo-requisitos">
                <h2 className="processo-requisitos__title">Requisitos</h2>
                <ul className="processo-requisitos__list">
                  {process.requirements.map((req) => (
                    <li key={req.id} className="processo-requisito">
                      <div className="processo-requisito__icon">
                        {req.icon_url ? (
                          <img src={req.icon_url} alt="" />
                        ) : (
                          <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
                            <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="1.8"/>
                            <path d="M8 12l3 3 5-5" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                          </svg>
                        )}
                      </div>
                      <span className="processo-requisito__text">{req.text}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {/* 3. Etapas detalhadas */}
            {process.steps.length > 0 && (
              <div className="processo-etapas">
                <h2 className="processo-etapas__title">Etapas do Processo</h2>
                <div className="processo-etapas__list">
                  {process.steps.map((step) => (
                    <div key={step.id} className="processo-etapa">
                      <div className="processo-etapa__square">
                        <span className="processo-etapa__number">{step.number}</span>
                        {step.image_url && (
                          <img src={step.image_url} alt="" className="processo-etapa__image" />
                        )}
                        {step.duration && (
                          <span className="processo-etapa__duration">
                            <svg width="13" height="13" viewBox="0 0 24 24" fill="none">
                              <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="1.8"/>
                              <path d="M12 7v5l3 3" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round"/>
                            </svg>
                            {step.duration}
                          </span>
                        )}
                      </div>

                      <div className="processo-etapa__content">
                        <h3 className="processo-etapa__title">{step.title}</h3>
                        <p className="processo-etapa__desc">{step.description}</p>
                        {step.tips.length > 0 && (
                          <div className="processo-etapa__tips">
                            <span className="processo-etapa__tips-label">Dicas:</span>
                            <ul className="processo-etapa__tips-list">
                              {step.tips.map((tip, i) => (
                                <li key={i}>{tip}</li>
                              ))}
                            </ul>
                          </div>
                        )}
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* 4. Materiais de Preparação */}
            {process.materials.length > 0 && (
              <div className="processo-materiais">
                <h2 className="processo-materiais__title">Materiais de Preparação</h2>
                <div className="processo-materiais__grid">
                  {process.materials.map((material) => (
                    <div key={material.id} className="processo-material">
                      <h3 className="processo-material__title">{material.title}</h3>
                      <ul className="processo-material__list">
                        {material.items.map((item) => (
                          <li key={item.id} className="processo-material__item">
                            <span className="processo-material__bullet">•</span>
                            {item.text}
                          </li>
                        ))}
                      </ul>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </>
        )}
      </section>

    </div>
  )
}