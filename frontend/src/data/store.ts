import { reducer } from './reducer';
import { createStore, Store } from 'redux';

export type AppStore = Store<UserState, AuthAction>






export const store: AppStore = createStore(reducer)