// ==========================================================
// 🎚️ Filters — Filtros globais (ano, curso, UF)
// ==========================================================
export default function Filters({ ano, setAno, anos }) {
  return (
    <div className="filters">
      <label>
        Ano:
        <select value={ano} onChange={(e) => setAno(e.target.value)}>
          {anos.map((a) => (
            <option key={a} value={a}>{a}</option>
          ))}
        </select>
      </label>
    </div>
  );
}
