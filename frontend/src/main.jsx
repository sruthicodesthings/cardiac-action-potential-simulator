import React, {useEffect, useState} from 'react';
import {createRoot} from 'react-dom/client';
import './style.css';

function Graph({time, voltage}){
  const w=700,h=300,p=30;
  const points=voltage.map((v,i)=>{
    const x=p+(time[i]/time[time.length-1])*(w-2*p);
    const y=p+((40-v)/140)*(h-2*p);
    return `${x},${y}`;
  }).join(' ');
  return <svg viewBox={`0 0 ${w} ${h}`}><line x1={p} y1={h-p} x2={w-p} y2={h-p}/><line x1={p} y1={p} x2={p} y2={h-p}/><polyline points={points} fill="none" stroke="black" strokeWidth="3"/></svg>
}
function App(){
  const [data,setData]=useState(null);
  useEffect(()=>{fetch('http://localhost:8000/action-potential').then(r=>r.json()).then(setData)},[]);
  if(!data) return <main><h1>Cardiac Action Potential</h1><p>loading...</p></main>;
  return <main><h1>Cardiac Action Potential Simulator</h1><p>This shows a simplified ventricular myocyte action potential.</p><Graph time={data.time_ms} voltage={data.voltage_mv}/><h2>The phases</h2>{Object.entries(data.phases).map(([n,x])=><p key={n}><b>Phase {n}:</b> {x}</p>)}<p><b>Approx. duration:</b> {Math.round(data.duration_ms)} ms</p></main>
}
createRoot(document.getElementById('root')).render(<App/>);
