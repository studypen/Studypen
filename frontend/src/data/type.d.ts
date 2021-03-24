

interface UserRegistrationDetail{
    first_name: string,
    last_name: string,
    password: string,
    username: string,
    email: string,
    password2: string,
}

interface User {
    first_name: string,
    last_name: string,
    username: string,
    email: string
}

type UserState = {
    user?: User
}

type AuthAction = {
    type: string,
    payload?: User
}

type DispatchType = (args: AuthAction) => UserState
