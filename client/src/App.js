import {Deploy} from './Component/Deploy/Deploy';
import {useState, useEffect} from 'react';
import Scrapper from './Component/Scrapper/Scrapper';

function App() {
  const [state, setState] = useState({})

  // fetch can be call the API
  useEffect(() => {
    fetch("/server").then(response => {
      if(response.status == 200){
        return response.json()
      }
    }).then(data => console.log(data))
    .then(error => console.log(error))
  })
  return (
    <div className="App">
      <Deploy />
      <Scrapper />
    </div>
  );
}

export default App;
