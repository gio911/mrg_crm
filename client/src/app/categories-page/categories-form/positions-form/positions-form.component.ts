import { AfterViewInit, Component, ElementRef, Input, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { MaterialInstance, MaterialService } from 'src/app/shared/classes/material.service';
import { Position } from 'src/app/shared/interfaces';
import { PositionsService } from 'src/app/shared/services/positions.service';


@Component({
  selector: 'app-positions-form',
  templateUrl: './positions-form.component.html',
  styleUrls: ['./positions-form.component.css']
})
export class PositionsFormComponent implements OnInit, AfterViewInit, OnDestroy {

  @Input('categoryId') categoryId:string 
  @ViewChild('modal') modalRef:ElementRef
  positionId:any=null
  positions:Position[]=[]
  loading=false
  modal:MaterialInstance
  form:FormGroup

  constructor(private positionsService:PositionsService) { }

  ngOnInit(): void {

    this.form = new FormGroup({
      name:new FormControl(null, Validators.required),
      price:new FormControl(null, [Validators.required, Validators.min(1) ])
    })

    this.loading=true
    this.positionsService.fetch(this.categoryId).
      subscribe(
        (positions)=>{
          console.log("POSITIONS",positions);
          
          this.positions=positions['results']
        }
      )
      this.loading=false
  }

  ngOnDestroy(): void {
    this.modal.destroy()
  }

  ngAfterViewInit(){
    this.modal = MaterialService.initModal(this.modalRef)
  }

  onSelectPosition(position:Position){
    // this.positionId=position.id
    this.modal.open()
    this.form.patchValue({
      name:position.name,
      price:position.price
    })

    MaterialService.updateTextInputs()
  }

  onAddPosition(){
    this.positionId=null
    this.form.reset({
      name:null,
      price:1
    })
    this.modal.open()
    MaterialService.updateTextInputs()

  }

  onCancel(){
    this.modal.close()
  }

  onSubmit(){
    this.form.disable()
    const newPosition={
      name:this.form.value.name,
      price:this.form.value.price,
      category:this.categoryId,
      id:''
    }

    const completed=()=>{
      this.modal.close()
      this.form.reset({name:'', price:1})
      this.form.enable()
    }



    if(this.positionId){
      newPosition.id=this.positionId
      this.positionsService.update(newPosition).subscribe(
        (position)=>{
          const idx = this.positions.findIndex(p=>p.id===position.id)
          this.positions[idx] = position
          MaterialService.toast("Changes were saved.")
          
        }, 
        error=>{MaterialService.toast(error.error.detail)},
        completed
      )
    }else{
      this.positionsService.create(newPosition).subscribe(
        (position)=>{
          MaterialService.toast('Position was created')
          this.positions.push(position)
      },
      (error)=>{
        this.form.enable()
        MaterialService.toast(error.error.detail)
      },
       completed
      
      )
    }

  }

  onDeletePosition(event:Event, position:Position){
    event.stopPropagation()
    const decision = window.confirm(`Are you sure to delete ${position.name}?`)

    if(decision){
      const idx = this.positions.findIndex(p=>p.id===position.id)
      this.positions.splice(idx,1)
      this.positionsService.delete(position).subscribe(
        (response)=>{MaterialService.toast(response.message)},
        error=>{MaterialService.toast(error.error.deteil)}
      )
    }
  }

}
