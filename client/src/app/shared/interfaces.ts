export interface User{
    email:string
    password:string
}

export interface Token{
    access:string
}

export interface Category{
    name:string
    imgSrc?:string
    user?:string
    id?:string
}

export interface Message{
    message:string
}

export interface Position{
    name:string
    category:string
    price:number
    user?:string
    id?:string
    quantity?:number
}

export interface Order{
    create_at?:Date
    order?:number
    consumer?:string
    list:OrderPosition[]
    id?:string
}

export interface OrderPosition{
    name:string
    price:number
    quantity:number
    id?:string
}