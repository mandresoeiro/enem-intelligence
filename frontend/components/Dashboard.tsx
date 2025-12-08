// ==========================================================
// 📊 Dashboard ENEM Data Portal
// ==========================================================
// Exibe estatísticas e gráficos básicos do ENEM
// ==========================================================

"use client";
import { useEffect, useState } from "react";
import { getEstatisticas } from "../services/api";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import styles from "./Dashboard.module.scss";

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
    <div className={styles.dashboard}>
      <div className={styles.header}>
        <h1 className={styles.title}>📊 Estatísticas ENEM</h1>
      </div>

      <div className={styles.cardGrid}>
        <div className={styles.card}>
          <h2 className={styles.cardTitle}>Média das Notas</h2>
          <div className={styles.cardValue}>—</div>
        </div>
      </div>

      <h2 className={styles.sectionTitle}>Evolução por Ano</h2>
      <div className={styles.rechartsWrapper}>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={dados}>
            <XAxis dataKey="ano" stroke="#94a3b8" />
            <YAxis stroke="#94a3b8" />
            <Tooltip />
            <Bar dataKey="media_notas" fill="#0ea5e9" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
