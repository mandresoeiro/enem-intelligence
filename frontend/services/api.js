// ==========================================================
// 🔗 ENEM Data Portal — Serviço de API (Axios)
// ==========================================================
// Centraliza as chamadas HTTP para a API Django.
// ==========================================================

import axios from "axios";

// URL base da API Django (ajuste se necessário)
const API_BASE_URL = "http://127.0.0.1:8000/api/enem/";

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// ==========================================================
// 🎯 Endpoints disponíveis
// ==========================================================

export const getAlunos = () => api.get("alunos/");
export const getCursos = () => api.get("cursos/");
export const getEstatisticas = () => api.get("estatisticas/");


// 📦 Explicação:

// axios → cliente HTTP para consumir a API Django

// recharts → biblioteca de gráficos (para estatísticas ENEM)

// sass → pré-processador CSS modular e profissional
