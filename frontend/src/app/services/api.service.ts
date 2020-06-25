import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  SERVER_URL = 'http://localhost:8080';

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  }

  constructor(
    private httpClient: HttpClient
  ) { }

  createUser(data): Observable<any> {
    return this.httpClient.post(`${this.SERVER_URL}/users/`, data, this.httpOptions);
  }

  login(data): Observable<any> {
    return this.httpClient.post(`${this.SERVER_URL}/login/`, data, this.httpOptions);
  }

  getConsultas(): Observable<any> {
    return this.httpClient.get(`${this.SERVER_URL}/consultas/`, this.httpOptions);
  }
}
