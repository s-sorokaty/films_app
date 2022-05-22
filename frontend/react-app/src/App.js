import { useEffect, useState } from 'react';
import './App.css';
import RowElement from './components/RowElement';
import Select from 'react-select';
import { apiPATH, apiSelector, API } from './utils/api';


function App() {
  const [data, setData] = useState([])
  const [selectedOption, setSelectedOption] = useState({ label: '' , isSearching: false})

  
  useEffect(() => {
    console.log('apiResolve')
    if (!!selectedOption.isSearching) {
      API.get(apiPATH[selectedOption.value]).then( res => {
        return res.json()
      }).then(async res => {
        if (Array.isArray(res)){
        console.log(data)
        setData(res)
        setSelectedOption({...selectedOption, isSearching: false })
      }
        else
          throw new Error("Bad format of data");
      }).catch(res=>{
          setData([]) 
          console.log(res)
          setSelectedOption({...selectedOption,isSearching: false })
      })
    
    }
  })

  return (
    <div className="wrap">
      <div className='header'>
      </div>
      <div className='main'>
        <div className='elemScreen'>
          <div className='header'>{data[0] ? Object.keys(data[0]).map((coloumn,key) => <div key={key}>{coloumn}</div>):''}</div>
          {data.map((obj, key) => <RowElement apiPath={apiPATH[selectedOption.value]} isEditing={false} props={obj} key={key} />)}
        </div>
        <div className='userBar'>
        <button className='manageButton' onClick={() => { console.log(data) 
        }}> check data</button>
          <button className='manageButton' onClick={() => { setData([]) }}> clear list</button>
          <button className='manageButton' onClick={() => { setData([{ Surname: '3', phoneNumber: 4, idClient: 1, Name: '2' }]) }}> return list</button>
          <button className='manageButton' onClick={() => {
            const newData = [...data, { Surname: '3', phoneNumber: 4, idClient: 1, Name: '2' }]
            setData(newData)
          }}> add elems</button>
          <div className='manageInfo'> current state is {selectedOption.label}</div>
          <Select
            defaultValue={selectedOption}
            onChange={(option)=>{
              setData([])
              setSelectedOption({...option, isSearching:true})
            }}
            options={apiSelector}
            className='manageSelector'
          ></Select>


        </div>
      </div>
    </div>
  );
}

export default App;
