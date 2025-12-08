"use client";
import { useEffect, useState } from "react";
import axios from "axios";
import Layout from "@/components/Layout";
import styles from "./alunos.module.scss";

export default function AlunosPage() {
  const [alunos, setAlunos] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [loading, setLoading] = useState(true);
  const [formData, setFormData] = useState({
    nome: "",
    cpf: "",
    uf: "",
    nota_enem_matematica: "",
    nota_enem_linguagens: "",
    nota_enem_ciencias: "",
    nota_enem_humanas: "",
  });
  const [buscandoNotas, setBuscandoNotas] = useState(false);

  useEffect(() => {
    carregarAlunos();
  }, []);

  const buscarNotasPorCPF = async (cpf) => {
    if (cpf.length >= 11) {
      setBuscandoNotas(true);
      try {
        const response = await axios.post(
          "http://localhost:8000/api/enem/alunos/buscar_notas_cpf/",
          { cpf }
        );
        if (response.data) {
          setFormData((prev) => ({
            ...prev,
            nota_enem_matematica: response.data.nota_enem_matematica || "",
            nota_enem_linguagens: response.data.nota_enem_linguagens || "",
            nota_enem_ciencias: response.data.nota_enem_ciencias || "",
            nota_enem_humanas: response.data.nota_enem_humanas || "",
            uf: response.data.uf || prev.uf,
          }));
          alert(
            "✅ Notas encontradas nos microdados e preenchidas automaticamente!"
          );
        }
      } catch (error) {
        if (error.response?.status === 404) {
          alert(
            "ℹ️ Notas não encontradas nos microdados. Preencha manualmente."
          );
        } else {
          console.error("Erro ao buscar notas:", error);
        }
      } finally {
        setBuscandoNotas(false);
      }
    }
  };

  const carregarAlunos = async () => {
    try {
      const response = await axios.get(
        "http://localhost:8000/api/enem/alunos/"
      );
      setAlunos(response.data);
    } catch (error) {
      console.error("Erro ao carregar alunos:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("http://localhost:8000/api/enem/alunos/", formData);
      setShowForm(false);
      setFormData({
        nome: "",
        cpf: "",
        uf: "",
        nota_enem_matematica: "",
        nota_enem_linguagens: "",
        nota_enem_ciencias: "",
        nota_enem_humanas: "",
      });
      carregarAlunos();
      alert("Aluno cadastrado com sucesso!");
    } catch (error) {
      console.error("Erro ao cadastrar aluno:", error);
      alert("Erro ao cadastrar aluno. Verifique os dados.");
    }
  };

  const handleDelete = async (id) => {
    if (confirm("Tem certeza que deseja excluir este aluno?")) {
      try {
        await axios.delete(`http://localhost:8000/api/enem/alunos/${id}/`);
        carregarAlunos();
        alert("Aluno excluído com sucesso!");
      } catch (error) {
        console.error("Erro ao excluir aluno:", error);
        alert("Erro ao excluir aluno.");
      }
    }
  };

  if (loading) {
    return (
      <Layout>
        <div className={styles.loading}>Carregando...</div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className={styles.container}>
        <div className={styles.header}>
          <div>
            <h1 className={styles.title}>👨‍🎓 Gerenciar Alunos</h1>
            <p className={styles.subtitle}>
              Cadastre e gerencie os alunos do sistema
            </p>
          </div>
          <button
            className={styles.btnPrimary}
            onClick={() => setShowForm(!showForm)}
          >
            {showForm ? "✕ Cancelar" : "+ Novo Aluno"}
          </button>
        </div>

        {showForm && (
          <div className={styles.formCard}>
            <h2 className={styles.formTitle}>📝 Cadastrar Novo Aluno</h2>
            <form onSubmit={handleSubmit} className={styles.form}>
              <div className={styles.formRow}>
                <div className={styles.formGroup}>
                  <label className={styles.label}>Nome Completo *</label>
                  <input
                    type="text"
                    className={styles.input}
                    value={formData.nome}
                    onChange={(e) =>
                      setFormData({ ...formData, nome: e.target.value })
                    }
                    required
                    placeholder="Ex: João Silva"
                  />
                </div>
                <div className={styles.formGroup}>
                  <label className={styles.label}>
                    CPF * {buscandoNotas && "🔍 Buscando notas..."}
                  </label>
                  <input
                    type="text"
                    className={styles.input}
                    value={formData.cpf}
                    onChange={(e) => {
                      const cpf = e.target.value;
                      setFormData({ ...formData, cpf });
                      if (cpf.length === 11) {
                        buscarNotasPorCPF(cpf);
                      }
                    }}
                    required
                    placeholder="Ex: 12345678901"
                    maxLength={11}
                  />
                  <small style={{ color: "#64748b", fontSize: "0.8rem" }}>
                    As notas serão buscadas automaticamente nos microdados
                  </small>
                </div>
                <div className={styles.formGroup}>
                  <label className={styles.label}>UF *</label>
                  <input
                    type="text"
                    className={styles.input}
                    value={formData.uf}
                    onChange={(e) =>
                      setFormData({
                        ...formData,
                        uf: e.target.value.toUpperCase(),
                      })
                    }
                    required
                    maxLength={2}
                    placeholder="Ex: SP"
                  />
                </div>
              </div>

              <h3 className={styles.sectionTitle}>📊 Notas do ENEM</h3>
              <div className={styles.formRow}>
                <div className={styles.formGroup}>
                  <label className={styles.label}>🔢 Matemática</label>
                  <input
                    type="number"
                    step="0.01"
                    className={styles.input}
                    value={formData.nota_enem_matematica}
                    onChange={(e) =>
                      setFormData({
                        ...formData,
                        nota_enem_matematica: e.target.value,
                      })
                    }
                    placeholder="Ex: 650.50"
                  />
                </div>
                <div className={styles.formGroup}>
                  <label className={styles.label}>📚 Linguagens</label>
                  <input
                    type="number"
                    step="0.01"
                    className={styles.input}
                    value={formData.nota_enem_linguagens}
                    onChange={(e) =>
                      setFormData({
                        ...formData,
                        nota_enem_linguagens: e.target.value,
                      })
                    }
                    placeholder="Ex: 720.30"
                  />
                </div>
                <div className={styles.formGroup}>
                  <label className={styles.label}>🔬 Ciências</label>
                  <input
                    type="number"
                    step="0.01"
                    className={styles.input}
                    value={formData.nota_enem_ciencias}
                    onChange={(e) =>
                      setFormData({
                        ...formData,
                        nota_enem_ciencias: e.target.value,
                      })
                    }
                    placeholder="Ex: 680.75"
                  />
                </div>
                <div className={styles.formGroup}>
                  <label className={styles.label}>🌍 Humanas</label>
                  <input
                    type="number"
                    step="0.01"
                    className={styles.input}
                    value={formData.nota_enem_humanas}
                    onChange={(e) =>
                      setFormData({
                        ...formData,
                        nota_enem_humanas: e.target.value,
                      })
                    }
                    placeholder="Ex: 700.00"
                  />
                </div>
              </div>

              <div className={styles.formActions}>
                <button type="submit" className={styles.btnSubmit}>
                  ✓ Cadastrar Aluno
                </button>
              </div>
            </form>
          </div>
        )}

        <div className={styles.tableCard}>
          <div className={styles.tableHeader}>
            <h2 className={styles.tableTitle}>📋 Lista de Alunos</h2>
            <span className={styles.badge}>{alunos.length} alunos</span>
          </div>
          <div className={styles.tableWrapper}>
            <table className={styles.table}>
              <thead>
                <tr>
                  <th>Nome</th>
                  <th>CPF</th>
                  <th>UF</th>
                  <th>Matemática</th>
                  <th>Linguagens</th>
                  <th>Ciências</th>
                  <th>Humanas</th>
                  <th>Ações</th>
                </tr>
              </thead>
              <tbody>
                {alunos.map((aluno) => (
                  <tr key={aluno.id}>
                    <td className={styles.cellNome}>
                      <div className={styles.avatar}>
                        {aluno.nome.charAt(0).toUpperCase()}
                      </div>
                      {aluno.nome}
                    </td>
                    <td>{aluno.cpf}</td>
                    <td>
                      <span className={styles.ufBadge}>{aluno.uf}</span>
                    </td>
                    <td>
                      {parseFloat(aluno.nota_enem_matematica || 0).toFixed(2)}
                    </td>
                    <td>
                      {parseFloat(aluno.nota_enem_linguagens || 0).toFixed(2)}
                    </td>
                    <td>
                      {parseFloat(aluno.nota_enem_ciencias || 0).toFixed(2)}
                    </td>
                    <td>
                      {parseFloat(aluno.nota_enem_humanas || 0).toFixed(2)}
                    </td>
                    <td>
                      <button
                        className={styles.btnDelete}
                        onClick={() => handleDelete(aluno.id)}
                      >
                        🗑️
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </Layout>
  );
}
