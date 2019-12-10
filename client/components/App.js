import React, { Component } from 'react';
import { connect } from "react-redux";
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import Home from '../components/home';


class App extends Component {

  render() {
    return (
    
      <React.Fragment>
        <Router>
          <div className="container">
            {/* Menu Bara */}
            <nav className="navbar navbar-light bg-light justify-content-center">
              <a className="navbar-brand" href="#">
                RECRUITER EXAM SYSTEM
              </a>
            </nav>

            {/* Routing */}
            <Switch>
                <Route exact path='/' component={Home} />
            </Switch>
            
          </div>
       </Router>
      </React.Fragment>
    
    );
  }
}

export default App;