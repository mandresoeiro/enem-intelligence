import { useEffect, useState } from "react";
import styles from "./Dashboard.module.scss";

export default function DashboardStatus() {
  const [alunos, setAlunos] = useState([]);
  const [simulados, setSimulados] = useState([]);
  const [estados, setEstados] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchAll() {
      try {
        const [alunosRes, simuladosRes, estadosRes] = await Promise.all([
          fetch("http://127.0.0.1:8000/api/enem/alunos/").then((r) => r.json()),
          fetch("http://127.0.0.1:8000/api/enem/simulados/").then((r) =>
            r.json()
          ),
          fetch("http://127.0.0.1:8000/api/enem/estatisticas-estado/").then(
            (r) => r.json()
          ),
        ]);
        setAlunos(alunosRes);
        setSimulados(simuladosRes);
        setEstados(estadosRes);
      } catch (err) {
        setError("Erro ao buscar dados do backend");
      } finally {
        setLoading(false);
      }
    }
    fetchAll();
  }, []);

  // Contadores
  const alunosComNotaEnem = alunos.filter(
    (a) =>
      a.nota_enem_matematica ||
      a.nota_enem_linguagens ||
      a.nota_enem_ciencias ||
      a.nota_enem_humanas
  ).length;

  return (
    <div className={styles.cardGrid}>
      <div className={styles.card}>
        <h2 className={styles.cardTitle}>Alunos cadastrados</h2>
        <div className={styles.cardValue}>{alunos.length}</div>
        <div className={styles.textMuted}>
          Com nota ENEM: {alunosComNotaEnem}
        </div>
      </div>
      <div className={styles.card}>
        <h2 className={styles.cardTitle}>Simulados registrados</h2>
        <div className={styles.cardValue}>{simulados.length}</div>
      </div>
      <div className={styles.card}>
        <h2 className={styles.cardTitle}>Estados com estatísticas</h2>
        <div className={styles.cardValue}>
          {[...new Set(estados.map((e) => e.estado))].length}
        </div>
      </div>
      {error && (
        <div className={styles.card} style={{ color: "#e11d48" }}>
          <h2 className={styles.cardTitle}>Erro</h2>
          <div>{error}</div>
        </div>
      )}
      {loading && (
        <div className={styles.card}>
          <h2 className={styles.cardTitle}>Carregando dados...</h2>
        </div>
      )}
    </div>
  );
}
