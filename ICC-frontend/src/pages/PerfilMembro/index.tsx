import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../../api";
import type { MemberDetail } from "../../types";
import "./index.css";

export default function PerfilMembro() {
  const { id } = useParams();

  const [member, setMember] = useState<MemberDetail | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (id) {
      api.getMember(Number(id)).then((data) => {
        setMember(data);
        setLoading(false);
      });
    }
  }, [id]);

  if (loading) return <p>Carregando...</p>;

  if (!member) {
    return (
      <main style={{ padding: 24 }}>
        <Link to="/equipe">← Voltar para equipe</Link>
        <h1>Membro não encontrado</h1>
      </main>
    );
  }

  return (
    <main className="member-page">
      <Link to="/equipe" className="back-link">
        ← Voltar para equipe
      </Link>

      <section className="member-hero">
        <img
          src={member.image}
          alt={member.name}
          className="member-hero-image"
        />

        <div className="member-hero-content">
          <h1>{member.name}</h1>
          <h2>{member.role}</h2>

          <p className="member-meta">
            {member.course} • {member.year}
          </p>

          <p className="member-description">
            {member.description}
          </p>

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
          {member.skills?.map((skill) => (
            <span key={skill} className="tag">
              {skill}
            </span>
          ))}
        </div>
      </section>

      <section className="detail-box">
        <h3>Projetos Realizados</h3>
        <ul className="projects-list">
          {member.projects?.map((project) => (
            <li key={project}>{project}</li>
          ))}
        </ul>
      </section>
    </main>
  );
}