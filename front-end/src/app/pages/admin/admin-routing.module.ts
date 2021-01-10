import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AdminGuard } from 'src/app/_guards/admin.guard';
import { CreateMovieComponent } from './create-movie/create-movie.component';
import { UsersComponent } from './users/users.component';


const routes: Routes = [
  {
    path: 'users',
    canActivate: [AdminGuard],
    component: UsersComponent
  },
  {
    path: 'movies/create',
    canActivate: [AdminGuard],
    component: CreateMovieComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AdminRoutingModule { }
