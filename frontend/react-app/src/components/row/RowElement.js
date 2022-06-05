import { useState } from 'react';
import './RowElement.css';
import { API, selectableColoums } from '../../utils/api';
import SelectableElem from './SelectableElem/SelectableElem';

function RowElement(props) {
  const [editState, setEditState] = useState(props.isEditing)
  const [data, setData] = useState(props.data)

  const checkResponce = (res) => {
    if (res.status == 200) {
      props.showNotification('Successful', 2000)
    }
    if (res.status == 422) {
      props.showNotification('Unprocessable Entity', 2000)
    }
    if (res.status == 500) {
      props.showNotification('Somethink went wrong', 2000)
    }
  }

  const updateItem = () => {
    API.update(props.apiPath, data).then(res => {
      checkResponce(res)
      props.refrash(true)
    })

  }
  const deleteItem = () => {
    API.delete(props.apiPath, data).then(res => {
      checkResponce(res)
      props.refrash(true)
    })
  }
  const addItem = () => {
    console.log(data)
    API.post(props.apiPath, data).then(res => {
      checkResponce(res)
      props.refrash(true)
    })
  }

  return (
    (props.isNew) ?
      <div className="elemContainer">
        {props.coloums.map((obj, key) => {
          if (!!selectableColoums[obj] && props.apiPath != selectableColoums[obj]) return <SelectableElem coloumn={props.coloums} name={obj} setValue={(elem) => { setData({ ...data, [elem.name]: elem.value }) }} className="coloumn" key={key} value={data[obj]}></SelectableElem>
          return <input onChange={(e) => { setData({ ...data, [e.target.name]: e.target.value }) }}
            className="coloumn" name={obj} key={key} value={data[obj]}></input>
        })}
        <button onClick={() => { addItem() }} className="manageButton">Подтвердить</button>
      </div>
      :
      !editState ?
        <div className="elemContainer">
          {props.coloums.map((obj, key) => <div className="coloumn" key={key}>{data[obj]} </div>
          )}
          <button onClick={() => deleteItem()} className="manageButton">Удалить</button>
          <button onClick={() => setEditState(true)} className="manageButton">Изменить</button>
        </div> :
        <div className="elemContainer">
          {props.coloums.map((obj, key) => {
            if (!!selectableColoums[obj] && props.apiPath != selectableColoums[obj]) return <SelectableElem coloumn={props.coloums} name={obj} setValue={(elem) => { setData({ ...data, [elem.name]: elem.value }) }} className="coloumn" key={key} value={data[obj]}></SelectableElem>
            return <input
              onChange={(e) => { setData({ ...data, [e.target.name]: e.target.value }) }}
              className="coloumn" key={key} name={obj} value={data[obj]}>
            </input>
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
