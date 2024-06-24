import React from 'react';
import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register"; // Importa el componente Register
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} /> {/* Ruta existente para LoginPanel */}
      <Route path="/register" element={<Register />} /> {/* Nueva ruta para Register */}
    </Routes>
  );
}

export default App;
