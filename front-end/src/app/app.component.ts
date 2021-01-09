import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';
import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { map, shareReplay } from 'rxjs/operators';
import { Auth } from './_models/auth.model';
import { AuthService } from './_services/auth.service';
import { LocalStorageService } from './_services/local-storage.service';

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
    private authService: AuthService) {}

  loggedIn: Auth;
  searchString: string;

  ngOnInit(): void {
    this.refreshAuthentication();
  }

  refreshAuthentication() {
    this.loggedIn = this.localStorageService.authFromLocalStorage;
  }

  search() {
    console.log(this.searchString);
  }

  logout() {
    this.authService.logout();
    this.refreshAuthentication();
  }
}
