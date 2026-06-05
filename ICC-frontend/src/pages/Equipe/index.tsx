import { useEffect, useState } from "react";
import MemberCard from "../../components/MemberCard";
import { api } from "../../api";
import "./index.css";

export default function Equipe() {
  const [members, setMembers] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.getMembers().then((data) => {
      setMembers(data);
      setLoading(false);
    });
  }, []);

  if (loading) return <p>Carregando...</p>;

  const directors = members.filter(
    (m) =>
      m.position?.toLowerCase().includes("presidente") ||
      m.position?.toLowerCase().includes("diretor")
  );

  const mentors = members.filter((m) =>
    m.position?.toLowerCase().includes("mentor") &&
    !(directors.includes(m))
  );

  const membros = members.filter((m) => 
    m.position?.toLowerCase().includes("trainee") ||
    m.position?.toLowerCase().includes("membro")
  );

  return (
    <main className="equipe-page">
      <section className="hero">
        <h1>Nossa Equipe</h1>
        <p>
          Conheça os membros que fazem do ICC o principal clube de consultoria
          estudantil do Brasil
        </p>
      </section>

      <section className="section">
        <h2>Diretoria</h2>
        <div className="cards-grid">
          {directors.map((member) => (
            <MemberCard key={member.id} member={member} />
          ))}
        </div>
      </section>

      <section className="section">
        <h2>Mentores</h2>
        <div className="cards-grid">
          {mentors.map((member) => (
            <MemberCard key={member.id} member={member} />
          ))}
        </div>
      </section>
      
      <section className="section">
        <h2>Trainees e Membros</h2>
        <div className="cards-grid">
          {membros.map((member) => (
            <MemberCard key={member.id} member={member} />
          ))}
        </div>
      </section>

    </main>
  );
}
