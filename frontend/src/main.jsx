import React, {useEffect, useState} from 'react';
import {createRoot} from 'react-dom/client';
import './style.css';

function App(){
  const [data,setData]=useState(null);
  useEffect(()=>{fetch('http://localhost:8000/action-potential').then(r=>r.json()).then(setData)},[]);
  if(!data) return <main><h1>Cardiac Action Potential</h1><p>loading...</p></main>;
  return <main><h1>Cardiac Action Potential Simulator</h1><p>A simple ventricular cell model.</p><p>Approx. AP duration: {Math.round(data.duration_ms)} ms</p><pre>{JSON.stringify(data.phases,null,2)}</pre></main>
}
createRoot(document.getElementById('root')).render(<App/>);
