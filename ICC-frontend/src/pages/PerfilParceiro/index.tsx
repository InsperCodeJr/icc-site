import { useEffect, useState } from "react"
import { Link, useParams } from "react-router-dom"
import { api } from "../../api"
import type { PartnerDetail } from "../../types"
import "./index.css"

export default function PerfilParceiro() {
  const { id } = useParams()
  const [partner, setPartner] = useState<PartnerDetail | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (id) {
      api.getPartner(Number(id)).then((data) => {
        setPartner(data)
        setLoading(false)
      })
    }
  }, [id])

  if (loading) return <p>Carregando...</p>
  if (!partner) return <p>Parceiro não encontrado.</p>

  return (
    /* codigo */
  )
}
