import React, { FormEvent, FormEventHandler, useState } from 'react'
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export const Login: React.FC = () => {
  const [username, setUsername] = useState("hdsj@gmail.com")
  const [password, setPassword] = useState("kdk")

  const login: FormEventHandler = async (e: FormEvent) => {
    e.preventDefault()

      const res = await axios.post('/account/login/', { username, password })
          .catch(error=> console.log({error}))


      console.log({ username, password, res })

  }

  return (<div>
    <h2>Login</h2>
    <form onSubmit={login}>
      <label>
        <p>Email</p>
        <input name="username" value={username} onChange={({ target }) => setUsername(target.value)} type="text" required />
      </label>
      <label>
        <p>Password</p>
        <input name="password" value={password} onChange={({ target }) => setPassword(target.value)} type="password" required />
      </label>
      <div>
        <button type="submit">Submit</button>
      </div>
    </form>
  </div>)
}