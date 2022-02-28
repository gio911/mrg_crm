import { Injectable } from "@angular/core";
import { ActivatedRouteSnapshot, CanActivate, CanActivateChild, Router, RouterStateSnapshot } from "@angular/router";
import { Observable, of } from "rxjs";
import { AuthService } from "../services/auth.service";

@Injectable({
    providedIn:'root'
})
export class AuthGuard implements CanActivate, CanActivateChild{
    constructor(private auth:AuthService, 
                private router:Router){
                    
                }

    canActivate(route:ActivatedRouteSnapshot, state:RouterStateSnapshot):Observable<boolean>{
        
        
        if(this.auth.isAuthenticated()){
            
            return of(true)
        }else{
            this.router.navigate(['login'], {
                queryParams:{
                    accessDenied:true
                }
            })
            return of(true)
        }

    } 
    
    canActivateChild(route:ActivatedRouteSnapshot, state:RouterStateSnapshot):Observable<boolean>{
        console.log('IS AUTH FROM GUARD',this.auth.isAuthenticated());
        return this.canActivate(route, state)
    }
    

}