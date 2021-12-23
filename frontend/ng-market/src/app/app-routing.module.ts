import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CategoriesComponent } from './categories/categories.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { OverviewPageComponent } from './overview-page/overview-page.component';
import { ProductsComponent } from './products/products.component';
import { RegisterPageComponent } from './register-page/register-page.component';
import { AuthGuard } from './shared/classes/auth.guard';
import { AuthLayoutComponent } from './shared/layouts/auth-layout/auth-layout.component';
import { SiteLayoutComponent } from './shared/layouts/site-layout/site-layout.component';


const routes: Routes = [

  {path:'', component: AuthLayoutComponent, children:[ 
    {path:'', redirectTo:'/login', pathMatch:'full'},
    {path:'login', component: LoginPageComponent},
    {path:'register', component: RegisterPageComponent}
  ]},
  {path:'', component: SiteLayoutComponent, canActivate:[AuthGuard], children:[
    {path:'overview', component:OverviewPageComponent },
    {path:'home', component: CategoriesComponent } 
   ]},

  {path:'home', component:CategoriesComponent},
  {path:'products/:id', component:ProductsComponent},
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {
    initialNavigation: 'enabled'
})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
