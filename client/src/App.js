import {Deploy} from './Component/Deploy/Deploy';
import {useState, useEffect} from 'react';
import Scrapper from './Component/Scrapper/Scrapper';

const flaskURL = "http://localhost:5000"

function App() {
  const [state, setState] = useState({})

  // fetch can be call the API
  // fetch(back-end address)
  useEffect(() => {
    fetch(`${flaskURL}/`).then(response => {
      if(response.status === 200){
        return response.json()
      }
    }).then(data => setState(data))
    .then(error => console.log(error))
  })
  return (
    <div className="App">
      <Scrapper prop={state} />
    </div>
  );
}

export default App;
