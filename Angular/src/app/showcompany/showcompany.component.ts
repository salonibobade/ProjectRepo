import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { Company } from '../company.model';
import { Router } from '@angular/router';
@Component({
  selector: 'app-showcompany',
  templateUrl: './showcompany.component.html',
  styleUrls: ['./showcompany.component.css']
})
export class ShowcompanyComponent implements OnInit {
  Key=0;
  company:any[] = [];

  constructor(private dataservice: DataService,private router: Router) { }

  ngOnInit() {
   
    this.dataservice.getcompanies().subscribe((data:any)=> {
      var count=Object.keys(data).length;
        console.log(data);
         for (var i=0;i<count;i++) 
         {
        //   // 
        //   // 
        //   // 
        //   // 
        // console.log(data[i]);
        // let u:Company = new Company();
        // var com
        // Object.assign(u , data[i]);
        // this.company[i] = u;
        // console.log("user:" + this.company[i].Ask);
        // console.log(data[i]);
        // let obj: Company = JSON.parse(data[i].toString());
        // console.log(obj.Ask);
        // this.company[i]=obj
        console.log(data[i])
        const employeeString = JSON.parse(data[i]);
        // let employee1 =employeeString;
        console.log(employeeString)
        console.log(this.company)
        this.company.push(employeeString);
          
         }
  
    }, (error) => {
      console.log('Error! ', error.text);
     
    }) ;
   
  }

 
  onClick()
  {
    this.router.navigate(['/users']).then(nav => {
      console.log(nav); // true if navigation is successful
    }, err => {
      console.log(err) // when there's an error
    }); 
  
  }
}
