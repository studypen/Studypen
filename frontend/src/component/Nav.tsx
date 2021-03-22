import React from 'react'
import { useSelector, shallowEqual, useDispatch } from 'react-redux'
import { Dispatch } from 'redux'
import { logout } from '../data/rest'
import './Nav.scss'



export const Nav: React.FC = () => {
  const user = useSelector((state: UserState) => state.user, shallowEqual)
  const dispatch = useDispatch<Dispatch<AuthAction>>()

  
  return (<nav>
    <h1>Hello Name</h1>
    <div className="user">
      {user === undefined ?
        (<div>
          <button>
            Login
          </button>
          <button>
            SignUp
          </button>
        </div>)
        : (<button onClick={() => logout(dispatch)}>
          Logout
        </button>)
      }
    </div>
  </nav>)
}