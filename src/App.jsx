import Navbar    from "./components/Navbar";
import Dashboard from "./pages/Dashboard";
export default function App() {
  return (
    <div style={{ background:"#f4f7f4", minHeight:"100vh", fontFamily:"Segoe UI, sans-serif" }}>
      <Navbar />
      <Dashboard />
    </div>
  );
}
