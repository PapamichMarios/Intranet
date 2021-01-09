import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { LoginRequest } from '../_requests/auth/login.request';
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

  logout() {
    this.localStorageService.removeAuthFromLocalStorage();
    this.router.navigate(['/auth/login'], {
      queryParams: {},
    });
  }
}
