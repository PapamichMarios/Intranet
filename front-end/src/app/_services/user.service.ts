import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { map, switchMap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { User } from '../_models/user.model';
import { ChangePasswordRequest } from '../_requests/auth/change-password.request';
import { LoginRequest } from '../_requests/auth/login.request';
import { RegisterRequest } from '../_requests/auth/register.request';
import { LocalStorageService } from './local-storage.service';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(
    private http: HttpClient,
    private localStorageService: LocalStorageService,
    private router: Router) { }

  
  getAllUsers() : Observable<any> {
    const url = environment.serverUrl + environment.users_all;
    return this.http.get(url).pipe(
      map(response => {
        return response['data'];
      })
    )
  }

  myProfile() : Observable<any> {
    const url = environment.serverUrl + environment.profile;
    return this.http.get(url).pipe(
      map( response => {
        return response['data'];
      })
    )
  }


  updateMyProfile(user: User): Observable<any> {
    const url = environment.serverUrl + environment.profile;
    return this.http.put(url, user).pipe(
        map( response => {
            return response['data'];
        })
    )
  }


  changePassword(changePasswordRequest: ChangePasswordRequest): Observable<any> {
    const url = environment.serverUrl + environment.change_password;
    return this.http.put(url, changePasswordRequest).pipe(
        map(response => {
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
