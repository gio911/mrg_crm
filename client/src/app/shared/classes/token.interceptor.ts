import { AuthService } from "../services/auth.service";
import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest, HttpErrorResponse } from "@angular/common/http";
import { Observable, throwError } from "rxjs";
import { Injectable } from '@angular/core'
import { catchError } from 'rxjs/operators'
import { Router, ActivatedRoute, Params } from '@angular/router'

@Injectable()
export class TokenInterceptor implements HttpInterceptor{
    
    constructor(private auth:AuthService, 
                private router:Router){

    }

    intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        if(this.auth.isAuthenticated()){
            console.log('SET HEADER',this.auth.getToken());
            
            req = req.clone({

                setHeaders:{
                    Authorization:this.auth.getToken()
                }
            })
        }
        return next.handle(req).pipe(
            catchError(
                (error:HttpErrorResponse)=>this.handleError(error)
            )
        )
    }

    private handleError(error:HttpErrorResponse):Observable<any>{
        if(error.status === 401){
            this.router.navigate(['/login'], {
                queryParams:{
                    sessionFaild:true
                }
            })
        }
        return throwError(error)
    }

}