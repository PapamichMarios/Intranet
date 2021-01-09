import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { catchError, switchMap, tap } from 'rxjs/operators';
import { Auth } from 'src/app/_models/auth.model';
import { LoginRequest } from 'src/app/_requests/auth/login.request';
import { AuthService } from 'src/app/_services/auth.service';
import { LocalStorageService } from 'src/app/_services/local-storage.service';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  loginRequest : LoginRequest;
  hasError: boolean = false;

  constructor(
    private authService: AuthService,
    private localStorageService: LocalStorageService,
    private router: Router) { }

  ngOnInit(): void {
    this.loginRequest = new LoginRequest();  
  }

  login() {
    this.authService.login(this.loginRequest)
    .pipe(
      tap((response: Auth) => this.localStorageService.authLocalStorage = response)
    )
    .subscribe(
      response => {
        if (response != null)
          this.router.navigateByUrl(environment.defaultUrl)
      }
    )
  }

}
