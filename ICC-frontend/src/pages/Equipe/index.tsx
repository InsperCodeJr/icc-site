import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import { api } from "../../api"
import type { Member } from "../../types"
import "./index.css"

export default function Equipe() {
  const [members, setMembers] = useState<Member[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.getMembers().then((data) => {
      setMembers(data)
      setLoading(false)
    })
  }, [])

  if (loading) return <p>Carregando...</p>

return (
  <div>
    <h1>Página da Equipe</h1>
    {/* Seu conteúdo aqui */}
  </div>
)
}
