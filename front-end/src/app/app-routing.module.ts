import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { LoginComponent } from './pages/auth/login/login.component';
import { RegisterComponent } from './pages/auth/register/register.component';
import { MovieProfileComponent } from './pages/movie-profile/movie-profile.component';
import { MoviesComponent } from './pages/movies/movies.component';
import { RateMovieComponent } from './pages/rate-movie/rate-movie.component';
import { TopMoviesComponent } from './pages/top-movies/top-movies.component';
import { AdminGuard } from './_guards/admin.guard';
import { AuthGuard } from './_guards/auth.guard';
import { LoggedGuard } from './_guards/logged.guard';


const routes: Routes = [
  {
    path: 'auth',
    loadChildren: () => import('./pages/auth/auth.module').then((m) => m.AuthModule),
  },
  {
    path: 'admin',
    canActivate: [AdminGuard],
    loadChildren: () => import('./pages/admin/admin.module').then((m) => m.AdminModule),
  },
  {
    path: 'movies',
    component: MoviesComponent
  },
  {
    path: 'movie/:id',
    component: MovieProfileComponent
  },
  {
    path: 'movie/:id/rate',
    canActivate: [AuthGuard],
    component: RateMovieComponent
  },
  {path: '**', redirectTo: 'movies'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
