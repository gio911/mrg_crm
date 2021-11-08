import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http:HttpClient) { }

  getCategoriesApi(){
    return this.http.get(`${environment.backendUrl}/v1/viewsets/category`)
  }
  getProductsByCategoryId(id:number){
    return this.http.get(`${environment.backendUrl}/v1/viewsets/category/`)
  }

}
