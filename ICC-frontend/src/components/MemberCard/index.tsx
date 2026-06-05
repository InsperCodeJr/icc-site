import { Link } from "react-router-dom";
import { drivePhotoUrl } from "../../utils";
import "./index.css";

type Member = {
  id: number;
  name: string;
  position: string;
  photo_url: string | null;
  course: string;
  year: number
};

export default function MemberCard({ member }: { member: Member }) {
  return (
    <Link to={`/equipe/${member.id}`} className="member-card">
      <img
        src={drivePhotoUrl(member.photo_url) || "https://placehold.co/400x400"}
        onError={(e) =>{(e.target as HTMLImageElement).src = "https://placehold.co/400x400";}}
        alt={member.name}
        className="member-image"
        loading="lazy"
      />

      <div className="member-content">
        <h3 className="member-name">{member.name}</h3>
        <p className="member-role">{member.position}</p>
      </div>
    </Link>
  );
}