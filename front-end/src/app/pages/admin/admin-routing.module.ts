import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AdminGuard } from 'src/app/_guards/admin.guard';
import { UsersComponent } from './users/users.component';


const routes: Routes = [
  {
    path: 'users',
    canActivate: [AdminGuard],
    component: UsersComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AdminRoutingModule { }
