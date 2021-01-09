import {Injectable} from '@angular/core';
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot} from '@angular/router';
import { LocalStorageService } from '../_services/local-storage.service';

@Injectable()
export class LoggedGuard implements CanActivate {

  constructor(
    private router: Router,
    private localStorageService: LocalStorageService) { }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
    if (this.localStorageService.authFromLocalStorage != null) {
        this.router.navigate(['/dashboard']);
        return false;
    }

    return true;
  }
}

