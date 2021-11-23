import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { User } from "../interfaces";

@Injectable()
export class AuthService{

    constructor(private http:HttpClient){

    }



    register(){

    }

    login(user:User){

    }

}