import FormContato from "../../components/FormContato";
// import { useEffect } from "react"
// import { api } from "../../api"
// import type { ContactInfo } from "../../types"
import "./index.css"

export default function Contato() {
  // const [contact, setContact] = useState<ContactInfo | null>(null)
  // const [loading, setLoading] = useState(true)

  // useEffect(() => {
  //   api.getContact()
  //     .then((data: any) => {
  //       if (data && data.id) {
  //         setContact(data)
  //       }
  //       setLoading(false)
  //     })
  //     .catch(() => setLoading(false))
  // }, [])

  return (
    <div className="contato-page">

      <div id="main-area">
        <h1 className="contato-header__title">Contato</h1>
        <p className="contato-header__subtitle">
          Entre em contato com o Insper Consulting Club
        </p>
        <FormContato />
      </div>
    </div>
  )
}
