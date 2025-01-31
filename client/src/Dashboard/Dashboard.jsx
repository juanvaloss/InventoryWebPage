import React from "react";

const Dashboard = () => {
  return (
    <div className="dashboard-container">
      <h1 className="dashboard-title">Refacciones Avalos</h1>
      <div className="buttons-container">
        <button className="dashboard-button">Consultar Catálogo</button>
        <button className="dashboard-button">Consultar Inventario</button>
        <button className="dashboard-button">Agregar Carga al Inventario</button>
        <button className="dashboard-button">Consultar Garantías</button>
        <button className="dashboard-button">Consultar Productos Apartados</button>
      </div>
    </div>
  );
};

export default Dashboard;
