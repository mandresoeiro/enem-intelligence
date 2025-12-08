"use client";
import { useEffect, useState } from "react";
import axios from "axios";
import styles from "./DashboardModerno.module.scss";

export default function DashboardModerno() {
  const [alunos, setAlunos] = useState([]);
  const [estatisticas, setEstatisticas] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function carregarDados() {
      try {
        const [alunosRes, statsRes] = await Promise.all([
          axios.get("http://localhost:8000/api/enem/alunos/"),
          axios.get("http://localhost:8000/api/enem/estatisticas-estado/"),
        ]);
        setAlunos(alunosRes.data);
        setEstatisticas(statsRes.data);
      } catch (error) {
        console.error("Erro ao carregar dados:", error);
      } finally {
        setLoading(false);
      }
    }
    carregarDados();
  }, []);

  const calcularMedia = (aluno) => {
    const notas = [
      parseFloat(aluno.nota_enem_matematica || 0),
      parseFloat(aluno.nota_enem_linguagens || 0),
      parseFloat(aluno.nota_enem_ciencias || 0),
      parseFloat(aluno.nota_enem_humanas || 0),
    ];
    const soma = notas.reduce((acc, nota) => acc + nota, 0);
    return (soma / 4).toFixed(2);
  };

  const getMediaEstado = (area, uf) => {
    const stat = estatisticas.find((s) => s.area === area && s.estado === uf);
    return stat ? parseFloat(stat.media_nota).toFixed(2) : "N/A";
  };

  if (loading) {
    return (
      <div className={styles.loading}>
        <div className={styles.spinner}></div>
        <p>Carregando dados...</p>
      </div>
    );
  }

  return (
    <div className={styles.container}>
      {/* Header */}
      <header className={styles.header}>
        <div className={styles.headerContent}>
          <h1 className={styles.title}>🎓 ENEM Intelligence</h1>
          <p className={styles.subtitle}>
            Análise de Desempenho e Estatísticas do ENEM 2024
          </p>
        </div>
      </header>

      {/* Stats Cards */}
      <div className={styles.statsGrid}>
        <div className={styles.statCard}>
          <div className={styles.statIcon}>👨‍🎓</div>
          <div className={styles.statContent}>
            <p className={styles.statLabel}>Total de Alunos</p>
            <h3 className={styles.statValue}>{alunos.length}</h3>
          </div>
        </div>

        <div className={styles.statCard}>
          <div className={styles.statIcon}>📊</div>
          <div className={styles.statContent}>
            <p className={styles.statLabel}>Estados Analisados</p>
            <h3 className={styles.statValue}>
              {[...new Set(estatisticas.map((s) => s.estado))].length}
            </h3>
          </div>
        </div>

        <div className={styles.statCard}>
          <div className={styles.statIcon}>📝</div>
          <div className={styles.statContent}>
            <p className={styles.statLabel}>Áreas Avaliadas</p>
            <h3 className={styles.statValue}>4</h3>
          </div>
        </div>

        <div className={styles.statCard}>
          <div className={styles.statIcon}>🎯</div>
          <div className={styles.statContent}>
            <p className={styles.statLabel}>Média Geral</p>
            <h3 className={styles.statValue}>
              {alunos.length > 0
                ? (
                    alunos.reduce(
                      (acc, aluno) => acc + parseFloat(calcularMedia(aluno)),
                      0
                    ) / alunos.length
                  ).toFixed(2)
                : "0"}
            </h3>
          </div>
        </div>
      </div>

      {/* Alunos Cards */}
      <section className={styles.section}>
        <h2 className={styles.sectionTitle}>📋 Desempenho dos Alunos</h2>
        <div className={styles.alunosGrid}>
          {alunos.map((aluno) => (
            <div key={aluno.id} className={styles.alunoCard}>
              <div className={styles.alunoHeader}>
                <div className={styles.alunoAvatar}>
                  {aluno.nome.charAt(0).toUpperCase()}
                </div>
                <div className={styles.alunoInfo}>
                  <h3 className={styles.alunoNome}>{aluno.nome}</h3>
                  <p className={styles.alunoUf}>📍 {aluno.uf}</p>
                </div>
                <div className={styles.mediaGeral}>
                  <span className={styles.mediaLabel}>Média</span>
                  <span className={styles.mediaValor}>
                    {calcularMedia(aluno)}
                  </span>
                </div>
              </div>

              <div className={styles.notasGrid}>
                <div className={styles.notaItem}>
                  <span className={styles.notaIcone}>🔢</span>
                  <div className={styles.notaDetalhes}>
                    <p className={styles.notaTitulo}>Matemática</p>
                    <p className={styles.notaValor}>
                      {parseFloat(aluno.nota_enem_matematica || 0).toFixed(2)}
                    </p>
                    <p className={styles.notaComparacao}>
                      Estado: {getMediaEstado("matematica", aluno.uf)}
                    </p>
                  </div>
                </div>

                <div className={styles.notaItem}>
                  <span className={styles.notaIcone}>📚</span>
                  <div className={styles.notaDetalhes}>
                    <p className={styles.notaTitulo}>Linguagens</p>
                    <p className={styles.notaValor}>
                      {parseFloat(aluno.nota_enem_linguagens || 0).toFixed(2)}
                    </p>
                    <p className={styles.notaComparacao}>
                      Estado: {getMediaEstado("linguagens", aluno.uf)}
                    </p>
                  </div>
                </div>

                <div className={styles.notaItem}>
                  <span className={styles.notaIcone}>🔬</span>
                  <div className={styles.notaDetalhes}>
                    <p className={styles.notaTitulo}>Ciências</p>
                    <p className={styles.notaValor}>
                      {parseFloat(aluno.nota_enem_ciencias || 0).toFixed(2)}
                    </p>
                    <p className={styles.notaComparacao}>
                      Estado: {getMediaEstado("ciencias", aluno.uf)}
                    </p>
                  </div>
                </div>

                <div className={styles.notaItem}>
                  <span className={styles.notaIcone}>🌍</span>
                  <div className={styles.notaDetalhes}>
                    <p className={styles.notaTitulo}>Humanas</p>
                    <p className={styles.notaValor}>
                      {parseFloat(aluno.nota_enem_humanas || 0).toFixed(2)}
                    </p>
                    <p className={styles.notaComparacao}>
                      Estado: {getMediaEstado("humanas", aluno.uf)}
                    </p>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer className={styles.footer}>
        <p>© 2024 ENEM Intelligence - Análise de Desempenho Acadêmico</p>
      </footer>
    </div>
  );
}
