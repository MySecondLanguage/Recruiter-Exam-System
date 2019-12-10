import React from "react";
import ReactDOM from "react-dom";
import { Provider } from 'react-redux';
import { createStore } from 'redux';
import { BrowserRouter } from 'react-router-dom';

import App from '../client/components/App';
import Reducer from '../client/reducer';
import './style.scss';

const store = createStore(Reducer)


function onStateChange() {
  const state = store.getState();
}

store.subscribe(onStateChange)

ReactDOM.render((
  <BrowserRouter>
      <Provider store={store}>
        <App />
      </Provider>
  </BrowserRouter>
), document.getElementById('app'))