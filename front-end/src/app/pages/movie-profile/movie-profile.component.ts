import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Movie } from 'src/app/_models/movie.model';
import { User } from 'src/app/_models/user.model';
import { LocalStorageService } from 'src/app/_services/local-storage.service';
import { MovieService } from 'src/app/_services/movie.service';

@Component({
  selector: 'app-movie-profile',
  templateUrl: './movie-profile.component.html',
  styleUrls: ['./movie-profile.component.scss']
})
export class MovieProfileComponent implements OnInit {

  movie: Movie;
  hasRated: boolean;
  loggedIn: any;

  constructor(
    private activatedRoute: ActivatedRoute,
    private movieService: MovieService,
    private localStorageService: LocalStorageService,
    public router: Router
  ) { }

  ngOnInit(): void {
    this.movie = new Movie();
    this.loggedIn = this.localStorageService.authFromLocalStorage;
    let movieId = this.activatedRoute.snapshot.paramMap.get('id');
    this.getMovieById(movieId);
  }

  getMovieById(movieId: string) {
    this.movieService.getMovieById(movieId).subscribe(
      response => {
        console.log(response);
        this.movie = response.movie;
        this.hasRated = response.hasRated;
      }
    )
  }
}
