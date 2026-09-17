import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import './index.css'
import App from './App.tsx'
import Equipe from './pages/Equipe/index.tsx'
import PerfilMembro from './pages/PerfilMembro/index.tsx'
import Atividades from './pages/Atividades/index.tsx'
import CategoriaAtividade from './pages/CategoriaAtividade/index.tsx'
import PerfilAtividade from './pages/PerfilAtividade/index.tsx'
import PerfilAtividadeItem from './pages/PerfilAtividadeItem/index.tsx'
import Parceiros from './pages/Parceiros/index.tsx'
import PerfilParceiro from './pages/PerfilParceiro/index.tsx'
import Projetos from './pages/Projetos/index.tsx'
import ProjetoDetalhe from './pages/ProjetoDetalhe/index.tsx'
import Home from './pages/Home/index.tsx'
import Processo from './pages/Processo/index.tsx'
import Noticias from './pages/Noticias/index.tsx'
import Contato from './pages/Contato/index.tsx'
import NaoEncontrada from './pages/NaoEncontrada/index.tsx'

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      { index: true, element: <Home /> },
      { path: "equipe", element: <Equipe /> },
      { path: "equipe/:id", element: <PerfilMembro /> },
      { path: "atividades", element: <Atividades /> },
      { path: "atividades/categoria/:categoria", element: <CategoriaAtividade /> },
      { path: "atividades/:id", element: <PerfilAtividade /> },
      { path: "atividades/item/:id", element: <PerfilAtividadeItem /> },
      { path: "parceiros", element: <Parceiros /> },
      { path: "parceiros/:id", element: <PerfilParceiro /> },
      { path: "projetos", element: <Projetos /> },
      { path: "projetos/:slug", element: <ProjetoDetalhe /> },
      { path: "processo", element: <Processo /> },
      { path: "news", element: <Noticias /> },
      { path: "contato", element: <Contato /> },
      { path: "*", element: <NaoEncontrada /> },
    ],
  },
])

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)