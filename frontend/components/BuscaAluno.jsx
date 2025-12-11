'use client';

import { useState } from 'react';
import axios from 'axios';
import styles from './BuscaAluno.module.scss';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://127.0.0.1:8001/api/enem/";

export default function BuscaAluno() {
  const [cpf, setCpf] = useState('');
  const [loading, setLoading] = useState(false);
  const [resultado, setResultado] = useState(null);
  const [erro, setErro] = useState(null);

  const formatarCPF = (valor) => {
    // Remove tudo que não é número
    const numeros = valor.replace(/\D/g, '');

    // Aplica máscara XXX.XXX.XXX-XX
    if (numeros.length <= 11) {
      return numeros
        .replace(/(\d{3})(\d)/, '$1.$2')
        .replace(/(\d{3})(\d)/, '$1.$2')
        .replace(/(\d{3})(\d{1,2})$/, '$1-$2');
    }
    return numeros.slice(0, 11);
  };

  const handleCpfChange = (e) => {
    const valorFormatado = formatarCPF(e.target.value);
    setCpf(valorFormatado);
  };

  const buscarNotas = async (e) => {
    e.preventDefault();
    setLoading(true);
    setErro(null);
    setResultado(null);

    try {
      const cpfLimpo = cpf.replace(/\D/g, '');
      
      // Aumenta timeout para 60 segundos (busca em arquivo grande)
      const response = await axios.post(
        `${API_BASE_URL}alunos/buscar_notas_cpf/`,
        { cpf: cpfLimpo },
        { timeout: 60000 } // 60 segundos
      );

      setResultado(response.data);
    } catch (error) {
      if (error.code === 'ECONNABORTED') {
        setErro('A busca está demorando muito. Isso pode indicar que o arquivo é muito grande ou o CPF não existe. Tente novamente mais tarde.');
      } else if (error.response?.status === 404) {
        setErro('Notas não encontradas para este CPF. Verifique se o CPF está correto e se você prestou o ENEM entre 2022 e 2024.');
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
        <h2 className={styles.titulo}>🔍 Buscar Notas do ENEM por CPF</h2>
        <p className={styles.descricao}>
          Consulte suas notas do ENEM de 2022, 2023 ou 2024 usando seu CPF.
          Não é necessário cadastro prévio!
        </p>

        <form onSubmit={buscarNotas} className={styles.formulario}>
          <div className={styles.inputGroup}>
            <label htmlFor="cpf">CPF</label>
            <input
              id="cpf"
              type="text"
              value={cpf}
              onChange={handleCpfChange}
              placeholder="000.000.000-00"
              maxLength="14"
              required
              className={styles.input}
            />
          </div>

          <button
            type="submit"
            disabled={loading || cpf.replace(/\D/g, '').length !== 11}
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
