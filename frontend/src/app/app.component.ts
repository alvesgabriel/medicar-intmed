import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from './auth/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';

  constructor(
    private router: Router,
    private authService: AuthService,
  ) {
    if (this.authService.isAuthenticated()) {
      this.router.navigate(['']);
    } else {
      this.router.navigate(['login']);
    }
  }
}
