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

  const consultants = members.filter((m) =>
    m.position?.toLowerCase().includes("consultor")
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
        <h2>Projetos</h2>
        <div className="cards-grid">
          {consultants.map((member) => (
            <MemberCard key={member.id} member={member} />
          ))}
        </div>
      </section>
    </main>
  );
}