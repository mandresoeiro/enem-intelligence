// ==========================================================
// 🎓 DashboardHeader — Cabeçalho do painel
// ==========================================================
"use client";

export default function DashboardHeader({ tema, toggleTema }) {
  return (
    <header className="header">
      <h1>📊 ENEM Data Portal</h1>
      <button onClick={toggleTema}>
        Alternar para {tema === "light" ? "🌙 Dark" : "☀️ Light"}
      </button>
    </header>
  );
}
