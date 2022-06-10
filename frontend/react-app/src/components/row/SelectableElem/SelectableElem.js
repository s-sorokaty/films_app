import { useEffect, useState } from 'react'
import { API, apiSecondPATH, selectableColoums } from '../../../utils/api'
import SearchMenu from './SearchMenu/SearchMenu'
import './SelectableElem.css'
import {Input} from '@chakra-ui/react'

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

  const [data, setData] = useState(props.value);
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
      ? <Input id="datetime" type="datetime-local" onChange={(e) => { setData(e.target.value) } } value={props.value}></Input>
      : <><Input onClick={() => setIsActive(!isActive)} onChange={()=>{console.log(props.value)}} value={props.value}></Input>
        <SearchMenu setIsActive = {()=>{setIsActive()}} setValue={(elem) => props.setValue(elem)} isActive={isActive} coloumns={coloumns} name={props.name}></SearchMenu>
      </>
    }

  </>

  );
}

export default SelectableElem;
