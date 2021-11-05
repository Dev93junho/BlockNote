import {useState, useEffect} from 'react';
import Scrapper from './Component/Scrapper/Scrapper';
import axios from "axios"

const flaskURL = "http://localhost:5000"

function App() {
  const [state, setState] = useState({})

  // fetch can be call the API
  // fetch(back-end address)
  useEffect(() => {
    axios.get(`${flaskURL}/post/`, {
      'method' : 'GET',
      headers: {
        'Content-Type' :'application/json'
      }
    })
    .then(response => response.json())
    .then(response => setState(response))
    // .catch(error => console.log(error))
  },[])

  return (
    <div className="App">
      <Scrapper props={state}/>
    </div>
  );
}

export default App;

// function escapeUnicode(str) {
//   return str.replace(/[^\0-~]/g, function(ch) {
//       return "\\u" + ("0000" + ch.charCodeAt().toString(16)).slice(-4);
//   });
// }

