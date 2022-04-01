import { AfterViewChecked, AfterViewInit, Component, ElementRef, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute, NavigationEnd, Params, Router } from '@angular/router';
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
    this.modal.close()

    const order = {
      list:this.order.list.map(item=>{
        delete item.id
        return item
      })
    }
    this.ordersService.create(order).subscribe(
      newOrder => {
        
        
        MaterialService.toast('Order was added')
      },
      error=>{MaterialService.toast(error.error.detail)},
      ()=>{
        this.modal.close()
      }
    )

    this.modal.close()

  }

}
