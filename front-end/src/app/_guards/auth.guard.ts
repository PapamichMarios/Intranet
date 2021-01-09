import {Injectable} from '@angular/core';
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot} from '@angular/router';
import { LocalStorageService } from '../_services/local-storage.service';
// import { Permission } from '../_models/auth/permission.model';

@Injectable()
export class AuthGuard implements CanActivate {

  constructor(
    private router: Router,
    private localStorageService: LocalStorageService) { }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
    if (this.localStorageService.authFromLocalStorage != null) {
      return true;
    }

    this.router.navigate(['/auth/login'], {queryParams: {returnUrl: state.url}});
    return false;
  }
}

