import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { AskComponent } from './ask/ask.component';
import { UserComponent } from './user/user.component';
import { CompanyComponent } from './company/company.component';
import { ShowcompanyComponent } from './showcompany/showcompany.component';

import { FormsModule } from '@angular/forms';

const routes: Routes = [
  { path: '', component: LoginComponent},
  { path: 'display', component: AskComponent},
  { path: 'users', component: UserComponent},
  { path: 'company', component: CompanyComponent},
  { path: 'showcompany', component: ShowcompanyComponent},
 

];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
    FormsModule
  ],
  exports: [
    RouterModule
  ],
  declarations: []
})
export class AppRoutingModule { }
