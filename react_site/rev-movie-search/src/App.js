import React, { Component } from 'react';
import './App.css';
import $ from 'jquery'

class App extends Component {
  constructor(props){
    super(props)
    this.state = {rows: []}
    this.searchMovie("*:*")
  }

searchMovie(query){
  const url = "http://localhost:8983/solr/movies/select?defType=edismax&q="+query+"&qf=cast.name%20cast.character%20directors.name%20genres%20original_title%20overview%20production_companies%20production_countries%20release_date%20spoken_languages%20tagline&rows=50"
  $.ajax({
    url: url,
    success: (res) => {
      console.log(res)
      const movies = res.response.docs
      var movieRows = []
      movies.forEach((movie) => {
        console.log(movie.title)
        movieRows.push(<p>{movie.title}</p>)
      })
      this.setState({rows: movieRows})
    },
    error: (xhr, status, err)=>{
      console.error("failed")
    }
  })
}

searchHandler(e){
  this.searchMovie(e.target.value)
}

  render() {
    return (
      <div className="App">
        <h1>
          Movie Search
        </h1>
        <input className = "SearchBar" onChange = {this.searchHandler.bind(this)} placeholder = "search"/>
        <div className="Results">
          {this.state.rows}
        </div>
      </div>
    );
  }
}

export default App;
