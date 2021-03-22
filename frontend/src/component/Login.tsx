import React, { Dispatch, FormEvent, FormEventHandler, useState } from 'react'
import axios from "axios";
import './Form.scss'
import { useDispatch } from 'react-redux';
import { login } from '../data/rest';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export const Login: React.FC = () => {
  const [username, setUsername] = useState("hdsj@gmail.com")
  const [password, setPassword] = useState("kdk")
  const dispatch: Dispatch<AuthAction> = useDispatch()


  return (<div>
    <form onSubmit={(e) => {e.preventDefault(); login(dispatch, username, password)}}>
      <h2>Login</h2>
      <label className="input-group">
        <p>Username</p>
        <input name="username" value={username} onChange={({ target }) => setUsername(target.value)} type="text" required />
      </label>
      <label className="input-group">
        <p>Password</p>
        <input name="password" value={password} onChange={({ target }) => setPassword(target.value)} type="password" required />
      </label>
      <div>
        <input type="submit" value="Submit" />
      </div>
    </form>
  </div>)
}