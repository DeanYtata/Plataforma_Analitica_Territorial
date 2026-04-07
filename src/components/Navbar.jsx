export default function Navbar() {
  return (
    <nav style={styles.nav}>
      <div style={styles.logo}>🗺️ Analítica Territorial</div>
      <div style={styles.sub}>Colombia · Datos Abiertos</div>
    </nav>
  );
}
const styles = {
  nav: { display:"flex", justifyContent:"space-between", alignItems:"center", padding:"16px 32px", background:"linear-gradient(135deg, #1a3a2a, #0d2b1a)", color:"#fff", boxShadow:"0 2px 8px rgba(0,0,0,0.3)" },
  logo:{ fontSize:"1.4rem", fontWeight:"700" },
  sub: { fontSize:"0.85rem", color:"#7fc99a" },
};
