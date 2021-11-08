import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from './../environments/environment';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'ng-market';
  productList = {results:[]}
  categoriesList ={results:[]}

  constructor(private http:HttpClient){
      this.getProductsList()
      this.getCategoriesList()
  }


  getProductsList(){
    this.http.get(`${environment.backendUrl}/v1/generic/product_list`).subscribe((res:any)=>{
      this.productList = res
      console.log(this.productList);
      
    })
    
    
  }
  getCategoriesList(){

    this.http.get(`${environment.backendUrl}/v1/viewsets/category`).subscribe((res:any)=>{
      this.categoriesList = res
      console.log(this.categoriesList);
  }
    )

}

}