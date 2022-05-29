import './Notification.css'

function Notification(props) {
  return (
    
    <div hidden={!props.isShowing} className='notification'> {props.text}</div>
  );
}

export default Notification;
