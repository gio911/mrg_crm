import { Component, OnInit} from '@angular/core';
import { map } from 'rxjs/operators';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';

import { ApiService } from 'src/services/api.service';


@Component({
  selector: 'app-categories',
  templateUrl: './categories.component.html',
  styleUrls: ['./categories.component.scss']
})
export class CategoriesComponent implements OnInit {

  categoriesList={results:[]}

  /** Based on the screen size, switch from standard to one column per row */
  cards = this.breakpointObserver.observe(Breakpoints.Handset).pipe(
    map(({ matches }) => {
      if (matches) {
        
        
        return [
          { title: 'Card 1', cols: 1, rows: 1 },
          
        ];
      }

      return [
        { title: 'Card 1', cols: 1, rows: 1 },
        
      ];
    })
  );

  constructor(private breakpointObserver: BreakpointObserver, private apiService:ApiService) {
    this.getCategoriesList()
  }

  ngOnInit(){
    // this.getCategoriesList()
  }

  getCategoriesList(){

    this.apiService.getCategoriesApi().subscribe((res:any)=>{
      this.categoriesList = res
      console.log(this.categoriesList);
  }
    )

}
}
