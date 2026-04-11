import { Link, useParams } from "react-router-dom";
import "./index.css";

const members = [
  {
    slug: "ana-carolina-silva",
    name: "Ana Carolina Silva",
    role: "Presidente",
    course: "Administração",
    year: "4º ano",
    image: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=900",
    description:
      "Apaixonada por estratégia e inovação, lidero o ICC com foco em desenvolver os melhores talentos em consultoria do Brasil.",
    skills: ["Estratégia", "Liderança", "Business Analytics", "Gestão de Projetos"],
    projects: ["Projeto Estratégico - Ambev", "Due Diligence - Startup Fintech", "Pesquisa de Mercado - Retail"],
  },
  {
    slug: "pedro-henrique-costa",
    name: "Pedro Henrique Costa",
    role: "Vice-Presidente",
    course: "Economia",
    year: "4º ano",
    image: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=900",
    description: "Atua no apoio à presidência e na coordenação de iniciativas estratégicas do clube.",
    skills: ["Negócios", "Análise Financeira", "Gestão"],
    projects: ["Plano de expansão - varejo"],
  },
];

export default function EquipeDetalhe() {
  const { slug } = useParams();

  const member = members.find((item) => item.slug === slug);

  if (!member) {
    return (
      <main style={{ padding: 24 }}>
        <Link to="/equipe">← Voltar para equipe</Link>
        <h1>Perfil não encontrado</h1>
      </main>
    );
  }

  return (
    <main className="member-page">
      <Link to="/equipe" className="back-link">
        ← Voltar para equipe
      </Link>

      <section className="member-hero">
        <img src={member.image} alt={member.name} className="member-hero-image" />

        <div className="member-hero-content">
          <h1>{member.name}</h1>
          <h2>{member.role}</h2>
          <p className="member-meta">
            {member.course} • {member.year}
          </p>

          <p className="member-description">{member.description}</p>

          <div className="detail-actions">
            <a href="#" className="detail-button linkedin">
              LinkedIn
            </a>
            <a href="#" className="detail-button email">
              Email
            </a>
          </div>
        </div>
      </section>

      <section className="detail-box">
        <h3>Competências</h3>
        <div className="tags">
          {member.skills.map((skill) => (
            <span key={skill} className="tag">
              {skill}
            </span>
          ))}
        </div>
      </section>

      <section className="detail-box">
        <h3>Projetos Realizados</h3>
        <ul className="projects-list">
          {member.projects.map((project) => (
            <li key={project}>{project}</li>
          ))}
        </ul>
      </section>
    </main>
  );
}