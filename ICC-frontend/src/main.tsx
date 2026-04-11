import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./index.css";
import App from "./App.tsx";
import Equipe from "./pages/Equipe";
import EquipeDetalhe from "./pages/PerfilMembro";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/equipe",
    element: (
      <>
        <App />
        <Equipe />
      </>
    ),
  },
  {
    path: "/equipe/:slug",
    element: (
      <>
        <App />
        <EquipeDetalhe />
      </>
    ),
  },
]);

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);