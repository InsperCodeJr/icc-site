import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import { api } from "../../api"
import type { ActivityCategory, CalendarMonth } from "../../types"
import "./index.css"

type SemesterFilter = 'both' | '1' | '2'

export default function Atividades() {
  const [categories, setCategories] = useState<ActivityCategory[]>([])
  const [calendar, setCalendar] = useState<CalendarMonth[]>([])
  const [semesterFilter, setSemesterFilter] = useState<SemesterFilter>('both')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    Promise.all([
      api.getCategories(),
      api.getCalendar(),
    ]).then(([categoriesData, calendarData]) => {
      setCategories(categoriesData)
      setCalendar(calendarData)
      setLoading(false)
    })
  }, [])

  const filteredCalendar = calendar.filter((m) => {
    if (semesterFilter === 'both') return true
    return m.semester === semesterFilter || m.semester === 'both'
  })

  if (loading) return <p className="atividades-loading">Carregando...</p>

  return (
    <div className="atividades-page">

      {/* Hero */}
      <section className="atividades-hero">
        <h1 className="atividades-hero__title">Nossas Atividades</h1>
        <p className="atividades-hero__subtitle">
          Um calendário completo de desenvolvimento profissional e prático
        </p>
      </section>

      {/* Cards Grid */}
      <section className="atividades-grid-section">
        <div className="atividades-grid">
          {categories.map((cat) => (
            <Link
              key={cat.slug}
              to={`/atividades/categoria/${cat.slug}`}
              className="atividade-card"
            >
              {/* Ícone */}
              <div className="atividade-card__icon">
                {cat.icon_url ? (
                  <img src={cat.icon_url} alt={cat.label} />
                ) : (
                  <div className="atividade-card__icon-placeholder" />
                )}
              </div>

              {/* Badge */}
              <div className="atividade-card__header">
                <span className={`atividade-card__badge ${cat.badge_class}`}>
                  {cat.badge}
                </span>
              </div>

              {/* Título e descrição */}
              <h3 className="atividade-card__title">{cat.label}</h3>
              <p className="atividade-card__desc">{cat.description}</p>

              {/* Tópicos */}
              {cat.highlights.length > 0 && (
                <ul className="atividade-card__list">
                  {cat.highlights.map((h) => (
                    <li key={h}>{h}</li>
                  ))}
                </ul>
              )}
            </Link>
          ))}
        </div>
      </section>

      {/* Calendário Anual */}
      <section className="calendario-section">
        <div className="calendario-wrapper">
          <div className="calendario-header">
            <h2 className="calendario-title">Calendário Anual</h2>
            <div className="calendario-filter">
              <button
                className={`calendario-filter__btn ${semesterFilter === 'both' ? 'active' : ''}`}
                onClick={() => setSemesterFilter('both')}
              >
                Ano completo
              </button>
              <button
                className={`calendario-filter__btn ${semesterFilter === '1' ? 'active' : ''}`}
                onClick={() => setSemesterFilter('1')}
              >
                1º Semestre
              </button>
              <button
                className={`calendario-filter__btn ${semesterFilter === '2' ? 'active' : ''}`}
                onClick={() => setSemesterFilter('2')}
              >
                2º Semestre
              </button>
            </div>
          </div>

          {filteredCalendar.length === 0 ? (
            <p className="calendario-empty">Nenhum mês cadastrado para este período.</p>
          ) : (
            <div className="calendario-grid">
              {filteredCalendar.map((c) => (
                <div key={c.id} className="calendario-card">
                  <h4 className="calendario-card__month">{c.month}</h4>
                  <ul className="calendario-card__list">
                    {c.items.map((item) => (
                      <li key={item}>{item}</li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>
          )}
        </div>
      </section>

    </div>
  )
}

