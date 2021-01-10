import { Component, OnInit } from '@angular/core';
import { RoleEnum } from 'src/app/_enums/role.enum';
import { User } from 'src/app/_models/user.model';
import { UserService } from 'src/app/_services/user.service';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.scss']
})
export class UsersComponent implements OnInit {

  users: User[];
  displayedColumns: string[] = ['role', 'firstName', 'lastName', 'email'];
  roleEnum = RoleEnum;
  
  constructor(
    private userService: UserService
  ) { }

  ngOnInit(): void {
    this.getAllUsers();
  }

  getAllUsers() : void {
    this.userService.getAllUsers().subscribe(
      response => {
        console.log(response);
        this.users = response;
      }
    );
  }
}
