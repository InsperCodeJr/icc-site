import { useEffect, useState } from "react"
import { api } from "../../api"
import type { NewsItem } from "../../types"
import "./index.css"

function formatDate(date: string) {
  return new Date(date).toLocaleDateString("pt-BR", {
    day: "2-digit",
    month: "long",
    year: "numeric",
  })
}

export default function Noticias() {
  const [news, setNews] = useState<NewsItem[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.getNews().then((data) => {
      setNews(data)
      setLoading(false)
    })
  }, [])

  return (
    <div className="news-page">

      <section className="news-header">
        <h1 className="news-header__title">Notícias</h1>
        <p className="news-header__subtitle">
          Fique por dentro do que acontece no ICC e no mundo da consultoria
        </p>
      </section>

      <section className="news-section">
        {loading ? (
          <div className="news-loading">
            <div className="news-loading__spinner" />
            <span>Carregando...</span>
          </div>
        ) : news.length === 0 ? (
          <div className="news-empty">
            <p>Nenhuma notícia cadastrada no momento.</p>
          </div>
        ) : (
          <div className="news-grid">
            {news.map((item) => (
              <a
                key={item.id}
                href={item.link}
                target="_blank"
                rel="noreferrer"
                className="news-card"
              >
                <div className="news-card__image">
                  {item.image_url ? (
                    <img src={item.image_url} alt={item.title} />
                  ) : (
                    <div className="news-card__image-placeholder">
                      <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
                        <rect x="3" y="3" width="18" height="18" rx="2" stroke="currentColor" strokeWidth="1.5"/>
                        <circle cx="8.5" cy="8.5" r="1.5" fill="currentColor"/>
                        <path d="M21 15l-5-5L5 21" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
                      </svg>
                    </div>
                  )}
                </div>

                <div className="news-card__content">
                  <div className="news-card__meta">
                    {item.source && (
                      <span className="news-card__source">{item.source}</span>
                    )}
                    {item.date && (
                      <span className="news-card__date">{formatDate(item.date)}</span>
                    )}
                  </div>
                  <h3 className="news-card__title">{item.title}</h3>
                  <p className="news-card__desc">{item.description}</p>
                  <span className="news-card__cta">
                    Ler matéria
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
                      <path d="M7 17L17 7M17 7H7M17 7v10" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                    </svg>
                  </span>
                </div>
              </a>
            ))}
          </div>
        )}
      </section>

    </div>
  )
}