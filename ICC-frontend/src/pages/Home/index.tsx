import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import { api } from "../../api"
import type { Member, Statistic, Partner } from "../../types"
import "./index.css"

export default function Home() {
  const [members, setMembers] = useState<Member[]>([])
  const [statistics, setStatistics] = useState<Statistic[]>([])
  const [partners, setPartners] = useState<Partner[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    Promise.all([
      api.getMembers(),
      api.getStatistics(),
      api.getPartners(),
    ]).then(([membersData, statsData, partnersData]) => {
      setMembers(membersData.slice(0, 6))
      setStatistics(statsData)
      setPartners(partnersData)
      setLoading(false)
    })
  }, [])

  return (
    <main className="home">
      {/* HERO */}
      <section className="hero-icc">
        <div className="hero-icc__overlay" />
        <div className="hero-icc__content">
          <span className="hero-icc__eyebrow">
            <span className="hero-icc__eyebrow-line" />
            CONSULTORIA × CARREIRA
          </span>
          <h1 className="hero-icc__title">
            Prepare-se para os processos <br />
            <em>que definem sua carreira.</em>
          </h1>
          <p className="hero-icc__subtitle">
            Somos a organização estudantil do Insper que forma alunos para os
            processos seletivos de consultoria — currículo, GMAT, Business
            Case, Case Interview e Personal Interview — com um trainee real de
            consultoria ao longo do semestre.
          </p>
          <div className="hero-icc__actions">
            <Link to="/processo" className="btn btn--primary">
              Seja membro →
            </Link>
            <Link to="/atividades" className="btn btn--ghost">
              Conheça as atividades
            </Link>
          </div>
        </div>
      </section>

      {/* SOBRE / MANIFESTO */}
      <section className="section about-icc">
        <div className="about-icc__text">
          <span className="eyebrow">A ORGANIZAÇÃO</span>
          <h2 className="section-title">
            Formação de consultoria, <br />
            <em>energia de estudante.</em>
          </h2>
          <p>
            Fundado em 2020, o Insper Consulting Club prepara alunos para os
            processos seletivos das empresas de consultoria e os expõe ao
            cotidiano da profissão através de um programa de trainee, no qual
            os membros resolvem um caso de consultoria real ao longo do
            semestre.
          </p>
          <p>
            Também promovemos eventos e capacitações em parceria com
            empresas, garantindo uma formação completa e sempre atualizada.
          </p>
        </div>
        <div className="about-icc__image">
          <img src="/src/images/background.jpg" alt="Membros do Insper Consulting Club" />
        </div>
      </section>

      {/* ESTATÍSTICAS */}
      <section className="stats-icc">
        {loading ? (
          <p className="stats-icc__loading">Carregando estatísticas...</p>
        ) : (
          statistics.map((stat) => (
            <div className="stats-icc__item" key={stat.id}>
              <span className="stats-icc__value">{stat.value}</span>
            </div>
          ))
        )}
      </section>

      {/* ATIVIDADES / TREINAMENTOS */}
      <section className="section training-icc">
        <span className="eyebrow eyebrow--center">O QUE FAZEMOS</span>
        <h2 className="section-title section-title--center">
          Treinamento completo, do currículo à entrevista final.
        </h2>

        <div className="training-icc__grid">
          <div className="training-card">
            <span className="training-card__index">01</span>
            <h3>Currículo</h3>
            <p>Elaboração e revisão de currículo com padrão de mercado.</p>
          </div>
          <div className="training-card">
            <span className="training-card__index">02</span>
            <h3>GMAT</h3>
            <p>Preparação para o teste exigido pelas principais consultorias.</p>
          </div>
          <div className="training-card">
            <span className="training-card__index">03</span>
            <h3>Business Case</h3>
            <p>Treino de raciocínio estruturado para resolução de cases.</p>
          </div>
          <div className="training-card">
            <span className="training-card__index">04</span>
            <h3>Case Interview</h3>
            <p>Simulações de entrevista de caso com feedback direto.</p>
          </div>
          <div className="training-card">
            <span className="training-card__index">05</span>
            <h3>Personal Interview</h3>
            <p>Preparação de fit e storytelling para a entrevista pessoal.</p>
          </div>
          <div className="training-card">
            <span className="training-card__index">06</span>
            <h3>Trainee</h3>
            <p>Resolução de um caso de consultoria real ao longo do semestre.</p>
          </div>
        </div>
      </section>

      {/* EQUIPE */}
      <section className="section team-icc">
        <div className="team-icc__header">
          <div>
            <span className="eyebrow">MEMBROS</span>
            <h2 className="section-title">Quem constrói o clube</h2>
          </div>
          <Link to="/equipe" className="btn btn--ghost">
            Ver equipe completa →
          </Link>
        </div>

        <div className="team-icc__grid">
          {loading ? (
            <p>Carregando equipe...</p>
          ) : (
            members.map((member) => (
              <Link to={`/equipe/${member.id}`} className="team-card" key={member.id}>
                <div className="team-card__photo">
                  {member.photo_url && <img src={member.photo_url} alt={member.name} />}
                </div>
                <h3>{member.name}</h3>
                <span>{member.role}</span>
              </Link>
            ))
          )}
        </div>
      </section>

      {/* PARCEIROS */}
      {!loading && partners.length > 0 && (
        <section className="section partners-icc">
          <span className="eyebrow eyebrow--center">PARCEIROS</span>
          <h2 className="section-title section-title--center">
            Empresas que confiam no nosso trabalho
          </h2>
          <div className="partners-icc__grid">
            {partners.map((partner) => (
              <Link to={`/parceiros/${partner.id}`} className="partner-logo" key={partner.id}>
                <img src={partner.logo_url} alt={partner.name} />
              </Link>
            ))}
          </div>
        </section>
      )}

      {/* CTA FINAL */}
      <section className="cta-icc">
        <h2>
          Pronto para dar o próximo passo <br /> na sua carreira?
        </h2>
        <Link to="/processo" className="btn btn--primary btn--lg">
          Faça parte do ICC →
        </Link>
      </section>
    </main>
  )
}