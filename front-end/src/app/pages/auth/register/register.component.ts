import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { RegisterRequest } from 'src/app/_requests/auth/register.request';
import { AuthService } from 'src/app/_services/auth.service';
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
    private router: Router) { }

  ngOnInit(): void {
    this.registerRequest = new RegisterRequest();
  }

  register() {
    this.authService.register(this.registerRequest).subscribe(
      response => {
        console.log(response);
        if (response != null) {
          location.reload();
          this.router.navigateByUrl(environment.defaultUrl);
        }
      }
    )
  }
}
