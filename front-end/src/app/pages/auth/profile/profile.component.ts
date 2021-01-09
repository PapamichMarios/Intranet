import { Component, OnInit } from '@angular/core';
import { Auth } from 'src/app/_models/auth.model';
import { User } from 'src/app/_models/user.model';
import { AuthService } from 'src/app/_services/auth.service';
import { UserService } from 'src/app/_services/user.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  user: User;
  staticUser: User;
  edit: boolean = false;

  constructor(
    private userService: UserService
  ) { }

  ngOnInit(): void {
    this.userService.myProfile().subscribe(
      response => {
        console.log(response);
        this.user = response;
        this.staticUser = JSON.parse(JSON.stringify(this.user));
      }
    )
  }

  toggleEdit() {
    this.edit = !this.edit;
    if (!this.edit) this.user = JSON.parse(JSON.stringify(this.staticUser));
  }

  updateProfile() {

  }

  updatePassword() {

  }

}
