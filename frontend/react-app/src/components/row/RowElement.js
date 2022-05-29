import { useState } from 'react';
import './RowElement.css';
import { API } from '../../utils/api';

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
    API.post(props.apiPath, data).then(res => {
      checkResponce(res)
      props.refrash(true)
    })
  }

  return (
    (props.isNew) ?
      <div className="elemContainer">
        {props.coloums.map((obj, key) => <input onChange={(e) => { setData({ ...data, [e.target.name]: e.target.value }) }}
          className="coloumn" name={obj} key={key} value={data[obj]}></input>)}
        <button onClick={() => { addItem() }} className="manageButton">apply</button>
      </div>
      :
      !editState ?
        <div className="elemContainer">
          {props.coloums.map((obj, key) => <div className="coloumn" key={key}>{data[obj]} </div>
          )}
          <button onClick={() => deleteItem()} className="manageButton">delete</button>
          <button onClick={() => setEditState(true)} className="manageButton">edit</button>
        </div> :
        <div className="elemContainer">
          {props.coloums.map((obj, key) =>
            <input
              onChange={(e) => { setData({ ...data, [e.target.name]: e.target.value }) }}
              className="coloumn" key={key} name={obj} value={data[obj]}>
            </input>
          )}
          <button onClick={() => {
            updateItem()
            setEditState(false)
          }} className="manageButton">confirm</button>
        </div>
  );
}

export default RowElement;
