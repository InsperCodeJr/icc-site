import { useEffect, useState } from "react"
import { Link, useParams } from "react-router-dom"
import { api } from "../../api"
import "./index.css"

interface ProjectDetail {
  id: number
  title: string
  description: string
  start_date: string
  end_date: string | null
  partners: { id: number; name: string }[]
  members: { id: number; name: string }[]
}

export default function PerfilAtividade() {
  const { id } = useParams()
  const [project, setProject] = useState<ProjectDetail | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (id) {
      api.getProject(Number(id)).then((data) => {
        setProject(data)
        setLoading(false)
      })
    }
  }, [id])

  if (loading) return <p>Carregando...</p>
  if (!project) return <p>Projeto não encontrado.</p>

  return (
    /* codigo */
  )
}
