import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import { api } from "../../api"
import type { MemberDetail } from "../../types"
import "./index.css"

export default function PerfilMembro() {
  const { id } = useParams()
  const [member, setMember] = useState<MemberDetail | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (id) {
      api.getMember(Number(id)).then((data) => {
        setMember(data)
        setLoading(false)
      })
    }
  }, [id])

  if (loading) return <p>Carregando...</p>
  if (!member) return <p>Membro não encontrado.</p>

  return;
}
