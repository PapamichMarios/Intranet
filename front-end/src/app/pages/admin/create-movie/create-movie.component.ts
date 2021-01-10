import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Genre } from 'src/app/_models/genre.model';
import { Movie } from 'src/app/_models/movie.model';
import { MovieService } from 'src/app/_services/movie.service';
import { SuccessService } from 'src/app/_services/utilities/success.service';

@Component({
  selector: 'app-create-movie',
  templateUrl: './create-movie.component.html',
  styleUrls: ['./create-movie.component.scss']
})
export class CreateMovieComponent implements OnInit {

  movie: Movie;
  genres: Genre[];

  constructor(
    private movieService: MovieService,
    private successService: SuccessService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.movie = new Movie();
    this.getMovieGenres();
  }

  create() {
    this.movieService.createMovie(this.movie).subscribe(
      response => {
        console.log(response);
        this.successService.throwSuccess('Movie added successfully!');
        this.router.navigateByUrl('/movies');
      }
    )
  }

  getMovieGenres() {
    this.movieService.getMovieGenres().subscribe(
      response => {
        console.log(response);
        this.genres = response;
      }
    );
  }
}
