import './SearchMenu.css'
import { translate } from '../../../../utils/translate'
import { API, selectableColoums } from '../../../../utils/api'
import { useState } from 'react'

function SearchMenu(props) {
  const [searchResult, setSearchResult] = useState([])
  const [selectors, setSelectors] = useState({})

  const getElems = () => {
    let query = '?'
    props.coloumns.map(coloumn=>{
      if (!!selectors[coloumn]){
        query += coloumn + '=' + selectors[coloumn] + '&'
      }
    })
    if (query.length === 1){
      query=''
    }
    API.get(selectableColoums[props.name] + query).then((res) => {
      return res.json()
    }).then(res => {
      console.log(res)
      setSearchResult(res)
    })
  }
  return (<>
    <div className='searchMenu' hidden={!props.isActive}>
      <div className='inputElems'>
        {props.coloumns.map(((obj, key) => {
          return <div key={key}><div><input onChange={(e)=>{
            setSelectors({...selectors, [obj]:e.target.value})
          }} placeholder={translate[obj]}></input></div></div>
        }))}
        <div><button onClick={() => { getElems() }}>Поиск</button></div>
      </div>
      <div className='result'>
        <div className='resultObj'>
        {props.coloumns.map(coloumn=><div className='elem'>{translate[coloumn]}</div>)}
        </div>
        {searchResult.map(res => {
        let resObj = []
        props.coloumns.map((coloumn, key) => resObj.push(<div onClick={()=>{
        }} className='elem' key={key}>{res[coloumn]}</div>))
        return <div className='resultObj' onClick={(e) => {
          props.setValue({
            name: props.name,
            value: res[props.name]
          })
          props.setIsActive(!props.isActive)
        }}>{resObj}</div>
      })}</div>
    </div>
  </>

  );
}

export default SearchMenu;
