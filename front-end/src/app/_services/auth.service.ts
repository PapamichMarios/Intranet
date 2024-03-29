import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { map, switchMap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { LoginRequest } from '../_requests/auth/login.request';
import { RegisterRequest } from '../_requests/auth/register.request';
import { LocalStorageService } from './local-storage.service';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private http: HttpClient,
    private localStorageService: LocalStorageService,
    private router: Router) { }

  login(loginRequest: LoginRequest) : Observable<any>{
    const url = environment.serverUrl + environment.login;
    return this.http.post(url, loginRequest).pipe(
      map( response => {
        return response['data'];
      })
    ) 
  }

  
  register(registerRequest: RegisterRequest) : Observable<any> {
    const url = environment.serverUrl + environment.register;
    return this.http.post(url, registerRequest).pipe(
      map(response => {return response['data']}),
      switchMap((response) => {
        let loginRequest = new LoginRequest();
        loginRequest.username = registerRequest.username;
        loginRequest.password = registerRequest.password;
        return this.login(loginRequest);
      })
    );
  }


  logout() {
    this.localStorageService.removeAuthFromLocalStorage();
    this.localStorageService.removeRolesFromLocalStorage();
    this.router.navigate(['/auth/login'], {
      queryParams: {},
    });
  }
}
