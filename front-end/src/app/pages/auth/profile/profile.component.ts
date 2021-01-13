import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { Auth } from 'src/app/_models/auth.model';
import { User } from 'src/app/_models/user.model';
import { ChangePasswordRequest } from 'src/app/_requests/auth/change-password.request';
import { AuthService } from 'src/app/_services/auth.service';
import { UserService } from 'src/app/_services/user.service';
import { SuccessService } from 'src/app/_services/utilities/success.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  edit: boolean = false;

  user: User;
  staticUser: User;

  changePasswordRequest: ChangePasswordRequest;
  confirmPassword: string;

  constructor(
    private userService: UserService,
    private successService: SuccessService,
    private authService: AuthService
  ) { }

  ngOnInit(): void {
    this.user = new User();
    this.changePasswordRequest = new ChangePasswordRequest();
    this.userService.myProfile().subscribe(
      response => {
        console.log(response);
        this.user = response;
        this.staticUser = JSON.parse(JSON.stringify(this.user));
        this.changePasswordRequest.id = this.user.id;
      }
    )
  }

  toggleEdit() {
    this.edit = !this.edit;
    if (!this.edit) this.user = JSON.parse(JSON.stringify(this.staticUser));
  }

  updateProfile() {
    this.userService.updateMyProfile(this.user)
    .subscribe(response => {
      console.log(response);
      this.successService.throwSuccess('Profile updated successfully! Please login again.');
      this.authService.logout();
      location.reload();
    });
  }

  updatePassword() {
    this.userService.changePassword(this.changePasswordRequest).subscribe(
      response => {
        console.log(response);
        this.successService.throwSuccess('Password changed successfully!')
      }
    )
  }

}
