import { Component, OnInit } from '@angular/core';
import { ApiService } from '../shared/services/api.service';

@Component({
  selector: 'app-overview-page',
  templateUrl: './overview-page.component.html',
  styleUrls: ['./overview-page.component.scss']
})
export class OverviewPageComponent implements OnInit {

  constructor(private router:ApiService) {
    
  }
   

  ngOnInit(): void {
    this.router.getCategoriesApi().subscribe(
      
      
      (x)=>{console.log('YOOO')}
      
    )
  }
}
