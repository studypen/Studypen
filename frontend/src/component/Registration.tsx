import React, { FormEvent, FormEventHandler, useState } from 'react'
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export const Registration: React.FC = () => {
  const [email, setEmail] = useState("hdsj@gmail.com")
  const [username, setUsername] = useState("user")
  const [password, setPassword] = useState("")
  const [rePassword, setRePassword] = useState("")


  const login: FormEventHandler = async (e: FormEvent) => {
    e.preventDefault()
    try {
      const res = await axios.post('/account/registration/',
        { username, email, password1: password, password2: rePassword })
        .catch(error=> console.log({msg: error?.response?.data || error}))

      console.log({ email, password1: password, res })
    } catch (e) {
      console.log(e)
    }
  }

  return (<div>
    <h2> Registration </h2>
    <form onSubmit={login}>
      <label>
        <p>Username</p>
        <input name="username" value={username} onChange={({ target }) => setUsername(target.value)} type="text" required />
      </label>
      <label>
        <p>Email</p>
        <input name="email" value={email} onChange={({ target }) => setEmail(target.value)} type="email" required />
      </label>
      <label>
        <p>Password</p>
        <input name="password" value={password} onChange={({ target }) => setPassword(target.value)} type="password" required />
      </label>
      <label>
        <p>Re enter Your Password</p>
        <input name="re-password" value={rePassword} onChange={({ target }) => setRePassword(target.value)} type="password" required />
      </label >
      <div>
        <button type="submit">Submit</button>
      </div>
    </form>
  </div>)
}