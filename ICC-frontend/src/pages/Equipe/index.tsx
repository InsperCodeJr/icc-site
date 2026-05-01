import { useEffect, useState } from "react";
import MemberCard from "../../components/MemberCard";
import { api } from "../../api";
import type { Member } from "../../types";
import "./index.css";

export default function Equipe() {
  const [members, setMembers] = useState<Member[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.getMembers().then((data) => {
      setMembers(data);
      setLoading(false);
    });
  }, []);

  if (loading) return <p>Carregando...</p>;

  // separa os grupos baseado no cargo
  const directors = members.filter(
    (m) =>
      m.role.toLowerCase().includes("presidente") ||
      m.role.toLowerCase().includes("diretor")
  );

  const consultants = members.filter((m) =>
    m.role.toLowerCase().includes("consultor")
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
            <MemberCard
              key={member.id}
              nome={member.name}
              member_id={member.id}
            />
          ))}
        </div>
      </section>

      <section className="section">
        <h2>Projetos</h2>
        <div className="cards-grid">
          {consultants.map((member) => (
            <MemberCard
              key={member.id}
              nome={member.name}
              member_id={member.id}
            />
          ))}
        </div>
      </section>
    </main>
  );
}