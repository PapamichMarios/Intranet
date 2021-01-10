import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { SharedModule } from './shared/shared.module';
import { AuthService } from './_services/auth.service';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { HttpErrorInterceptor } from './_interceptors/error.interceptor';
import { TokenInterceptor } from './_interceptors/token.interceptor';
import { LoggedGuard } from './_guards/logged.guard';
import { MoviesComponent } from './pages/movies/movies.component';
import { MovieProfileComponent } from './pages/movie-profile/movie-profile.component';
import { AdminGuard } from './_guards/admin.guard';
import { Auth } from './_models/auth.model';
import { AuthGuard } from './_guards/auth.guard';
import { TopMoviesComponent } from './pages/top-movies/top-movies.component';
import { RateMovieComponent } from './pages/rate-movie/rate-movie.component';

@NgModule({
  declarations: [
    AppComponent,
    MoviesComponent,
    MovieProfileComponent,
    TopMoviesComponent,
    RateMovieComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    SharedModule,
    HttpClientModule
  ],
  providers: [
    AuthService,
    LoggedGuard,
    AuthGuard,
    AdminGuard,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: TokenInterceptor,
      multi: true
    },
    {
      provide: HTTP_INTERCEPTORS,
      useClass: HttpErrorInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
