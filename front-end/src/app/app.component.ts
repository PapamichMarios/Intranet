import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { map, shareReplay } from 'rxjs/operators';
import { RoleEnum } from './_enums/role.enum';
import { Auth } from './_models/auth.model';
import { Genre } from './_models/genre.model';
import { Role } from './_models/role.model';
import { AuthService } from './_services/auth.service';
import { LocalStorageService } from './_services/local-storage.service';
import { MovieService } from './_services/movie.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  
  title = 'front-end';

  isHandset$: Observable<boolean> = this.breakpointObserver.observe(Breakpoints.Handset)
    .pipe(
      map(result => result.matches),
      shareReplay()
    );

  constructor(
    private breakpointObserver: BreakpointObserver,
    private localStorageService: LocalStorageService,
    private authService: AuthService,
    public router: Router,
    private movieService: MovieService) {}

  loggedIn: Auth;
  isAdmin: Role;
  searchString: string;
  genres: Genre[];

  ngOnInit(): void {
    this.refreshAuthentication();
    this.getMovieGenres();
  }

  refreshAuthentication() {
    this.loggedIn = this.localStorageService.authFromLocalStorage;
    let roles = this.localStorageService.rolesFromLocalStorage;
    this.isAdmin = roles != null ? roles.find(role => RoleEnum[role.name] === RoleEnum.ROLE_ADMINISTRATOR) : null;
  }

  getMovieGenres() {
    this.movieService.getMovieGenres().subscribe(
      response => {
        this.genres = response;
      }
    )
  }

  search() {
    console.log(this.searchString);
    this.router.navigateByUrl("/movies?search=" + this.searchString);
  }

  logout() {
    this.authService.logout();
    this.refreshAuthentication();
  }
}
