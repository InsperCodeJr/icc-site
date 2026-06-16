import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../../api";
import "./index.css";

export default function PerfilMembro() {
  const { id } = useParams();

  const [member, setMember] = useState<any>(null);
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
          src={member.photo_url || "https://placehold.co/400x500"}
          alt={member.name}
          className="member-hero-image"
        />

        <div className="member-hero-content">
          <h1>{member.name}</h1>

          {/* posição agora é string */}
          <h2>{member.position}</h2>

          {/* campos opcionais */}
          {member.entry_date && (
            <p className="member-meta">
              Entrou em: {member.entry_date}
            </p>
          )}

          {member.biography && (
            <p className="member-description">
              {member.biography}
            </p>
          )}
        </div>
      </section>

      {/* só mostra se existir */}
      {member.projects && member.projects.length > 0 && (
        <section className="detail-box">
          <h3>Projetos</h3>
          <ul className="projects-list">
            {member.projects.map((project: any) => (
              <li key={project.id}>{project.title}</li>
            ))}
          </ul>
        </section>
      )}
    </main>
  );
}