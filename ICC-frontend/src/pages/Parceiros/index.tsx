import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import { api } from "../../api"
import type { Partner } from "../../types"
import "./index.css"

export default function Parceiros() {
  const [partners, setPartners] = useState<Partner[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.getPartners().then((data) => {
      setPartners(data)
      setLoading(false)
    })
  }, [])

  if (loading) return <p>Carregando...</p>

  return (
    /* codigo */
  )
}
