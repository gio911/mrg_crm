import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from './../environments/environment';
import { AuthService } from './shared/services/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'ng-market';
  productList = {results:[]}
  categoriesList ={results:[]}

  constructor(private http:HttpClient, private auth: AuthService){
      // this.getProductsList()
      // this.getCategoriesList()
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

ngOnInit(){
  console.log('OOOPS2');
  try{
    console.log();
    
  const potentialToken = localStorage.getItem('auth-token')

  if(potentialToken!== null){
    console.log('POTENTIAL TOKEN',potentialToken);
    
    this.auth.setToken(potentialToken)
    console.log('FROM LOCAL STOREGE',this.auth.getToken());
    console.log('FROM IS AUTHEN',this.auth.isAuthenticated());
  }
  console.log('OOOPS3');
}catch{
  console.log("OOOPS4");
  
}
  
  }
}

