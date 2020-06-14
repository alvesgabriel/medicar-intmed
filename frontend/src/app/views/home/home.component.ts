import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css', '../../app.component.css']
})
export class HomeComponent implements OnInit {

  public userForm: FormGroup;

  constructor(
    private apiService: ApiService,
    private fb: FormBuilder
  ) { }

  ngOnInit(): void {
    this.userForm = this.fb.group({
      name: new FormControl('', [Validators.required]),
      email: new FormControl('', [Validators.required, Validators.email]),
      password: new FormControl('', [Validators.required]),
      password_confirm: new FormControl('', [Validators.required]),
    })
  }
  hide_pass = true;
  hide_pass_confirm = true;
  

  getErrorMessageName() {
    // if (this.userForm.value.name.hasError('required')) {
    if (this.userForm.hasError('required', 'name')) {
      return 'Nome campo obrigatório';
    }
  }

  getErrorMessageEmail() {
    if (this.userForm.hasError('required', 'email')) {
      return 'Email campo obrigatório';
    }
    return this.userForm.hasError('email', 'email') ? 'Email invalido' : '';
  }
  getErrorMessagePassword() {
    if (this.userForm.hasError('required', 'password')) {
      return 'Senha campo obrigatório';
    }
  }

  getErrorMessagePasswordConfirm() {
    if (this.userForm.hasError('required', 'password_confirm')) {
      return 'Confirmar campo obrigatório';
    }
  }

  createUser(form) {
    this.apiService.createUser(form.value).subscribe(
      result => { }
    );
  }

}
