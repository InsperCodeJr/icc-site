import { useEffect, useState } from "react"
import { api } from "../../api"
import type { ContactInfo } from "../../types"
import "./index.css"

export default function Contato() {
  const [contact, setContact] = useState<ContactInfo | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.getContact()
      .then((data) => {
        if (data && data.id) {
          setContact(data)
        }
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  return (
    <div className="contato-page">

      <section className="contato-header">
        <h1 className="contato-header__title">Contato</h1>
        <p className="contato-header__subtitle">
          Entre em contato com o Insper Consulting Club
        </p>
      </section>

      <section className="contato-section">
        {loading ? (
          <div className="contato-loading">
            <div className="contato-loading__spinner" />
            <span>Carregando...</span>
          </div>
        ) : !contact ? (
          <div className="contato-empty">
            <p>Informações de contato não disponíveis no momento.</p>
          </div>
        ) : (
          <div className="contato-grid">

            {contact.email && (
              <a href={`mailto:${contact.email}`} className="contato-card">
                <div className="contato-card__icon">
                  <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
                    <rect x="2" y="4" width="20" height="16" rx="2" stroke="currentColor" strokeWidth="1.8"/>
                    <path d="M2 7l10 7 10-7" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round"/>
                  </svg>
                </div>
                <div className="contato-card__content">
                  <span className="contato-card__label">Email</span>
                  <span className="contato-card__value">{contact.email}</span>
                </div>
                <svg className="contato-card__arrow" width="16" height="16" viewBox="0 0 24 24" fill="none">
                  <path d="M7 17L17 7M17 7H7M17 7v10" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </a>
            )}

            {contact.instagram && (
              <a href={contact.instagram} target="_blank" rel="noreferrer" className="contato-card">
                <div className="contato-card__icon">
                  <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
                    <rect x="2" y="2" width="20" height="20" rx="5" stroke="currentColor" strokeWidth="1.8"/>
                    <circle cx="12" cy="12" r="4" stroke="currentColor" strokeWidth="1.8"/>
                    <circle cx="17.5" cy="6.5" r="1" fill="currentColor"/>
                  </svg>
                </div>
                <div className="contato-card__content">
                  <span className="contato-card__label">Instagram</span>
                  <span className="contato-card__value">
                    {contact.instagram.replace('https://instagram.com/', '@').replace('https://www.instagram.com/', '@')}
                  </span>
                </div>
                <svg className="contato-card__arrow" width="16" height="16" viewBox="0 0 24 24" fill="none">
                  <path d="M7 17L17 7M17 7H7M17 7v10" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </a>
            )}

            {contact.linkedin && (
              <a href={contact.linkedin} target="_blank" rel="noreferrer" className="contato-card">
                <div className="contato-card__icon">
                  <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
                    <rect x="2" y="2" width="20" height="20" rx="4" stroke="currentColor" strokeWidth="1.8"/>
                    <path d="M7 10v7M7 7v.5" stroke="currentColor" strokeWidth="2" strokeLinecap="round"/>
                    <path d="M11 17v-4a2 2 0 0 1 4 0v4M11 10v7" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round"/>
                  </svg>
                </div>
                <div className="contato-card__content">
                  <span className="contato-card__label">LinkedIn</span>
                  <span className="contato-card__value">Insper Consulting Club</span>
                </div>
                <svg className="contato-card__arrow" width="16" height="16" viewBox="0 0 24 24" fill="none">
                  <path d="M7 17L17 7M17 7H7M17 7v10" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </a>
            )}

            {contact.whatsapp && (
              <a
                href={`https://wa.me/${contact.whatsapp.replace(/\D/g, '')}`}
                target="_blank"
                rel="noreferrer"
                className="contato-card"
              >
                <div className="contato-card__icon">
                  <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
                    <path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2 22l5.1-1.34A9.94 9.94 0 0 0 12 22c5.52 0 10-4.48 10-10S17.52 2 12 2z" stroke="currentColor" strokeWidth="1.8" strokeLinejoin="round"/>
                    <path d="M8.5 9.5c.5 1 1.5 2.5 3 3.5s2.5 1.5 3 1.5" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round"/>
                  </svg>
                </div>
                <div className="contato-card__content">
                  <span className="contato-card__label">WhatsApp</span>
                  <span className="contato-card__value">{contact.whatsapp}</span>
                </div>
                <svg className="contato-card__arrow" width="16" height="16" viewBox="0 0 24 24" fill="none">
                  <path d="M7 17L17 7M17 7H7M17 7v10" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </a>
            )}

          </div>
        )}
      </section>

    </div>
  )
}