import "./index.css";
import { Link } from "react-router-dom";

export default function Header() {
  return (
    <div className="header">
      <Link to={"/"} className="link-img">
        <img src="src\images\Logotipo Fundo Transparente Vermelho.png" alt="Logo ICC" />
      </Link>
      <section>
        <Link to={"/equipe"} className="link-text">Nossa Equipe</Link>
        <Link to={"/atividades"} className="link-text">Atividades</Link>
        <Link to={"/parceiros"} className="link-text">Parceiros</Link>
        <Link to={"/participe"} className="link-text">Seja membro</Link>
        <Link to={"/news"} className="link-text">Notícias</Link>
        <Link to={"/contato"} className="link-text">Contato</Link>
      </section>
    </div>
  );
}