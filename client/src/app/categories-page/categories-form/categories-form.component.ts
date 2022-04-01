import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { materialize, of, switchMap } from 'rxjs';
import { MaterialService } from 'src/app/shared/classes/material.service';
import { Category } from 'src/app/shared/interfaces';
import { CategoriesService } from 'src/app/shared/services/categories.service';

@Component({
  selector: 'app-categories-form',
  templateUrl: './categories-form.component.html',
  styleUrls: ['./categories-form.component.css']
})
export class CategoriesFormComponent implements OnInit {

  isNew=true
  form:FormGroup
  image:File
  imagePreview:string | ArrayBuffer=''
  category:Category

  @ViewChild('input') inputRef:ElementRef

  constructor(private route:ActivatedRoute,
              private categoriesService:CategoriesService,
              private router:Router) { }

  ngOnInit(): void {


    this.form = new FormGroup({
      name:new FormControl(null, Validators.required),

    })

    this.form.disable()

    // this.route.params.subscribe((params:Params)=>{
    //   if(params['id']){
    //     this.isNew=false
    //   }

    // }) 


    this.route.params.
        pipe(
          switchMap(
            (params:Params)=>{
              if(params['id']){
                this.isNew=false
               return this.categoriesService.getById(params['id'])
              }
              return of(null)
            }
            )
        ).
        subscribe(
          (category:Category)=>{
            if(category){
              console.log(category);
              this.category = category
              this.form.patchValue({
                name:category.name
              })
              this.imagePreview = category['image']
              MaterialService.updateTextInputs()
            }
            this.form.enable()
          },
          error=>MaterialService.toast(error.error.detail)
        )

  }
  onSubmit(){
    let obs$
    this.form.disable()

    if(this.isNew){
      obs$=this.categoriesService.create(this.form.value.name, this.image)
    } else {
      obs$=this.categoriesService.update(this.category.id, this.form.value.name, this.image)
    }

    obs$.subscribe(
      category=>{
        this.category=category
        MaterialService.toast('The Category were created')
        this.router.navigate(['/categories'])
        this.form.enable()
      },
      error=>{
        MaterialService.toast(error.error.detail)
        this.form.enable()
      }
    )
  } 

  triggerClick(){
    this.inputRef.nativeElement.click()
  }

  deleteCategory(){
    
    const desision = window.confirm(`Are you sure you want to delete a category ${this.category.name}?`)
    if (desision){
      this.categoriesService.delete(this.category.id).subscribe(
        (response)=>{MaterialService.toast(response.message)},
        (error)=>MaterialService.toast(error.error.detail),
        ()=>this.router.navigate(['/categories'])
      )
    }
  }

  onFileUpload(event:any){

    const file = event.target.files[0]
    this.image = file

    const reader = new FileReader()  //превью картинки

    reader.onload = () =>{
      this.imagePreview= reader.result
    }

    reader.readAsDataURL(file)

  }
}
