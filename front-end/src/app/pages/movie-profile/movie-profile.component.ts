import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Movie } from 'src/app/_models/movie.model';
import { MovieService } from 'src/app/_services/movie.service';

@Component({
  selector: 'app-movie-profile',
  templateUrl: './movie-profile.component.html',
  styleUrls: ['./movie-profile.component.scss']
})
export class MovieProfileComponent implements OnInit {

  movie: Movie;

  constructor(
    private activatedRoute: ActivatedRoute,
    private movieService: MovieService
  ) { }

  ngOnInit(): void {
    this.movie = new Movie();
    let movieId = this.activatedRoute.snapshot.paramMap.get('id');
    this.getMovieById(movieId);
  }

  getMovieById(movieId: string) {
    this.movieService.getMovieById(movieId).subscribe(
      response => {
        console.log(response);
        this.movie = response;
      }
    )
  }
}
