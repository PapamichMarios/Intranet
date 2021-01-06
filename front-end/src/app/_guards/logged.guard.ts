import {Injectable} from '@angular/core';
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot} from '@angular/router';
import { Permission } from '../_models/auth/permission.model';

@Injectable()
export class LoggedGuard implements CanActivate {

  constructor(private router: Router) { }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
    if (localStorage.getItem('currentUser') || localStorage.getItem('permissions')) {
        this.router.navigate(['/dashboard']);
        return false;
    }

    return true;
  }
}

