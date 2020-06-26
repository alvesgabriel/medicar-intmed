import { Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { AuthResponse } from 'src/app/auth/auth.response';
import { AuthService } from 'src/app/auth/auth.service';
import { ApiService } from 'src/app/services/api.service';
import { ConsultaComponent } from "../home/consulta/consulta.component";
import { consulta } from './consulta.response';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css', '../../app.component.css']
})
export class HomeComponent implements OnInit {

  displayedColumns: string[] = ['especialidade', 'profissional', 'data', 'hora', 'desmarcar'];
  dataSource: consulta[] = [];

  consultas: consulta[];

  user: AuthResponse;

  @ViewChild(MatPaginator, { static: true }) paginator: MatPaginator;

  constructor(
    public dialog: MatDialog,
    public apiService: ApiService,
    public authService: AuthService,
  ) { }

  ngOnInit(): void {
    this.getConsultas();
  }

  openDialog() {
    const dialogRef = this.dialog.open(ConsultaComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

  getConsultas() {
    this.apiService.getConsultas().subscribe((data) => {
      this.dataSource = data['results'];
      this.user = this.authService.auth;
    });
  }

  delConsulta(consulta: consulta) {
    this.apiService.delConsulta(consulta.id).subscribe(() => {
      this.getConsultas();
    });
  }

  logout() {
    this.authService.logout();
  }

}
