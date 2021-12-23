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

    login(user:User):Observable<{tokens:string}>{
        return this.http.post<{tokens:string}>('http://localhost:8000/api/login/', user)
        .pipe(
            tap(
                ({tokens})=>{
                    
                    
                    localStorage.setItem('auth-token', tokens['access'])
                    this.setToken(tokens['access'])
                  
                }
            ) //оператор tap позволяет нам выцепить что-либо из стрима
        )
    
    
    }

    setToken(token:string){
        this.token =token
    }

    getToken():string{
        return this.token
    }

    isAuthenticated():boolean{
        console.log('FROM LOGIN AUTH', !!this.token);

        return !!this.token
    }

    logout(){
        this.setToken(null)
        localStorage.clear()
    }
}