import { Injectable } from "@angular/core";
import { CanActivate, Router, ActivatedRouteSnapshot, RouterStateSnapshot } from "@angular/router";
import { RoleEnum } from "../_enums/role.enum";
import { Auth } from "../_models/auth.model";
import { LocalStorageService } from "../_services/local-storage.service";

@Injectable()
export class AdminGuard implements CanActivate {

  constructor(
    private router: Router,
    private localStorageService: LocalStorageService) { }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
    let auth = this.localStorageService.authFromLocalStorage;
    let roles = this.localStorageService.rolesFromLocalStorage;
    let isAdmin = roles.find(role => RoleEnum[role.name] === RoleEnum.ROLE_ADMINISTRATOR)
    
    if (auth == null || roles == null || isAdmin == null) {
        this.router.navigate(['/auth/login'], {queryParams: {returnUrl: state.url}});
        return false;
    }

    return true;
  }
}