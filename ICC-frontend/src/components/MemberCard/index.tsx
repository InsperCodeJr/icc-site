import { Link } from "react-router-dom";
import "./index.css"

interface MemberCardProps {
  nome: string;
  member_id: string;
}

export default function MemberCard({ nome, member_id }: MemberCardProps) {
  return (
    <Link to={`/equipe/${member_id}`}>
      <div className="card">
        <img src="https://placehold.co/200x300" alt="Foto do membro" />
        <h3>{nome}</h3>
      </div>
    </Link>
  );
}