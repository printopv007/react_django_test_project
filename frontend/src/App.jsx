import { useState,useEffect } from 'react'
import './App.css'

function App() {
 const[data, SetData]=useState([])
  useEffect(()=>{
    async function fetchData(){
      console.log(import.meta.env.VITE_API_URL);
      try{
        const response = await fetch(`${import.meta.env.VITE_API_URL}posts`);
        if(!response){
          throw new Error('Network Response Failed');
        }
        const result= await response.json();
        // console.log(result);
        SetData(result);
      }
      catch(error){
        console.log('Error Fetching data:'+error);
      }

    }
    fetchData();
  },[]);


  return (
   
    <div>
      <h1 className='users'>test</h1>
      {data.map((data)=>(
      <div className='user'><h3 key={data.id}></h3><br /><h1>{data.title}{data.body}</h1></div>
      ))}
    </div>


  )
}

export default App
