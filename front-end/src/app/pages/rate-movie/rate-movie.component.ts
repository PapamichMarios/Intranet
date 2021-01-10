import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Movie } from 'src/app/_models/movie.model';
import { Rating } from 'src/app/_models/rating.model';
import { MovieService } from 'src/app/_services/movie.service';
import { SuccessService } from 'src/app/_services/utilities/success.service';

@Component({
  selector: 'app-rate-movie',
  templateUrl: './rate-movie.component.html',
  styleUrls: ['./rate-movie.component.scss']
})
export class RateMovieComponent implements OnInit {

  rating: Rating;

  constructor(
    private movieService: MovieService,
    private activatedRoute: ActivatedRoute,
    private successService: SuccessService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.rating = new Rating();
  }

  rate() {
    this.rating.movieId = parseInt(this.activatedRoute.snapshot.paramMap.get('id'));
    this.movieService.rateMovie(this.rating).subscribe(
      response => {
        console.log(response);
        this.successService.throwSuccess("Movie rated successfully");
        this.router.navigateByUrl("/movies");
      }
    )
  }
}
