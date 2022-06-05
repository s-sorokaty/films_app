import { useEffect, useState } from 'react'
import { API, apiSecondPATH, selectableColoums } from '../../../utils/api'
import SearchMenu from './SearchMenu/SearchMenu'
import './SelectableElem.css'

function toTimestamp(strDate) {
  var datum = Date.parse(strDate);
  return datum / 1000;
}

function SelectableElem(props) {
  const getColumn = () => {
    API.get(selectableColoums[props.name] + apiSecondPATH.coloums).then((res) => {
      return res.json()
    }).then(res => {
      setColoumns(res)
    })
  }

  const [data, setData] = useState('');
  const [isActive, setIsActive] = useState(false)
  const [coloumns, setColoumns] = useState(() => {
    getColumn()
    return []
  })



  useEffect(() => {
    props.setValue({ name: props.name, value: data })
  }, [data])

  return (<>
    {(selectableColoums[props.name] == 'DATE')
      ? <input id="datetime" type="datetime-local" onChange={(e) => { setData(toTimestamp(e.target.value)) }} ></input>
      : <><input onClick={() => setIsActive(!isActive)} value={props.value} ></input>
        <SearchMenu setValue={(elem) => props.setValue(elem)} isActive={isActive} coloumns={coloumns} name={props.name}></SearchMenu>
      </>
    }

  </>

  );
}

export default SelectableElem;
