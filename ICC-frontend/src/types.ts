export interface ActivityCategory {
  id: number
  slug: string
  label: string
  description: string
  highlights: string[]
  icon_url: string | null
  badge: string
  badge_class: string
  order: number
}

export interface CalendarMonth {
  id: number
  month: string
  items: string[]
  semester: '1' | '2' | 'both'
  order: number
}

export interface ProjectImage {
  id: number
  image_url: string
  caption: string
  order: number
}

export interface TimelineEvent {
  id: number
  date: string
  title: string
  description: string
  order: number
}

export interface ContentBlock {
  id: number
  title: string
  text: string
  image_url: string | null
  image_caption: string
  image_align: 'left' | 'right' | 'center'
  order: number
}

export interface Project {
  id: number
  title: string
  description: string
  category: string | null
  partners: string[]
  start_date: string
  end_date: string | null
}

export interface ProjectDetail {
  id: number
  title: string
  description: string
  category: ActivityCategory | null
  start_date: string
  end_date: string | null
  partners: { id: number; name: string }[]
  members: { id: number; name: string }[]
  images: ProjectImage[]
  timeline_events: TimelineEvent[]
  content_blocks: ContentBlock[]
}

export interface ActivityImage {
  id: number
  image_url: string
  caption: string
  order: number
}

export interface Activity {
  id: number
  title: string
  description: string
  category: string | null
}

export interface ActivityDetail {
  id: number
  title: string
  description: string
  category: ActivityCategory | null
  images: ActivityImage[]
  content_blocks: ContentBlock[]
  responsible_partner: {
    id: number
    name: string
    logo_url: string | null
  } | null
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