// ==========================================================
// 📊 Dashboard ENEM Data Portal
// ==========================================================
// Exibe estatísticas e gráficos básicos do ENEM
// ==========================================================

"use client";
import { useEffect, useState } from "react";
import { getEstatisticas } from "../services/api";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function Dashboard() {
  const [dados, setDados] = useState([]);

  useEffect(() => {
    async function carregar() {
      try {
        const res = await getEstatisticas();
        setDados(res.data);
      } catch (error) {
        console.error("Erro ao carregar dados:", error);
      }
    }
    carregar();
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">📊 Estatísticas ENEM</h1>

      <div className="bg-white rounded-xl shadow p-4">
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={dados}>
            <XAxis dataKey="ano" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="media_notas" fill="#2563eb" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
