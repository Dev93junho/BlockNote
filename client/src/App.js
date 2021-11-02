import {Deploy} from './Component/Deploy/Deploy';
import {useState, useEffect} from 'react';
import TextEditor from './TextEditor';
// fetched with server
function App() {
  const [state, setState] = useState({})

  useEffect(() => {
    fetch("/server").then(response => {
      if(response.staus == 200){
        return response.json()
      }
    }).then(data => console.log(data))
    .then(error => console.log(error))
  })
  return (
    <div className="App">
      {/* <Deploy prop={state}/> */}
      <TextEditor /> 
    </div>
  );
}

export default App;
