import React from 'react'
import { shallowEqual, useSelector } from 'react-redux'
import { Dashboard as Dashboard } from '../component/Dashboard'
import { Welcome } from '../component/Welcome'


export const Home: React.FC = () => {
  const user = useSelector((state: UserState) => state.user, shallowEqual)
  return (
    <section style={{marginLeft: 20}} className="home">
      {
        user === undefined
        ? <Welcome/>
        : <Dashboard/>
      }
    </section>
  )
}