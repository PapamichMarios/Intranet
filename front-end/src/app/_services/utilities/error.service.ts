import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';

@Injectable({
  providedIn: 'root'
})
export class ErrorService {

  constructor(public snackBar: MatSnackBar) { }

  throwError(msg: string) {
    this.snackBar.open(msg, 'X', {
      panelClass: ['mat-toolbar', 'mat-warn'],
      duration: 10000
    });
  }
}
