"use client";
import { useEffect, useState } from "react";
import { getEstatisticas } from "../../services/api";
import DashboardHeader from "./DashboardHeader";
import DataCard from "./DataCard";
import Charts from "./Charts";
import Filters from "./Filters";

export default function Dashboard() {
  const [dados, setDados] = useState([]);
  const [ano, setAno] = useState("2024");
  const [tema, setTema] = useState("light");

  const toggleTema = () => {
    const novo = tema === "light" ? "dark" : "light";
    setTema(novo);
    document.documentElement.setAttribute("data-theme", novo);
  };

  useEffect(() => {
    async function carregar() {
      try {
        const res = await getEstatisticas();
        const filtrados = res.data.filter((d) => d.ano === parseInt(ano));
        setDados(filtrados);
      } catch (err) {
        console.error("Erro ao carregar dados:", err);
      }
    }
    carregar();
  }, [ano]);

  return (
    <div className="dashboard">
      <DashboardHeader tema={tema} toggleTema={toggleTema} />
      <Filters ano={ano} setAno={setAno} anos={[2020, 2021, 2022, 2023, 2024]} />
      <div className="cards-grid">
        <DataCard titulo="Cursos Ativos" valor={dados.length} cor="#10b981" />
        <DataCard titulo="Ano Atual" valor={ano} cor="#2563eb" />
      </div>
      <Charts dados={dados.map((d) => ({ curso: d.curso, media_notas: d.media_notas }))} />
    </div>
  );
}
