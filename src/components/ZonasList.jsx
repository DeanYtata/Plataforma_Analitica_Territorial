const ZONAS = [
  { id:1, nombre:"Chapinero",      score:87, nivel:"Alto",  color:"#2e7d32", poblacion:"132.120"   },
  { id:2, nombre:"Usaquén",        score:82, nivel:"Alto",  color:"#2e7d32", poblacion:"494.066"   },
  { id:3, nombre:"Suba",           score:71, nivel:"Medio", color:"#e6a817", poblacion:"1.287.001" },
  { id:4, nombre:"Kennedy",        score:65, nivel:"Medio", color:"#e6a817", poblacion:"1.161.248" },
  { id:5, nombre:"Ciudad Bolívar", score:48, nivel:"Bajo",  color:"#c62828", poblacion:"764.167"   },
];
export default function ZonasList() {
  return (
    <div style={s.card}>
      <h2 style={s.titulo}>📊 Ranking de Zonas Territoriales</h2>
      <p style={s.desc}>Ordenadas por score de oportunidad (mayor a menor)</p>
      <div style={s.header}><span>#</span><span>Zona</span><span>Población</span><span>Score</span><span>Nivel</span></div>
      {ZONAS.map((z,i) => (
        <div key={z.id} style={s.fila}>
          <span style={s.rank}>#{i+1}</span>
          <span style={s.nombre}>{z.nombre}</span>
          <span style={s.dato}>{z.poblacion}</span>
          <span style={s.barraWrap}>
            <div style={{...s.barra, width:`${z.score}%`, background:z.color}} />
            <span style={s.scoreNum}>{z.score}</span>
          </span>
          <span style={{...s.badge, background:z.color+"22", color:z.color}}>{z.nivel}</span>
        </div>
      ))}
    </div>
  );
}
const s = {
  card:    { background:"#fff", borderRadius:"12px", padding:"28px", boxShadow:"0 4px 16px rgba(0,0,0,0.08)" },
  titulo:  { margin:"0 0 8px", color:"#1a3a2a", fontSize:"1.2rem" },
  desc:    { color:"#666", margin:"0 0 20px", fontSize:"0.9rem" },
  header:  { display:"grid", gridTemplateColumns:"40px 1fr 1fr 160px 80px", gap:"12px", padding:"8px 12px", background:"#f0f4f0", borderRadius:"8px", fontWeight:"700", fontSize:"0.78rem", color:"#1a3a2a", textTransform:"uppercase", marginBottom:"8px" },
  fila:    { display:"grid", gridTemplateColumns:"40px 1fr 1fr 160px 80px", gap:"12px", padding:"12px", borderRadius:"8px", alignItems:"center", background:"#fafafa", border:"1px solid #eee", marginBottom:"6px", fontSize:"0.9rem" },
  rank:    { fontWeight:"700", color:"#999" },
  nombre:  { fontWeight:"600", color:"#222" },
  dato:    { color:"#555" },
  barraWrap:{ position:"relative", height:"20px", background:"#eee", borderRadius:"10px", overflow:"hidden", display:"flex", alignItems:"center" },
  barra:   { position:"absolute", left:0, top:0, height:"100%", borderRadius:"10px" },
  scoreNum:{ position:"relative", zIndex:1, fontSize:"0.75rem", fontWeight:"700", color:"#fff", paddingLeft:"6px" },
  badge:   { display:"inline-block", padding:"3px 10px", borderRadius:"20px", fontSize:"0.78rem", fontWeight:"600" },
};
