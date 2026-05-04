import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import { api } from "../../api"
import type { Member, Statistic, Partner } from "../../types"
import "./index.css"

export default function Home() {
  const [members, setMembers] = useState<Member[]>([])
  const [statistics, setStatistics] = useState<Statistic[]>([])
  const [partners, setPartners] = useState<Partner[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    Promise.all([
      api.getMembers(),
      api.getStatistics(),
      api.getPartners(),
    ]).then(([membersData, statsData, partnersData]) => {
      setMembers(membersData.slice(0, 6))
      setStatistics(statsData)
      setPartners(partnersData)
      setLoading(false)
    })
  }, [])

  if (loading) return <p>Carregando...</p>

  return (
    <body>
      a
    </body>
  )
}
