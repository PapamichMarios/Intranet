import {
    HttpEvent,
    HttpInterceptor,
    HttpHandler,
    HttpRequest,
    HttpResponse,
    HttpErrorResponse
   } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { Injectable } from '@angular/core';
import { catchError, retry } from 'rxjs/operators';
import { ErrorService } from '../_services/utilities/error.service';
import { Exceptions } from '../_models/exception/exceptions.model';

@Injectable()
export class HttpErrorInterceptor implements HttpInterceptor {

    constructor(public errorService: ErrorService) { }

    intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {

      return next.handle(request)
        .pipe(
          retry(1),
          catchError( (error: HttpErrorResponse) => {
            console.log(error);
            let errorMessage = '';

            // client-side error
            // if (error instanceof ErrorEvent) {
            //     errorMessage = `Error: ${error.error.message}`;
            // }

            // server-side error
            if (error instanceof HttpErrorResponse) {

              let message;
              if(error.error.type != null) {
                  message = error.error.type;
              } else {
                  message = 'GenericMessage'
              }

              this.errorService.throwError(Exceptions[message]);
            }

            return throwError(errorMessage);
        })
      )
    }
}