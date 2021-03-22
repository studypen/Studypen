import * as actionTypes from './actionTypes'
import { initUser } from './rest'

export const reducer = (state = {}, action: AuthAction): UserState => {
  switch (action.type) {
    case actionTypes.LOGIN_SUCCESS:
      return {...state, user: action.payload}

    case actionTypes.LOG_OUT:
      return {...state, user: undefined}
      // TODO:
      return state;
  }
  return state
}