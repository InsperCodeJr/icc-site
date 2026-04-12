import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from "react-router-dom"
import './index.css'

import App from './App.tsx'
import Equipe from './pages/Equipe/index.tsx'
import PerfilMembro from './pages/PerfilMembro/index.tsx'
import Atividades from './pages/Atividades/index.tsx'
import PerfilAtividade from './pages/PerfilAtividade/index.tsx'
import Parceiros from './pages/Parceiros/index.tsx'
import PerfilParceiro from './pages/PerfilParceiro/index.tsx'
import Home from './pages/Home/index.tsx'
import Mailing from './pages/Mailing/index.tsx'
import Processo from './pages/Processo/index.tsx'

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      { index: true, element: <Home /> },
      { path: "equipe", element: <Equipe /> },
      { path: "equipe/:id", element: <PerfilMembro /> },
      { path: "atividades", element: <Atividades /> },
      { path: "atividades/:id", element: <PerfilAtividade /> },
      { path: "parceiros", element: <Parceiros /> },
      { path: "parceiros/:id", element: <PerfilParceiro /> },
      { path: "mailing", element: <Mailing /> },
      { path: "processo", element: <Processo /> },
    ],
  },
])

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
