import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from "@angular/forms";
import { MatDialogRef } from '@angular/material/dialog';
import { MatSelectChange } from '@angular/material/select';
import { Router } from "@angular/router";
import { ApiService } from "../../../services/api.service";
import { agenda } from '../agenda.response';
import { especialidade } from '../especialidade.response';
import { medico } from '../medico.response';

@Component({
  selector: 'app-consulta',
  templateUrl: './consulta.component.html',
  styleUrls: ['./consulta.component.css', '../../../app.component.css']
})
export class ConsultaComponent implements OnInit {

  public consultaForm: FormGroup;
  especialidades: especialidade[];
  medicos: medico[];
  agendas: agenda[];
  horarios: string[];

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
      horario: new FormControl('', [Validators.required]),
    });
    this.getEspecialidades();
  }

  closeDialog() {
    this.dialogRef.close();
  }

  getEspecialidades() {
    this.apiService.getEspecialidades().subscribe(data => {
      this.especialidades = data.results;
    });
  }

  getMedicos(event: MatSelectChange) {
    this.apiService.getMedicos(event.value).subscribe(data => {
      this.medicos = data.results;
    });
  }

  getAgendas(event: MatSelectChange) {
    this.apiService.getAgendas(event.value).subscribe(data => {
      this.agendas = data.results;
    });
  }

  getHorarios(event: MatSelectChange) {
    this.apiService.getHorarios(event.value).subscribe(data => {
      this.horarios = data['horarios'];
    });
  }

  addConsulta(form) {
    this.apiService.addConsulta(form.value).subscribe(() => {
      this.closeDialog();
      this.router.navigate(['home']);
    });
  }

}
