import {Injectable} from '@angular/core';
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot} from '@angular/router';
import { Permission } from '../_models/auth/permission.model';

@Injectable()
export class AuthGuard implements CanActivate {

  constructor(private router: Router) { }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {

    if (localStorage.getItem('permissions') && localStorage.getItem('role')) {
      const permissions = <Permission[]>JSON.parse(localStorage.getItem('permissions'));
      const routePermissions = route.data['permissions'] ? <string[]>route.data['permissions'] : null;
      
      if (!routePermissions || (permissions && routePermissions.some(per => permissions.some(p => p.key === per)))) {
        return true;
      } else {
        this.router.navigate(['/dashboard']);
        return false;
      }
    }

    this.router.navigate(['/auth/login'], {queryParams: {returnUrl: state.url}});
    return false;
  }
}

