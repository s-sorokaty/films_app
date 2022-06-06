import { useEffect, useState } from 'react';
import './App.css';
import RowElement from './components/row/RowElement';
import Select from 'react-select';
import { apiPATH, apiSelector, API, apiSecondPATH } from './utils/api';
import Notification from './components/notification/Notification';
import { translate } from './utils/translate';


function App() {

  const [data, setData] = useState([])
  const [coloums, setColoums] = useState([])
  const [selectedOption, setSelectedOption] = useState({ label: '' })
  const [newElems, setNewElems] = useState([])
  const [isRefrashing, setIsRefrash] = useState(false)
  const [isShowNotification, setIsShowNotification] = useState(false)
  const [textNotification, setTextNotification] = useState('')
  const [selectors, setSelectors] = useState({})

  const showNotification = (text, timeout) => {
    setIsShowNotification(true)
    setTextNotification(text)
    setTimeout(() => {
      setIsShowNotification(false)
    }, timeout)
  }

  const refreshList = () => {
    let query = '?'
    coloums.map(coloumn=>{
      if (!!selectors[coloumn]){
        query += coloumn + '=' + selectors[coloumn] + '&'
        setData([])
      }
    })
    if (query.length === 1){
      query=''
    }
    if (!!selectedOption.value)
      API.get(apiPATH[selectedOption.value] + query).then(res => {
        return res.json()
      })
        .then(async res => {
          if (Array.isArray(res)) {
            setData(res)
            setSelectedOption({ ...selectedOption })
          }
          else setData([])
        }).catch(e => {
          setData([])
          setSelectedOption({ ...selectedOption })
          showNotification(e.message, 3000)
        })
  }
  const getColoums = () => {
    if (!!selectedOption.value)
      API.get(apiPATH[selectedOption.value] + apiSecondPATH.coloums).then((res) => {
        return res.json()
      }).then(res => {
        if (Array.isArray(res)) setColoums(res)
        else setColoums([])
      }).catch(e => {
        setColoums([])
        showNotification(e.message, 3000)
      })
  }
  const sort = (coloumn) => {
    let newDate = [...data]
    console.log(data)
    console.log(newDate.sort((a, b) => {
      if (a[coloumn] > b[coloumn])
        return -1
    }))
    setData([])
    setData(newDate)
  }

  useEffect(() => {
    setData([])
    setIsRefrash(false)
    getColoums()
    refreshList()
  }, [isRefrashing])

  return (
    <div className="wrap">
      <div className='mainHeader'>
        <div className='mainName'>Приложения для управления кинотеатром.</div>
      </div>
      <div className='main'>
        <div className='elemScreen'>
          <div className='header'>{coloums.map((coloumn, key) => {
            return <div className='coloumnName' onClick={() => { 
              // sort(coloumn) 
            }} key={key}>{translate[coloumn]}</div>
          })}</div>
          {data.map((obj, key) => <RowElement apiPath={apiPATH[selectedOption.value]} coloums={coloums} showNotification={showNotification} refrash={setIsRefrash} isEditing={false} isNew={false} data={obj} key={key} />)}
          {newElems.map((obj, key) => <RowElement apiPath={apiPATH[selectedOption.value]} coloums={coloums} showNotification={showNotification} refrash={setIsRefrash} data={obj} isNew={true} key={key}></RowElement>
          )}
        </div>
        <div className='userBar'>
          <button className='addButton' onClick={() => {
            const emptyObj = {}
            coloums.map(obj => emptyObj[obj])
            if (!!coloums.length)
              setNewElems([emptyObj])
          }}> Добавить запись</button>
          <div className='manageInfo'>{selectedOption.label}</div>
          <Select
            defaultValue={selectedOption}
            onChange={(option) => {
              setData([])
              setIsRefrash(true)
              setSelectedOption({ ...option })
              setNewElems([])
              setSelectors({})
            }}
            options={apiSelector}
            className='manageSelector'
          ></Select>
          <div className='filterElement'>
          {coloums.map(((obj, key) => {
          return <div className = 'searchInput' key={key}><input  onChange={(e)=>{
            setSelectors({...selectors, [obj]:e.target.value})
          }} placeholder={translate[obj]} value={selectors[obj]}></input></div>
        }))}
        <button className='searchInput' onClick={()=>{refreshList()}}>Найти</button>
        <button className='searchInput' onClick={()=>{
          console.log(selectors)
          console.log(data)
          
          }}>Селекторы</button>
          </div>
        </div>
      </div>
      <Notification isShowing={isShowNotification} text={textNotification}></Notification>
    </div>
  );
}

export default App;
