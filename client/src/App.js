import {Deploy} from './Component/Deploy/Deploy';
import {useState, useEffect} from 'react';

const flaskURL = "http://localhost:5000"

function App() {
  const [state, setState] = useState({})

  // fetch can be call the API
  // fetch(back-end address)
  useEffect(() => {
    fetch(`${flaskURL}/index`).then(response => {
      if(response.status === 200){
        return response.json()
      }
    }).then(data => console.log(data))
    .then(error => console.log(error))
  })
  return (
    <div className="App">
      <Deploy />
    </div>
  );
}

export default App;
