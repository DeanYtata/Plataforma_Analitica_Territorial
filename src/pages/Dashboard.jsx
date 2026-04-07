import { useState } from "react";
import UploadZone from "../components/UploadZone";
import ZonasList  from "../components/ZonasList";
export default function Dashboard() {
  const [ultimaCarga, setUltimaCarga] = useState(null);
  return (
    <main style={s.main}>
      <div style={s.stats}>
        {[
          { icon:"📍", val:"5",               label:"Zonas analizadas" },
          { icon:"📂", val:ultimaCarga ?? "—", label:"Dataset activo"   },
          { icon:"📈", val:"70.6",             label:"Score promedio"   },
        ].map((c) => (
          <div key={c.label} style={s.card}>
            <span style={s.icon}>{c.icon}</span>
            <div><div style={s.val}>{c.val}</div><div style={s.lbl}>{c.label}</div></div>
          </div>
        ))}
      </div>
      <UploadZone onSuccess={setUltimaCarga} />
      <ZonasList />
    </main>
  );
}
const s = {
  main: { maxWidth:"1100px", margin:"0 auto", padding:"32px 24px" },
  stats:{ display:"grid", gridTemplateColumns:"repeat(3,1fr)", gap:"16px", marginBottom:"24px" },
  card: { background:"#fff", borderRadius:"12px", padding:"20px", display:"flex", alignItems:"center", gap:"16px", boxShadow:"0 2px 8px rgba(0,0,0,0.07)", border:"1px solid #e8f5e9" },
  icon: { fontSize:"2rem" },
  val:  { fontSize:"1.3rem", fontWeight:"700", color:"#1a3a2a", maxWidth:"180px", overflow:"hidden", textOverflow:"ellipsis", whiteSpace:"nowrap" },
  lbl:  { fontSize:"0.8rem", color:"#888", marginTop:"2px" },
};
