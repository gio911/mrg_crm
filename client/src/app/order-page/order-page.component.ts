import { AfterViewChecked, AfterViewInit, Component, ElementRef, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute, NavigationEnd, Params, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { MaterialInstance, MaterialService } from '../shared/classes/material.service';
import { OrderPosition } from '../shared/interfaces';
import { OrdersService } from '../shared/services/orders.service';
import { OrderService } from './order.service';

@Component({
  selector: 'app-order-page',
  templateUrl: './order-page.component.html',
  styleUrls: ['./order-page.component.css'],
  providers:[OrderService]
})
export class OrderPageComponent implements OnInit, OnDestroy, AfterViewInit {

  @ViewChild('modal') modalRef:ElementRef
  isRoot:boolean
  modal:MaterialInstance
  loading=false
  oSub:Subscription

  constructor(private router:Router,
              public order:OrderService,
              private ordersService:OrdersService) { }

  ngOnInit(): void {
      this.isRoot = this.router.url === '/order'
      this.router.events.subscribe(
        event=>{
          if(event instanceof NavigationEnd){
            this.isRoot=this.router.url === '/order'
          }
        }
      )
  }

  ngAfterViewInit(): void {
      this.modal = MaterialService.initModal(this.modalRef)
  }

  ngOnDestroy(){
    this.modal.destroy()
    if(this.oSub){
      this.oSub.unsubscribe()
    }
  }

  removePosition(orderPosition:OrderPosition){
    this.order.remove(orderPosition)
  }

  open(){
    this.modal.open()
  }

  cancel(){
    this.modal.close()
  }

  submit(){
    this.loading=true
    const order = {
      list:this.order.list.map(item=>{
        delete item.id
        return item
      })
    }
    this.oSub=this.ordersService.create(order).subscribe(
      newOrder => {
        
        console.log(newOrder);
        this.loading=false
        MaterialService.toast(`Order # ${newOrder.id} was added`)
        this.order.clear()
      },
      error=>{MaterialService.toast(error.error.detail)},
      ()=>{
        this.modal.close()
      }
    )


  }

}
