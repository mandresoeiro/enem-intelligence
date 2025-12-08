"use client";
import Sidebar from "./Sidebar";
import styles from "./Layout.module.scss";

export default function Layout({ children }) {
  return (
    <div className={styles.layoutWrapper}>
      <Sidebar />
      <main className={styles.mainContent}>{children}</main>
    </div>
  );
}
