import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { BehaviorSubject, Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
import { ApiService } from '../services/api.service';
import { AuthResponse } from './auth.response';


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  authState = new BehaviorSubject(false);
  auth: AuthResponse;

  constructor(
    private router: Router,
    private apiService: ApiService,
  ) { }

  isLoggedIn() {
    let user = JSON.parse(localStorage.getItem('USER_INFO'));
      if (user) {
        this.auth = user;
        this.authState.next(true);
      }
  }

  isAuthenticated() {
    return this.authState.value;
  }

  login(user): Observable<any> {
    return this.apiService.login(user).pipe(
      tap(async (res: AuthResponse) => {
        if (res) {
          await localStorage.setItem('USER_INFO', JSON.stringify(res));
          this.auth = res;
          this.authState.next(true);
        }
      })
    );
  }

  logout() {
    localStorage.removeItem('USER_INFO');
    this.router.navigate(['login']);
    this.authState.next(false);
  }
}
