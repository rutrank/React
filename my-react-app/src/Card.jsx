
function Card(props) {

  return (
    <div className="card">
      <img className="img" src="http://via.placeholder.com/150" alt="profile picture"></img>
      <h2>{props.name}</h2>
      <p>I am a boy and studying react right now and i like to watch movies</p>
    </div>
  );

}

export default Card