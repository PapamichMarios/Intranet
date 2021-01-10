import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, NavigationEnd, Router } from '@angular/router';
import { Movie } from 'src/app/_models/movie.model';
import { MovieService } from 'src/app/_services/movie.service';

@Component({
  selector: 'app-movies',
  templateUrl: './movies.component.html',
  styleUrls: ['./movies.component.scss']
})
export class MoviesComponent implements OnInit {

  movies: Movie[];
  
  constructor(
    private movieService: MovieService,
    private activatedRoute: ActivatedRoute,
    private router: Router
  ) { 
    router.events.subscribe((val) => {
      if (val instanceof NavigationEnd) {
        this.ngOnInit();
      }
    });
  }

  ngOnInit(): void {
    let search = this.activatedRoute.snapshot.queryParamMap.get('search');
    let genre = this.activatedRoute.snapshot.queryParamMap.get('genre');

    if (search == null && genre == null)
      this.getAllMovies();

    if (search != null)
      this.getMoviesByName(search);

    if (genre != null)
      this.getMoviesByGenre(genre);
  }

  getAllMovies() : void {
    this.movieService.getAllMovies().subscribe(
      response => {
        console.log(response);
        this.movies = response;
      }
    )
  }

  getMoviesByName(name: string): void {
    this.movieService.getMovieByName(name).subscribe(
      response => {
        console.log(response);
        this.movies = response;
      }
    )
  }

  getMoviesByGenre(name: string): void {
    this.movieService.getMovieByGenre(name).subscribe(
      response => {
        console.log(response);
        this.movies = response;
      }
    )
  }

  redirectToProfile(id: number) : void {
    this.router.navigateByUrl("movie/" + id);
  }
}
