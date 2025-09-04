import { useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  // Appel API au chargement du composant
  useEffect(() => {
    axios.get("http://backend-service:8080/")
      .then(response => console.log("Réponse du backend :", response.data))
      .catch(error => console.error("Erreur API :", error));
  }, []); // Le tableau vide [] signifie que cela s'exécute une fois au montage

  return (
    <div className="App">
      <h1>hello test</h1>
    </div>
  );
}

export default App;