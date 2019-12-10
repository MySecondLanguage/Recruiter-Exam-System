import React, { Component } from 'react';
import { connect } from "react-redux";
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import Home from '../components/home';


class App extends Component {

  render() {
    return (
    
      <React.Fragment>
    
          <div className="container">
                <Home></Home>            
          </div>
    
      </React.Fragment>
    
    );
  }
}

export default App;