import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from "@angular/forms";
import { Router } from "@angular/router";
import { ApiService } from "../../../services/api.service";

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css', '../../../app.component.css']
})
export class UserComponent implements OnInit {

  public userForm: FormGroup;

  constructor(
    private router: Router,
    private fb: FormBuilder,
    private apiService: ApiService
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
      result => {
        this.makeLogin()
      }
    );
  }

  makeLogin() {
    this.router.navigate(['login']);
  }

}
