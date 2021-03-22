import React from 'react'
import { shallowEqual, useSelector } from 'react-redux'
import { Login } from '../component/Login'



export const Home: React.FC = () => {
  const user = useSelector((state: UserState) => state.user, shallowEqual)
  return (
    <section style={{marginLeft: 20}} className="home">
      {
        user === undefined
        ? <Login/>
        : <h1> Welcome {user.first_name} </h1>
      }
    </section>
  )
}