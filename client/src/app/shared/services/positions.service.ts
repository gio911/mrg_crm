import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { Message, Position } from "../interfaces";


@Injectable({
    providedIn:'root'
})
export class PositionsService{
    
    constructor(private http:HttpClient){

    }

    fetch(categoryId:string):Observable<Position[]>{

        return this.http.get<Position[]>(`/api/product_list/${categoryId}/`)

    }

    create(position:Position):Observable<Position>{
        return this.http.post<Position>('/api/add_product/', position)
    }

    update(position:Position):Observable<Position>{
        return this.http.put<Position>(`/api/add_product/${position.id}`, position)
    }

    delete(position:Position):Observable<Message>{
        return this.http.delete<Message>(`/api/delete_product/${position.id}/`)
    }

}