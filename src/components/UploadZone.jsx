import { useState } from "react";
export default function UploadZone({ onSuccess }) {
  const [archivo, setArchivo] = useState(null);
  const [estado,  setEstado]  = useState("idle");
  const [mensaje, setMensaje] = useState("");
  const handleFile = (e) => { setArchivo(e.target.files[0]); setEstado("idle"); setMensaje(""); };
  const handleUpload = async () => {
    if (!archivo) { setEstado("error"); setMensaje("⚠️ Selecciona un archivo CSV primero."); return; }
    setEstado("cargando"); setMensaje("Procesando dataset...");
    await new Promise((r) => setTimeout(r, 1500));
    setEstado("exito"); setMensaje(`✅ Dataset "${archivo.name}" cargado exitosamente. Se registraron 5 zonas.`);
    if (onSuccess) onSuccess(archivo.name);
  };
  const color = { idle:"#555", cargando:"#e6a817", exito:"#2e7d32", error:"#c62828" };
  return (
    <div style={s.card}>
      <h2 style={s.titulo}>📂 Cargar Dataset Territorial</h2>
      <p style={s.desc}>Sube un archivo CSV con datos de zonas geográficas.</p>
      <label style={s.label}>
        <input type="file" accept=".csv" onChange={handleFile} style={{ display:"none" }} />
        {archivo ? `📄 ${archivo.name}` : "Seleccionar archivo CSV..."}
      </label>
      <button onClick={handleUpload} disabled={estado==="cargando"} style={{...s.btn, opacity:estado==="cargando"?0.7:1}}>
        {estado==="cargando" ? "⏳ Cargando..." : "⬆️ Subir Archivo"}
      </button>
      {mensaje && <div style={{...s.msg, color:color[estado], borderColor:color[estado]}}>{mensaje}</div>}
    </div>
  );
}
const s = {
  card: { background:"#fff", borderRadius:"12px", padding:"28px", boxShadow:"0 4px 16px rgba(0,0,0,0.08)", marginBottom:"24px" },
  titulo:{ margin:"0 0 8px", color:"#1a3a2a", fontSize:"1.2rem" },
  desc: { color:"#666", margin:"0 0 20px", fontSize:"0.9rem" },
  label:{ display:"block", padding:"12px 20px", background:"#f0f4f0", border:"2px dashed #4caf50", borderRadius:"8px", cursor:"pointer", textAlign:"center", marginBottom:"16px", fontSize:"0.9rem" },
  btn:  { display:"block", width:"100%", padding:"12px", background:"linear-gradient(135deg,#2e7d32,#4caf50)", color:"#fff", border:"none", borderRadius:"8px", fontSize:"1rem", fontWeight:"600", cursor:"pointer", marginBottom:"16px" },
  msg:  { padding:"12px 16px", borderRadius:"8px", border:"1px solid", fontSize:"0.9rem", background:"#fafafa" },
};
