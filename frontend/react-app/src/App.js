import { useEffect, useState } from 'react';
import './App.css';
import RowElement from './components/RowElement';
import Select from 'react-select';
import { apiPATH, apiSelector, API } from './utils/api';


function App() {
  const [data, setData] = useState([])
  const [selectedOption, setSelectedOption] = useState({ label: '', isSearching: false })
  const [newElems, setNewElems] = useState([])

  useEffect(() => {
    console.log('apiResolve')
    if (!!selectedOption.isSearching) {
      API.get(apiPATH[selectedOption.value]).then(res => {
        return res.json()
      }).then(async res => {
        if (Array.isArray(res)) {
          setData(res)
          setNewElems([])
          setSelectedOption({ ...selectedOption, isSearching: false })
        }
        else
          throw new Error("Bad format of data");
      }).catch(res => {
        setData([])
        setSelectedOption({ ...selectedOption, isSearching: false })
      })

    }
  })

  return (
    <div className="wrap">
      <div className='header'>
      </div>
      <div className='main'>
        <div className='elemScreen'>
          <div className='header'>{data[0] ? Object.keys(data[0]).map((coloumn, key) => <div key={key}>{coloumn}</div>) : ''}</div>
          {data.map((obj, key) => <RowElement apiPath={apiPATH[selectedOption.value]} isEditing={false} props={obj} key={key} />)}
          {newElems.map((obj, key) => <RowElement apiPath={apiPATH[selectedOption.value]} props={obj} isNew={true} key={key}></RowElement>
          )}
        </div>
        <div className='userBar'>
          <button className='manageButton' onClick={() => {
            debugger
            console.log(data)
          }}> check data</button>
          <button className='manageButton' onClick={() => { setData([]) }}> clear list</button>
          <button className='manageButton' onClick={() => {
            if (!!data[0]) {
              let elem = {}
              for (let i of Object.keys(data[0])) {
                elem[i] = ''
              }
              setNewElems([elem])
            }
          }}> add elems</button>
          <div className='manageInfo'> current state is {selectedOption.label}</div>
          <Select
            defaultValue={selectedOption}
            onChange={(option) => {
              setData([])
              setSelectedOption({ ...option, isSearching: true })
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
