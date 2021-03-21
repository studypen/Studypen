



interface User {
    name: string,
    isLogin: boolean
}

type UserState = {
    user: User
}

type AuthAction = {
    type: string
}

type DispatchType = (args: AuthAction) => UserState
