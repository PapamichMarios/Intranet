import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AuthGuard } from 'src/app/_guards/auth.guard';
import { LoggedGuard } from 'src/app/_guards/logged.guard';
import { LoginComponent } from './login/login.component';
import { MyRatingsComponent } from './my-ratings/my-ratings.component';
import { ProfileComponent } from './profile/profile.component';
import { RegisterComponent } from './register/register.component';


const routes: Routes = [
  {
    path: 'login',
    canActivate: [LoggedGuard],
    component: LoginComponent
  },
  {
    path: 'register',
    canActivate: [LoggedGuard],
    component: RegisterComponent
  },
  {
    path: 'profile',
    canActivate: [AuthGuard],
    component: ProfileComponent
  },
  {
    path: 'my-ratings',
    canActivate: [AuthGuard],
    component: MyRatingsComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AuthRoutingModule { }
