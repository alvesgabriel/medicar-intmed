import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from "@angular/forms";
import { MatDialogRef } from '@angular/material/dialog';
import { Router } from "@angular/router";
import { ApiService } from "../../../services/api.service";

@Component({
  selector: 'app-consulta',
  templateUrl: './consulta.component.html',
  styleUrls: ['./consulta.component.css', '../../../app.component.css']
})
export class ConsultaComponent implements OnInit {

  especialidadesList = [
    { id: 1, nome: "Pediatria" },
    { id: 2, nome: "Ginecologia" },
    { id: 3, nome: "Cardiologia" },
    { id: 4, nome: "Clínico Geral" },
    { id: 5, nome: "Oncologia" },
  ];

  medicosList = [
    {
      id: 1,
      crm: 3711,
      nome: "Drauzio Varella",
      especialidade: {
        id: 2,
        nome: "Pediatria"
      }
    },
    {
      id: 2,
      crm: 2544,
      nome: "Gregory House",
      especialidade: {
        id: 3,
        nome: "Cardiologia"
      }
    },
    {
      id: 3,
      crm: 3087,
      nome: "Tony Tony Chopper",
      especialidade: {
        id: 2,
        nome: "Pediatria"
      }
    }
  ];

  agendasList = [
    {
      id: 1,
      medico: {
        id: 3,
        crm: 3087,
        nome: "Tony Tony Chopper",
        especialidade: {
          id: 2,
          nome: "Pediatria"
        }
      },
      dia: "2020-02-10",
      horarios: ["14:00", "14:15", "16:00"]
    },
    {
      id: 2,
      medico: {
        id: 2,
        crm: 2544,
        nome: "Gregory House",
        especialidade: {
          id: 3,
          nome: "Cardiologia"
        }
      },
      dia: "2020-02-10",
      horarios: ["08:00", "08:30", "09:00", "09:30", "14:00"]
    }
  ];

  horariosList = ["08:00", "08:30", "09:00", "09:30", "14:00"];

  public consultaForm: FormGroup;

  constructor(
    private router: Router,
    private fb: FormBuilder,
    private apiService: ApiService,
    private dialogRef: MatDialogRef<ConsultaComponent>,
  ) { }

  ngOnInit(): void {
    this.consultaForm = this.fb.group({
      especialidade_id: new FormControl('', [Validators.required]),
      medico_id: new FormControl('', [Validators.required]),
      agenda_id: new FormControl('', [Validators.required]),
      hora: new FormControl('', [Validators.required]),
    })
  }

  close() {
    this.dialogRef.close();
  }

}
