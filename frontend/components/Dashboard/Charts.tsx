// ==========================================================
// 📊 Charts — Visualização das médias por curso
// ==========================================================
"use client";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function Charts({ dados }) {
  return (
    <div className="card">
      <h3>Médias por Curso</h3>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={dados}>
          <XAxis dataKey="curso" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="media_notas" fill="#2563eb" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
