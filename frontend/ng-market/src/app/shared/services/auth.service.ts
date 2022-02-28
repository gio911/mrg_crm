import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { tap } from "rxjs/operators";
import { User } from "../interfaces";

@Injectable({
    providedIn:'root'
})
export class AuthService{

    private token = null

    constructor(private http:HttpClient){

    }

    register(user:User):Observable<User>{
        return this.http.post<User>('http://localhost:8000/api/register/', user)
    }

    login(user:User):Observable<{token:string}>{
        return this.http.post<{token:string}>('http://localhost:8000/api/login/', user)
        .pipe(
            tap(
                ({token})=>{
                    
                    
                    localStorage.setItem('auth-token', token['access'])
                    this.setToken(token['access'])
                  
                }
            ) //оператор tap позволяет нам выцепить что-либо из стрима
        )
    
    
    }

    setToken(token:string){
        this.token =token
        console.log('FROM SET TOKEN', this.token);
        
    }

    getToken():string{
        console.log('FROM GET TOKEN', this.token);
        
        return this.token
    }

    isAuthenticated():boolean{

        return !!this.token
    }

    logout(){
        this.setToken(null)
        localStorage.clear()
    }
}