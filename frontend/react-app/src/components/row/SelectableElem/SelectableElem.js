import { useState } from 'react'
import { API, apiSecondPATH, selectableColoums } from '../../../utils/api'
import SearchMenu from './SearchMenu/SearchMenu'
import './SelectableElem.css'


function SelectableElem(props) {

  const getColumn = () => {
    API.get(selectableColoums[props.name] + apiSecondPATH.coloums).then((res) => {
      return res.json()
    }).then(res => {
      setColoumns(res)
    })
  }

  const [isActive, setIsActive] = useState(false)
  const [coloumns, setColoumns] = useState(() => {
    getColumn()
    return []
  })

  return (<>
    <button onClick={() => setIsActive(!isActive)}>{props.value}</button>
    <SearchMenu setValue={(elem) => props.setValue(elem)} isActive={isActive} coloumns={coloumns} name={props.name}></SearchMenu>
  </>

  );
}

export default SelectableElem;
