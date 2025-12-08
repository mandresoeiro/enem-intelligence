// ==========================================================
// 🧩 Tipos Globais — ENEM Data Portal
// ==========================================================

export interface Estatistica {
  id: number;
  curso: string;
  ano: number;
  media_notas: number;
  total_inscritos: number;
}

export interface DataCardProps {
  titulo: string;
  valor: string | number;
  cor?: string;
}

export interface FiltersProps {
  ano: string;
  setAno: (ano: string) => void;
  anos: number[];
}

export interface DashboardHeaderProps {
  tema: "light" | "dark";
  toggleTema: () => void;
}

export interface ChartsProps {
  dados: Estatistica[];
}
