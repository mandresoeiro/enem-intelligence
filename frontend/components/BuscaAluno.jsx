'use client';

import { useState } from 'react';
import axios from 'axios';
import styles from './BuscaAluno.module.scss';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://127.0.0.1:8001/api/enem/";

export default function BuscaAluno() {
  const [inscricao, setInscricao] = useState('');
  const [loading, setLoading] = useState(false);
  const [resultado, setResultado] = useState(null);
  const [erro, setErro] = useState(null);

  const handleInscricaoChange = (e) => {
    // Remove tudo que não é número
    const numeros = e.target.value.replace(/\D/g, '');
    setInscricao(numeros);
  };

  const buscarNotas = async (e) => {
    e.preventDefault();
    setLoading(true);
    setErro(null);
    setResultado(null);

    try {
      // Aumenta timeout para 60 segundos (busca em arquivo grande)
      const response = await axios.post(
        `${API_BASE_URL}alunos/buscar_notas_cpf/`,
        { cpf: inscricao },
        { timeout: 60000 }
      );

      setResultado(response.data);
    } catch (error) {
      if (error.code === 'ECONNABORTED') {
        setErro('A busca está demorando muito. Isso pode indicar que o arquivo é muito grande ou o número de inscrição não existe. Tente novamente mais tarde.');
      } else if (error.response?.status === 404) {
        setErro('Notas não encontradas para este número de inscrição. Verifique se está correto e se você prestou o ENEM entre 2022 e 2024.');
      } else if (error.message === 'Network Error') {
        setErro('Não foi possível conectar ao servidor. Verifique se o backend está rodando.');
      } else {
        setErro('Erro ao buscar notas. Tente novamente mais tarde.');
      }
      console.error('Erro na busca:', error);
    } finally {
      setLoading(false);
    }
  };

  const calcularMedia = (notas) => {
    const valores = [
      notas.nota_enem_matematica,
      notas.nota_enem_linguagens,
      notas.nota_enem_ciencias,
      notas.nota_enem_humanas
    ].filter(n => n !== null && n !== undefined);

    if (valores.length === 0) return 0;
    const soma = valores.reduce((acc, val) => acc + val, 0);
    return (soma / valores.length).toFixed(2);
  };

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        <h2 className={styles.titulo}>🔍 Buscar Notas do ENEM por Número de Inscrição</h2>
        <p className={styles.descricao}>
          Consulte suas notas do ENEM de 2022, 2023 ou 2024 usando seu número de inscrição.
          Não é necessário cadastro prévio!
        </p>

        <form onSubmit={buscarNotas} className={styles.formulario}>
          <div className={styles.inputGroup}>
            <label htmlFor="inscricao">Número de Inscrição</label>
            <input
              id="inscricao"
              type="text"
              value={inscricao}
              onChange={handleInscricaoChange}
              placeholder="Digite seu número de inscrição"
              maxLength="12"
              required
              className={styles.input}
            />
          </div>

          <button
            type="submit"
            disabled={loading || inscricao.length < 12}
            className={styles.botaoBuscar}
          >
            {loading ? '🔄 Buscando... (pode levar até 60s)' : '🔍 Buscar Notas'}
          </button>
        </form>

        {loading && (
          <div className={styles.info} style={{marginTop: '1rem', color: '#666'}}>
            ⏳ A busca pode demorar alguns minutos devido ao tamanho dos arquivos de microdados...
          </div>
        )}

        {erro && (
          <div className={styles.erro}>
            <span>⚠️</span>
            <p>{erro}</p>
          </div>
        )}

        {resultado && (
          <div className={styles.resultado}>
            <h3>✅ Notas Encontradas - ENEM {resultado.ano}</h3>
            <p style={{fontSize: '0.9rem', color: '#666', marginBottom: '1rem'}}>
              Inscrição: {resultado.inscricao}
            </p>

            <div className={styles.notasGrid}>
              <div className={styles.notaCard}>
                <span className={styles.materia}>📐 Matemática</span>
                <span className={styles.nota}>
                  {resultado.nota_enem_matematica?.toFixed(1) || 'N/A'}
                </span>
              </div>

              <div className={styles.notaCard}>
                <span className={styles.materia}>📚 Linguagens</span>
                <span className={styles.nota}>
                  {resultado.nota_enem_linguagens?.toFixed(1) || 'N/A'}
                </span>
              </div>

              <div className={styles.notaCard}>
                <span className={styles.materia}>🔬 Ciências da Natureza</span>
                <span className={styles.nota}>
                  {resultado.nota_enem_ciencias?.toFixed(1) || 'N/A'}
                </span>
              </div>

              <div className={styles.notaCard}>
                <span className={styles.materia}>🌍 Ciências Humanas</span>
                <span className={styles.nota}>
                  {resultado.nota_enem_humanas?.toFixed(1) || 'N/A'}
                </span>
              </div>
            </div>

            <div className={styles.media}>
              <span>📊 Média Geral:</span>
              <strong>{calcularMedia(resultado)}</strong>
            </div>

            {resultado.uf && (
              <div className={styles.info}>
                <span>📍 UF da Prova:</span>
                <strong>{resultado.uf}</strong>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
