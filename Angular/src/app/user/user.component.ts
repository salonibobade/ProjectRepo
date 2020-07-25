import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DataService } from '../data.service';
import { User } from '../user.model';
import { FormBuilder,FormGroup, Validators } from '@angular/forms';


@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {
  user: User = new User();
  userForm: FormGroup;
  submitted = false;
   authenticated=false
  constructor(private router: Router,private dataservice:DataService,private formBuilder: FormBuilder) { 
    this.userForm = this.formBuilder.group({
      'username': ['', Validators.required],
      'password': ['', Validators.required],
   
    });
  }
  arrresp: string;

  ngOnInit() {
  }
login():void
{ 
  console.log(this.user.userName)
  this.submitted = true;

  // stop here if form is invalid
  if (this.userForm.invalid) {
    console.log("invalid");
      return;
  }
  
  this.dataservice.setUsername(this.user.userName);
  
  this.dataservice.loginUser(this.user).subscribe((data:any)=> {
    
    if (Object.values(data)[0]=="true") {
        console.log(data);

        this.authenticated = true;
      
        alert('User logged in succesfully');
        if(this.authenticated){
        this.dataservice.setUsername(this.user.userName);
       
        this.router.navigate(['./display']).then(nav => {
          console.log(nav); // true if navigation is successful
        }, err => {
          console.log(err) // when there's an error
        });
      }
    } else {
        this.authenticated = false;
        console.log(data);
        alert('User logged in unsuccesful');
        this.router.navigate(['']);
    }
  }, (error) => {
    console.log('Error! ', error.text);
   
  }) ;
 
}
}
