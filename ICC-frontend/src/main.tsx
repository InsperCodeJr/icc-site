import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import './index.css'
import App from './App.tsx'
import Parceiros from './pages/Parceiros'

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/parceiros",
    element: <Parceiros />,
  },
])

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)