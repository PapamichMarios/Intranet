import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Auth } from '../_models/auth.model';
import { Role } from '../_models/role.model';

@Injectable({
  providedIn: 'root'
})
export class LocalStorageService {

  private authLocalStorageToken = `${environment.appVersion}-${environment.USERDATA_KEY}`;

  constructor() { }

  /**
   * Auth token
   */
  set authLocalStorage(auth: Auth) {
    // store auth token/type
    if (auth && auth.token) {
      localStorage.setItem(this.authLocalStorageToken, JSON.stringify(auth));
    }
  }
  
  get authFromLocalStorage(): Auth {
      try {
          const authData = JSON.parse(localStorage.getItem(this.authLocalStorageToken));
          return authData;
      } catch (error) {
          console.error(error);
          return undefined;
      }
  }

  removeAuthFromLocalStorage() {
      localStorage.removeItem(this.authLocalStorageToken);
  }


  /**
   * Roles
   */
  set rolesLocalStorage(roles: Role[]) {
    if (roles) {
      localStorage.setItem('roles', JSON.stringify(roles));
    }
  }
  
  get rolesFromLocalStorage(): Role[] {
      try {
          const authData = JSON.parse(localStorage.getItem('roles'));
          return authData;
      } catch (error) {
          console.error(error);
          return undefined;
      }
  }

  removeRolesFromLocalStorage() {
      localStorage.removeItem('roles');
  }

}
