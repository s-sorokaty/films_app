import { useState } from 'react';
import './RowElement.css';
import lodash from 'lodash'
import { API } from '../utils/api';

function RowElement(props) {
  const [editState, setEditState] = useState(props.isEditing)
  const [data, setData] = useState(() => {
    const elemData = []
    for (const [key, value] of Object.entries(props.props)) {
      elemData.push(value)
    }
    return elemData
  })
  const getDBObj = () => {
    let body = {}
    for (let i in key) {
      console.log(key[i], data[i])
      body[key[i]] = data[i]
    }
    return body
  }
  const [key, setKey] = useState(() => {
    const elemKey = []
    for (const [key, value] of Object.entries(props.props)) {
      elemKey.push(key)
    }
    return elemKey
  })

  const updateItem = () => {
    API.update(props.apiPath, getDBObj())
  }
  const deleteItem = () => {
    API.delete(props.apiPath, getDBObj())
  }

  return (
    !editState ?
      <div className="elemContainer">
        {data.map((obj, key) => <div className="coloumn" key={key}>{obj} </div>)}
        <button onClick={()=>{deleteItem()}} className="manageButton">delete</button>
        <button onClick={() => setEditState(true)} className="manageButton">edit</button>
      </div> :
      <div className="elemContainer">
        {data.map((obj, key) => <input onChange={(e) => {
          const newData = lodash.cloneDeep(data)
          newData[data.indexOf(data[key])] = e.target.value
          setData(newData)
        }} className="coloumn" key={key} value={data[key]}></input>)}
        <button onClick={() => {
          updateItem()
          setEditState(false)
        }} className="manageButton">confirm</button>
      </div>
  );
}

export default RowElement;
