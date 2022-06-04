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

  const showNotification = (text, timeout) => {
    setIsShowNotification(true)
    setTextNotification(text)
    setTimeout(() => {
      setIsShowNotification(false)
    }, timeout)
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
  const refreshList = () => {
    if (!!selectedOption.value)
      API.get(apiPATH[selectedOption.value]).then(res => {
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

  useEffect(() => {
    setIsRefrash(false)
    getColoums()
    refreshList()
  }, [isRefrashing])

  return (
    <div className="wrap">
      <div className='mainHeader'>
        <div className='mainName'>Приложения для бронирования управления кинотеатром.</div>
      </div>
      <div className='main'>
        <div className='elemScreen'>
          <div className='header'>{coloums.map((coloumn, key) => {
            return <div className='coloumnName' key={key}>{translate[coloumn]}</div>
          })}</div>
          {data.map((obj, key) => <RowElement apiPath={apiPATH[selectedOption.value]} coloums={coloums} showNotification={showNotification} refrash={setIsRefrash} isEditing={false} isNew={false} data={obj} key={key} />)}
          {newElems.map((obj, key) => <RowElement apiPath={apiPATH[selectedOption.value]} coloums={coloums} showNotification={showNotification} refrash={setIsRefrash} data={obj} isNew={true} key={key}></RowElement>
          )}
        </div>
        <div className='userBar'>
          <button className='manageButton' onClick={() => {
            console.log(data)
          }}> check data</button>
          <button className='manageButton' onClick={() => {
            const emptyObj = {}
            coloums.map(obj => emptyObj[obj] = '')
            if (!!coloums.length)
              setNewElems([emptyObj])
          }}> add elems</button>
          <div className='manageInfo'>{selectedOption.label}</div>
          <Select
            defaultValue={selectedOption}
            onChange={(option) => {
              setData([])
              setIsRefrash(true)
              setSelectedOption({ ...option })
              setNewElems([])
            }}
            options={apiSelector}
            className='manageSelector'
          ></Select>
        </div>
      </div>
      <Notification isShowing={isShowNotification} text={textNotification}></Notification>
    </div>
  );
}

export default App;
