import FormContato from "../../components/FormContato"
import PageHero from "../../components/PageHero"
import { InstagramIcon, LinkedInIcon, MailIcon } from "../../components/Icons"
import usePageTitle from "../../hooks/usePageTitle"
import "./index.css"

// Extraído de site-data/icc.json (sobre.contato).
const CANAIS = [
  {
    label: "E-mail",
    valor: "insperconsultingclub@gmail.com",
    href: "mailto:insperconsultingclub@gmail.com",
    icon: <MailIcon size={20} />,
  },
  {
    label: "Instagram",
    valor: "@insperconsultingclub",
    href: "https://www.instagram.com/insperconsultingclub/",
    icon: <InstagramIcon size={20} />,
  },
  {
    label: "LinkedIn",
    valor: "Insper Consulting Club",
    href: "https://br.linkedin.com/company/insperconsultingclub",
    icon: <LinkedInIcon size={19} />,
  },
]

export default function Contato() {
  usePageTitle("Contato", "Entre em contato com o Insper Consulting Club")

  return (
    <div className="contato-page">
      <PageHero title="Contato" lead="Entre em contato com o Insper Consulting Club" />

      <section className="section">
        <div className="container contato-grid">
          <aside className="contato-canais">
            <h2 className="contato-canais__title">Canais oficiais</h2>
            <ul>
              {CANAIS.map((canal) => (
                <li key={canal.label}>
                  <a
                    href={canal.href}
                    className="contato-canal"
                    {...(canal.href.startsWith("http") ? { target: "_blank", rel: "noopener noreferrer" } : {})}
                  >
                    <span className="contato-canal__icon">{canal.icon}</span>
                    <span>
                      <span className="contato-canal__label">{canal.label}</span>
                      <span className="contato-canal__valor">{canal.valor}</span>
                    </span>
                  </a>
                </li>
              ))}
            </ul>
          </aside>

          <div className="contato-form-wrap">
            <FormContato />
          </div>
        </div>
      </section>
    </div>
  )
}
