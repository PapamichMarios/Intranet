import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { map, tap } from 'rxjs/operators';
import { RegisterRequest } from 'src/app/_requests/auth/register.request';
import { AuthService } from 'src/app/_services/auth.service';
import { LocalStorageService } from 'src/app/_services/local-storage.service';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  registerRequest: RegisterRequest;
  confirmPasswordInput: string;

  constructor(
    private authService: AuthService,
    private router: Router,
    private localStorageService: LocalStorageService) { }

  ngOnInit(): void {
    this.registerRequest = new RegisterRequest();
  }

  register() {
    this.authService.register(this.registerRequest).pipe(
      map((response: any) => {
        this.localStorageService.authLocalStorage = response.auth;
        this.localStorageService.rolesLocalStorage = response.roles;
        return response;
      })
    )
    .subscribe(
      response => {
        console.log(response);
        if (response != null) {
          location.reload();
          this.router.navigateByUrl(environment.defaultUrl);
        }
      }
    );
  }
}
