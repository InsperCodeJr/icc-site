import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
<<<<<<< HEAD
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
=======
import { createBrowserRouter, RouterProvider } from "react-router-dom"
>>>>>>> 6b1a5a32110e17b7231ce776cf9ff4fbdc08672e
import './index.css'

import App from './App.tsx'
<<<<<<< HEAD
import Parceiros from './pages/Parceiros'
=======
import Equipe from './pages/Equipe/index.tsx'
import PerfilMembro from './pages/PerfilMembro/index.tsx'
import Atividades from './pages/Atividades/index.tsx'
import PerfilAtividade from './pages/PerfilAtividade/index.tsx'
import Parceiros from './pages/Parceiros/index.tsx'
import PerfilParceiro from './pages/PerfilParceiro/index.tsx'
import Home from './pages/Home/index.tsx'
import Mailing from './pages/Mailing/index.tsx'
import Processo from './pages/Processo/index.tsx'
>>>>>>> 6b1a5a32110e17b7231ce776cf9ff4fbdc08672e

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
<<<<<<< HEAD
  },
  {
    path: "/parceiros",
    element: <Parceiros />,
=======
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
>>>>>>> 6b1a5a32110e17b7231ce776cf9ff4fbdc08672e
  },
])

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
