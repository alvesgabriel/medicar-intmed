import { Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { ConsultaComponent } from "../home/consulta/consulta.component";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css', '../../app.component.css']
})
export class HomeComponent implements OnInit {

  displayedColumns: string[] = ['especialidade', 'profissional', 'data', 'hora', 'desmarcar'];
  dataSource = new MatTableDataSource<any>(ELEMENT_DATA);

  @ViewChild(MatPaginator, { static: true }) paginator: MatPaginator;

  constructor(public dialog: MatDialog) { }

  ngOnInit(): void {
    this.dataSource.paginator = this.paginator;
  }

  openDialog() {
    const dialogRef = this.dialog.open(ConsultaComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

}

const ELEMENT_DATA = [
  {
    id: 1,
    dia: "2020-02-05",
    horario: "12:00",
    data_agendamento: "2020-02-01T10:45:0-03:00",
    medico: {
      id: 2,
      crm: 2544,
      nome: "Gregory House",
      especialidade: {
        id: 3,
        nome: "Cardiologia"
      }
    }
  },
  {
    id: 2,
    dia: "2020-03-01",
    horario: "09:00",
    data_agendamento: "2020-02-01T10:45:0-03:00",
    medico: {
      id: 1,
      crm: 3711,
      nome: "Drauzio Varella",
      especialidade: {
        id: 2,
        nome: "Pediatria"
      }
    }
  }
];
