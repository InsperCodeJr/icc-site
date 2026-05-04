import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import { api } from "../../api"
import type { Project } from "../../types"
import "./index.css"

export default function Atividades() {
  const [projects, setProjects] = useState<Project[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.getProjects().then((data) => {
      setProjects(data)
      setLoading(false)
    })
  }, [])

  if (loading) return <p>Carregando...</p>

  return (
    /* codigo */
  )
}
