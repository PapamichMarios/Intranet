import {Injectable} from '@angular/core';
import {
  HttpErrorResponse,
  HttpHandler,
  HttpHeaderResponse,
  HttpHeaders,
  HttpInterceptor,
  HttpProgressEvent,
  HttpRequest,
  HttpResponse,
  HttpSentEvent,
  HttpUserEvent
} from '@angular/common/http';
import {BehaviorSubject, Observable, throwError} from 'rxjs';
import {catchError, filter, finalize, switchMap, take} from 'rxjs/operators';
import { AuthService } from '../_services/auth.service';
import { LocalStorageService } from '../_services/local-storage.service';


@Injectable()
export class TokenInterceptor implements HttpInterceptor {

  isRefreshingToken: boolean = false;
  tokenSubject: BehaviorSubject<string> = new BehaviorSubject<string>(null);

  constructor(
    private authService: AuthService,
    private localStorageService: LocalStorageService) {
  }

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpSentEvent | HttpHeaderResponse | HttpProgressEvent | HttpResponse<any> | HttpUserEvent<any> | any> {

    let accessToken = this.localStorageService.authFromLocalStorage == null ? '' : this.localStorageService.authFromLocalStorage.token;
    
    return next
    .handle(this.addTokenToRequest(request, accessToken))
    .pipe(
      catchError(err => {
        if (err instanceof HttpErrorResponse) {
          switch ((<HttpErrorResponse>err).status) {
            case 401:
              return this.handle401Error(request, next);
            case 400:
              return <any>this.authService.logout();
            default:
              return throwError(err);
          }
        } else {
          return throwError(err);
        }
      }));
  }

  private addTokenToRequest(request: HttpRequest<any>, token: string): HttpRequest<any> {
    let headers = new HttpHeaders();
    headers = headers.append('Authorization', `Bearer ${token}`);

    return request.clone({headers});
  }

  private handle401Error(request: HttpRequest<any>, next: HttpHandler) {

    if (!this.isRefreshingToken) {
      this.isRefreshingToken = true;
      // Reset here so that the following requests wait until the token
      // comes back from the refreshToken call.
      this.tokenSubject.next(null);

      return <any>this.authService.logout();
    }
  }
}
