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
company:Company[];
  constructor(private dataservice: DataService,private router: Router) { }

  ngOnInit() {
    this.dataservice.getcompanies().subscribe(data=>
      {
        this.company=data;
      
      },err=>{
        console.log(err.message)
      });
  }

  deleteData(comp:Company)
  {
    console.log("Username in deleting is  "+this.dataservice.getUsername());
    
    this.dataservice.deleteStock(comp);
    this.router.navigate(['./display']).then(nav => {
      console.log(nav); // true if navigation is successful
    }, err => {
      console.log(err) // when there's an error
    });
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
