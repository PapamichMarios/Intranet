import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';

@Injectable({
  providedIn: 'root'
})
export class SuccessService {

  constructor(public snackBar: MatSnackBar) { }

  throwSuccess(msg: string) {
    this.snackBar.open(msg, 'X', {
      panelClass: ['mat-toolbar', 'mat-accent'],
      duration: 10000
    });
  }
}
