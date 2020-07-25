import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import  {Company} from '../company.model'
import { DataService } from '../data.service';
@Component({
  selector: 'app-ask',
  templateUrl: './ask.component.html',
  styleUrls: ['./ask.component.css']
})
export class AskComponent implements OnInit {

  constructor(private router: Router,private dataservice: DataService) { }
company:Company[];
marketcap:number;
  ngOnInit() {

    
    

  }
  onClick()
  {
    
  
    
    if (typeof this.marketcap === 'undefined') {
      console.log(this.marketcap + ' is undefined');
    }
   
    this.dataservice.setmarketCap(this.marketcap);
   
      this.router.navigate(['/company']).then(nav => {
        console.log(nav); // true if navigation is successful
      }, err => {
        console.log(err) // when there's an error
      }); 
    
        
        }
        showcomp()
        {
          
          this.router.navigate(['/showcompany']).then(nav => {
            console.log(nav); // true if navigation is successful
          }, err => {
            console.log(err) // when there's an error
          }); 
          
        }
      
  
}
