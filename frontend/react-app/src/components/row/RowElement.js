import { useState } from 'react';
import './RowElement.css';
import { API, apiPATH, needInfo, selectableColoums } from '../../utils/api';
import SelectableElem from './SelectableElem/SelectableElem';
import { translate } from '../../utils/translate';
import {Input} from '@chakra-ui/react'

function RowElement(props) {
  const [extData, setExtData] = useState(()=>{
    return props.data
  })
  const [data, setData] = useState(props.data)
  const getExtData = async () =>{
    let extended ={}
    await props.coloums.map(async (obj, key) => {
      if (!!selectableColoums[obj] && props.apiPath != selectableColoums[obj]){
        if (selectableColoums[obj] !='DATE'){
      let res = await API.get(selectableColoums[obj] + '?'+ obj + '=' + data[obj])
      res = await res.json()
      let info =''
      for (let coloum in needInfo[obj]){
        const c = needInfo[obj][coloum]
        info += translate[c] + ': ' + res[0][c] + '\n'
      }
      extended = {...extended, [obj]:info} 
      setExtData({...extended})
  }
      }
    })
  }

  const [editState, setEditState] = useState(() =>{
    getExtData()
    return props.isEditing})

  const checkResponce = (res) => {
    if (res.status === 200) {
      props.showNotification('Successful', 2000)
    }
    if (res.status === 422) {
      props.showNotification('Unprocessable Entity', 2000)
    }
    if (res.status === 500) {
      props.showNotification('Somethink went wrong', 2000)
    }
  }

  const updateItem = () => {
    API.update(props.apiPath, data).then(res => {
      checkResponce(res)
      props.refrash(true)
    }).catch(e => {

    })

  }
  const deleteItem = () => {
    API.delete(props.apiPath, data).then(res => {
      checkResponce(res)
      props.refrash(true)
    }).catch(e => {

    })
  }
  const addItem = () => {
    console.log(data)
    API.post(props.apiPath, data).then(res => {
      checkResponce(res)
      props.refrash(true)
    }).catch(e => {

    })
  }


  return (
    (props.isNew) ?
      <div className="elemContainer">
        {props.coloums.map((obj, key) => {
          if (!!selectableColoums[obj] && props.apiPath != selectableColoums[obj]) return <SelectableElem coloumn={props.coloums} name={obj} setValue={(elem) => { setData({ ...data, [elem.name]: elem.value }) }} className="coloumn" key={key} value={data[obj]}></SelectableElem>
          return <Input onChange={(e) => { setData({ ...data, [e.target.name]: e.target.value }) }}
            className="coloumn" name={obj} key={key} value={data[obj]}></Input>
        })}
        <button onClick={() => { addItem() }} className="manageButton">Подтвердить</button>
      </div>
      :
      !editState ?
        <div className="elemContainer">

          {props.coloums.map((obj, key) => {
            if (!!selectableColoums[obj] && props.apiPath != selectableColoums[obj]){
                if (selectableColoums[obj] !='DATE'){

                  return <div className="coloumn" key={key}>{extData[obj]}</div>
               }}
            
             return <div className="coloumn" key={key}>{data[obj]}</div>
          }
          )}
          <button onClick={() => deleteItem()} className="manageButton">Удалить</button>
          <button onClick={() => setEditState(true)} className="manageButton">Изменить</button>
          <button onClick={() => console.log(extData)} className="manageButton">Изменить</button>
        </div> :
        <div className="elemContainer">
          {props.coloums.map((obj, key) => {
            if (!!selectableColoums[obj] && props.apiPath != selectableColoums[obj]) return <SelectableElem coloumn={props.coloums} name={obj} setValue={(elem) => { setData({ ...data, [elem.name]: elem.value }) }} className="coloumn" key={key} value={data[obj]}></SelectableElem>
            return <Input
              onChange={(e) => { setData({ ...data, [e.target.name]: e.target.value }) }}
              className="coloumn" key={key} name={obj} value={data[obj]}>
            </Input>
          }
          )}
          <button onClick={() => {
            updateItem()
            setEditState(false)
          }} className="manageButton">Подтвердить</button>
        </div>
  );
}

export default RowElement;
