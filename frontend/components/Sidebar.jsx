"use client";
import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import styles from "./Sidebar.module.scss";

export default function Sidebar() {
  const [isOpen, setIsOpen] = useState(true);
  const pathname = usePathname();

  const menuItems = [
    { icon: "📊", label: "Dashboard", href: "/" },
    { icon: "🔍", label: "Buscar Aluno", href: "/buscar-aluno" },
    { icon: "👨‍🎓", label: "Alunos", href: "/alunos" },
    { icon: "📝", label: "Simulados", href: "/simulados" },
    { icon: "🎯", label: "Cursos", href: "/cursos" },
    { icon: "📈", label: "Estatísticas", href: "/estatisticas" },
    { icon: "⚙️", label: "Configurações", href: "/configuracoes" },
  ];

  return (
    <>
      <button
        className={styles.menuToggle}
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Toggle menu"
      >
        {isOpen ? "✕" : "☰"}
      </button>

      <aside className={`${styles.sidebar} ${isOpen ? styles.open : ""}`}>
        <div className={styles.logo}>
          <div className={styles.logoIcon}>🎓</div>
          <h2 className={styles.logoText}>ENEM Intelligence</h2>
        </div>

        <nav className={styles.nav}>
          {menuItems.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className={`${styles.navItem} ${
                pathname === item.href ? styles.active : ""
              }`}
            >
              <span className={styles.navIcon}>{item.icon}</span>
              <span className={styles.navLabel}>{item.label}</span>
            </Link>
          ))}
        </nav>

        <div className={styles.footer}>
          <div className={styles.user}>
            <div className={styles.userAvatar}>A</div>
            <div className={styles.userInfo}>
              <p className={styles.userName}>Admin</p>
              <p className={styles.userRole}>Administrador</p>
            </div>
          </div>
        </div>
      </aside>
    </>
  );
}
