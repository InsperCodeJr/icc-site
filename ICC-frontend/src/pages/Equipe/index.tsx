import "./index.css";
import MemberCard, { type Member } from "../../components/MemberCard";

const directors: Member[] = [
  {
    slug: "ana-carolina-silva",
    name: "Ana Carolina Silva",
    role: "Presidente",
    course: "Administração",
    year: "4º ano",
    image: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=800",
  },
  {
    slug: "pedro-henrique-costa",
    name: "Pedro Henrique Costa",
    role: "Vice-Presidente",
    course: "Economia",
    year: "4º ano",
    image: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=800",
  },
  {
    slug: "julia-martins",
    name: "Julia Martins",
    role: "Diretora de Projetos",
    course: "Administração",
    year: "3º ano",
    image: "https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?w=800",
  },
  {
    slug: "lucas-oliveira",
    name: "Lucas Oliveira",
    role: "Diretor de Marketing",
    course: "Engenharia",
    year: "3º ano",
    image: "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=800",
  },
];

const consultants: Member[] = [
  {
    slug: "rafael-ferreira",
    name: "Rafael Ferreira",
    role: "Consultor Senior",
    course: "Economia",
    year: "3º ano",
    image: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800",
  },
  {
    slug: "camila-rodrigues",
    name: "Camila Rodrigues",
    role: "Consultora Senior",
    course: "Administração",
    year: "2º ano",
    image: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=800",
  },
  {
    slug: "gabriel-lima",
    name: "Gabriel Lima",
    role: "Consultor",
    course: "Engenharia",
    year: "2º ano",
    image: "https://images.unsplash.com/photo-1507591064344-4c6ce005b128?w=800",
  },
  {
    slug: "mariana-alves",
    name: "Mariana Alves",
    role: "Consultora",
    course: "Economia",
    year: "2º ano",
    image: "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=800",
  },
  {
    slug: "thiago-nascimento",
    name: "Thiago Nascimento",
    role: "Consultor Junior",
    course: "Administração",
    year: "1º ano",
    image: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=800",
  },
  {
    slug: "isabela-costa",
    name: "Isabela Costa",
    role: "Consultora Junior",
    course: "Economia",
    year: "1º ano",
    image: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=800",
  },
  {
    slug: "felipe-souza",
    name: "Felipe Souza",
    role: "Consultor Junior",
    course: "Engenharia",
    year: "1º ano",
    image: "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=800",
  },
];

export default function Equipe() {
  return (
    <main className="equipe-page">
      <section className="hero">
        <h1>Nossa Equipe</h1>
        <p>
          Conheça os membros que fazem do ICC o principal clube de consultoria estudantil do
          Brasil
        </p>
      </section>

      <section className="section">
        <h2>Diretoria</h2>
        <div className="cards-grid">
          {directors.map((member) => (
            <MemberCard key={member.slug} member={member} />
          ))}
        </div>
      </section>

      <section className="section">
        <h2>Projetos</h2>
        <div className="cards-grid">
          {consultants.map((member) => (
            <MemberCard key={member.slug} member={member} />
          ))}
        </div>
      </section>
    </main>
  );
}