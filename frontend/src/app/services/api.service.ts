import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiResponse } from './api.response';

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

  getConsultas(): Observable<ApiResponse> {
    return this.httpClient.get<ApiResponse>(`${this.SERVER_URL}/consultas/?ordering=dia`, this.httpOptions);
  }

  addConsulta(data): Observable<any> {
    return this.httpClient.post(`${this.SERVER_URL}/consultas/`, data, this.httpOptions);
  }

  delConsulta(consulta_id: number) {
    return this.httpClient.delete(`${this.SERVER_URL}/consultas/${consulta_id}/`, this.httpOptions);
  }

  getEspecialidades(): Observable<ApiResponse> {
    return this.httpClient.get<ApiResponse>(`${this.SERVER_URL}/especialidades/`, this.httpOptions);
  }

  getMedicos(especialidade_id: number): Observable<ApiResponse> {
    return this.httpClient.get<ApiResponse>(`${this.SERVER_URL}/medicos/?especialidade=${especialidade_id}`, this.httpOptions);
  }

  getAgendas(medico_id: number): Observable<ApiResponse> {
    return this.httpClient.get<ApiResponse>(`${this.SERVER_URL}/agendas/?medico=${medico_id}`, this.httpOptions);
  }

  getHorarios(agenda_id: number): Observable<ApiResponse> {
    return this.httpClient.get<ApiResponse>(`${this.SERVER_URL}/agendas/${agenda_id}/`, this.httpOptions);
  }

}
