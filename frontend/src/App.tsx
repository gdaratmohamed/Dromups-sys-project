import { useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  // Appel API au chargement du composant
  useEffect(() => {
    axios.get("http://localhost:8000/")
      .then(response => console.log("Réponse du backend :", response.data))
      .catch(error => console.error("Erreur API :", error));
  }, []); // Le tableau vide [] signifie que cela s'exécute une fois au montage

  return (
    <div className="App">
      <h1>hello test</h1>
      <p>Vérifiez la console du navigateur (F12) pour voir la réponse du backend.</p>
    </div>
  );
}

export default App;