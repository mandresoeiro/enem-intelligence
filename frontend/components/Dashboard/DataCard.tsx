// ==========================================================
// 📦 DataCard — Cartão de métrica simples
// ==========================================================
export default function DataCard({ titulo, valor, cor = "#2563eb" }) {
  return (
    <div className="card" style={{ borderTop: `4px solid ${cor}` }}>
      <h3>{titulo}</h3>
      <p className="valor">{valor}</p>
    </div>
  );
}
