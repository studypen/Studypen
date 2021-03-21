import React from 'react';
import './App.scss';
import { Login } from './component/Login';
import { Registration } from './component/Registration';

const App: React.FC = () =>
(
  <div className="App">
    <Login/>
    <Registration/>
  </div>
);

export default App;
