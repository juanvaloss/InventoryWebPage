import Dashboard from './Dashboard/Dashboard'
import { Routes, Route } from 'react-router';


function App() {

  return (
    <Routes>

      <Route path="/" element={<Dashboard/>} />

    </Routes>
  );
}

export default App


