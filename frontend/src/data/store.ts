import { reducer } from './reducer'
import { createStore, Store } from 'redux'
import { initUser } from './rest'

export type AppStore = Store<UserState, AuthAction>


export const store: AppStore = createStore(reducer)

initUser(store.dispatch)