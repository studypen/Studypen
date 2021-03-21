import React from 'react';
import './App.scss';
import { Login } from './component/Login';
import { Registration } from './component/Registration';
import { hot } from 'react-hot-loader/root'
import { setConfig } from 'react-hot-loader';
import { Provider } from 'react-redux'
import { store } from './data/store'

setConfig({
  reloadHooks: false,
});

const App: React.FC = () =>
(
  <Provider store={store}>
    <div className="App">
      <Login />

      <Registration />
    </div>
  </Provider>
);


export default hot(App);
