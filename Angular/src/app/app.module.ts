import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpClientModule} from "@angular/common/http";
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { LoginComponent } from './login/login.component';
import { Route, RouterModule } from '@angular/router';
import { AskComponent } from './ask/ask.component';
import { UserComponent } from './user/user.component';
import { CompanyComponent } from './company/company.component';
import { DataService } from './data.service';
import { ShowcompanyComponent } from './showcompany/showcompany.component';

const ROUTES: Route[] = [
  { path: '', component: LoginComponent},
  { path: 'display', component: AskComponent},
  { path: 'users', component: UserComponent},
  { path: 'company', component: CompanyComponent},
  { path: 'showcompany', component: ShowcompanyComponent},
]
@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    AskComponent,
    UserComponent,
    CompanyComponent,
    ShowcompanyComponent,
 
  
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule,
    ReactiveFormsModule.withConfig({warnOnNgModelWithFormControl: 'never'}),
    RouterModule.forRoot(ROUTES)
  ],
  providers: [DataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
