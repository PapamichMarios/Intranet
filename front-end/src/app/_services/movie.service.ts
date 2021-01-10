import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { map, switchMap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { User } from '../_models/user.model';
import { ChangePasswordRequest } from '../_requests/auth/change-password.request';
import { LoginRequest } from '../_requests/auth/login.request';
import { RegisterRequest } from '../_requests/auth/register.request';
import { LocalStorageService } from './local-storage.service';

@Injectable({
  providedIn: 'root'
})
export class MovieService {

  constructor(
    private http: HttpClient) { }

  
  getAllMovies() : Observable<any> {
    const url = environment.serverUrl + environment.movies_all;
    return this.http.get(url).pipe(
      map(response => {
        return response['data'];
      })
    )
  }

  
  getMovieByName(name: string): Observable<any> {
    const url = environment.serverUrl + environment.movies_by_name;
    let params = new HttpParams().append('name', name);
    return this.http.get(url, {params: params}).pipe(
        map(response=> {
            return response['data'];
        })
    )
  }

  getMovieByGenre(genre: string): Observable<any> {
    const url = environment.serverUrl + environment.movies_by_genre + genre;
    return this.http.get(url).pipe(
        map(response=> {
            return response['data'];
        })
    )
  }

  getMovieGenres(): Observable<any> {
    const url = environment.serverUrl + environment.movie_genres;
    return this.http.get(url).pipe(
        map(response => {
            return response['data'];
        })
    )
  }
  
}
