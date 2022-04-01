import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { Order } from "../interfaces";

@Injectable({
    providedIn:'root'
})
export class OrdersService{
    constructor( private http:HttpClient){

    }

    create(order:Order):Observable<Order>{  
        console.log(order);
        
        return this.http.post<Order>('/api/order_submit/', order)
        
    }
}