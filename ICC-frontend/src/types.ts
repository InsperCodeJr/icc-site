export interface Position {
  title: string
}

export interface Project {
  id: number
  title: string
  description: string
  partners: string[]
  start_date: string
  end_date: string | null
}

export interface Member {
  id: number
  name: string
  position: string
  photo_url: string | null
}

export interface MemberDetail extends Member {
  biography: string
  number_of_projects: number
  hours: number
  entry_date: string
  exit_date: string | null
  email: string | null
  linkedin: string | null
  projects: Project[]
}

export interface Partner {
  id: number
  name: string
  logo_url: string | null
}

export interface PartnerDetail extends Partner {
  description: string
  category: string | null
  contato: string
}

export interface Statistic {
  id: number
  value: string
  description: string
  order: number
}