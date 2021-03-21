import * as actionTypes from './actionTypes'


const user: User = {
  name: 'unknown',
  isLogin: false
}

const initialState: UserState = { user }
export const reducer = (state = initialState, action: AuthAction): UserState => {
  switch (action.type) {
    case actionTypes.LOGIN_START:
      

      // TODO:
      return state;
  }
  return state
}