import { Link } from "react-router-dom";
import "./index.css";

export type Member = {
  slug: string;
  name: string;
  role: string;
  course: string;
  year: string;
  image: string;
};

type MemberCardProps = {
  member: Member;
};

export default function MemberCard({ member }: MemberCardProps) {
  return (
    <Link to={`/equipe/${member.slug}`} className="member-card-link">
      <article className="member-card">
        <img className="member-image" src={member.image} alt={member.name} />

        <div className="member-content">
          <h3 className="member-name">{member.name}</h3>
          <p className="member-role">{member.role}</p>
          <p className="member-info">
            {member.course} • {member.year}
          </p>

          <div className="member-actions">
            <span className="icon-button">in</span>
            <span className="icon-button">✉</span>
          </div>
        </div>
      </article>
    </Link>
  );
}