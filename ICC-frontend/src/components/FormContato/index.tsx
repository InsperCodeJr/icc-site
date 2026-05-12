import { useState } from "react";
import "./index.css";

export default function FormContato() {
  const [contactType, setContactType] = useState("");
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");

  return (
    <form method="post" className="contato">
      <section className="campo">
        <label htmlFor="nome">Nome *</label>
        <input
          type="text"
          placeholder="Nome completo"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
        />
      </section>
      <section className="campo">
        <label htmlFor="tel-num">Telefone *</label>
        <input
          type="text"
          placeholder="(11) 91234-5678"
          name="tel-num"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
        />
      </section>
      <section className="campo">
        <label htmlFor="email">E-mail *</label>
        <input
          type="email"
          placeholder="ex.emplo@email.com"
          name="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </section>
      <section className="campo">
        <label htmlFor="tipo-contato">Você é: *</label>
        <select
          id="tipo-contato"
          name="tipo-contato"
          value={contactType}
          onChange={(e) => setContactType(e.target.value)}
        >
          <option value="">Ecolha uma opcao</option>
          <option value="aluno">Aluno do Insper</option>
          <option value="empresa">Empresa</option>
        </select>
      </section>
      <section className="campo">
        <button type="submit">Enviar</button>
      </section>
    </form>
  );
}
