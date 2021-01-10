import { Component, OnInit } from '@angular/core';
import { Rating } from 'src/app/_models/rating.model';
import { UserService } from 'src/app/_services/user.service';

@Component({
  selector: 'app-my-ratings',
  templateUrl: './my-ratings.component.html',
  styleUrls: ['./my-ratings.component.scss']
})
export class MyRatingsComponent implements OnInit {
  
  ratings: Rating[];
  displayedColumns: string[] = ['rating', 'comment', 'movie'];
  
  constructor(
    private userService: UserService
  ) { }

  ngOnInit(): void {
    this.getMyProfile();
  }

  getMyProfile() : void {
    this.userService.myProfile().subscribe(
      response => {
        console.log(response);
        this.ratings = response.ratings;
      }
    );
  }
}
