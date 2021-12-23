import { Component, OnDestroy, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router, Params } from '@angular/router';
import { Subscription } from 'rxjs';
import { MaterialService } from '../shared/classes/material.service';
import { AuthService } from '../shared/services/auth.service';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss']
})
export class LoginPageComponent implements OnInit, OnDestroy {

  form:FormGroup
  aSub:Subscription

  constructor(private auth:AuthService,
              private router:Router,
              private route:ActivatedRoute) { }


// route:ActivatedRoute   в этой переменной будет находиться все информация по текущему роуту 

  ngOnDestroy(){
    if(this.aSub){
      this.aSub.unsubscribe()
    }
  }

  ngOnInit(): void {
  
    this.form = new FormGroup({
      email: new FormControl(null, [Validators.required, Validators.email]),
      password: new FormControl(null, [Validators.required, Validators.minLength(6)])
    })
    this.route.queryParams.subscribe((params:Params)=>{
      if(params['registered']){
        alert('Now you can enter to the app')

      } else if(params['accessDenied']){
        
        alert('You Hawe to Auth at the beginning')
      }
    })
  }

  onSubmit(){
    this.form.disable()
    this.aSub = this.auth.login(this.form.value).subscribe(
      (x)=>{console.log('HIIIIIH',x);
      
        this.router.navigate(['/overview'])},
      (error)=>{
        alert(error.error.detail)
        MaterialService.toast('HI THERE')
        this.form.enable()
      }
      
    )
  }
}
