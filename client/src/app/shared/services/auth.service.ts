import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { tap } from "rxjs/operators";
import { User } from "../interfaces";

@Injectable({
    providedIn:'root'
})
export class AuthService{

    private token = ''

    constructor(private http:HttpClient){

    }

    register(user:User):Observable<User>{
        return this.http.post<User>('/api/register/', user)
    }

    login(user:User):Observable<{token:any}>{
        return this.http.post<{token:any}>('/api/login/', user)
        .pipe(
            tap(
                ({token})=>{
                    console.log(token['access']);
                    
                    
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
console.log('ISAUTHENTICATED',!!this.token);

        return !!this.token
    }

    logout(){
        this.setToken('')
        localStorage.clear()
    }
}