import axios, { AxiosError } from "axios";
import { Dispatch } from "react";
import * as actions from "./actionTypes";
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'


export const initUser = async (dispatch: Dispatch<AuthAction>): Promise<void> => {
  const res = await axios.get<User>('/account/user/')
    .catch((res: AxiosError) => res.response?.status == 403)

  if (typeof res == 'boolean')
    dispatch({ type: actions.LOG_OUT })

  else dispatch({ type: actions.LOGIN_SUCCESS, payload: res.data })
}


export const logout = async (dispatch: Dispatch<AuthAction>): Promise<void> => {
  const res = await axios.get<void>('/account/logout/')
    .catch((res: AxiosError) => res.response?.status == 403)

  if (typeof res != 'boolean')
    dispatch({ type: actions.LOG_OUT })
  else console.error('handel logout failed')
}


export const login = async (dispatch: Dispatch<AuthAction>, username: string, password: string): Promise<void> => {
  const res = await axios.post<User>('/account/login/', { username, password })
    .catch((err: AxiosError) => err.response?.status === 403)
  if (typeof res !== 'boolean')
    dispatch({ type: actions.LOGIN_SUCCESS, payload: res.data })
  else console.log('handel login failed')
}
