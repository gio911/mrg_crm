import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Category } from '../shared/interfaces';
import { CategoriesService } from '../shared/services/categories.service';

@Component({
  selector: 'app-categories-page',
  templateUrl: './categories-page.component.html',
  styleUrls: ['./categories-page.component.css']
})
export class CategoriesPageComponent implements OnInit {

  // loading = false
  // categories:Category[]=[]
  categories$:Observable<Category[]>
  constructor(private categoriesService:CategoriesService) { }

  ngOnInit(): void {
    // this.loading = true
    // this.categoriesService.fetch().subscribe((categories)=>{
    //   this.loading = false
    //   this.categories = categories['results']
    //     console.log('CATEGORIES FROM SERVER', categories);
        
    //})

    this.categories$=this.categoriesService.fetch()

  }

}
