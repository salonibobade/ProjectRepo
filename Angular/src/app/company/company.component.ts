import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import  {Company} from '../company.model'
import { Router } from '@angular/router';
@Component({
  selector: 'app-company',
  templateUrl: './company.component.html',
  styleUrls: ['./company.component.css']
})
export class CompanyComponent implements OnInit {
company:Company[]=[];

  constructor(private dataservice:DataService,private router: Router) { 
   

 
  }

  ngOnInit() {
   
    
    this.dataservice.getStocks().subscribe(
      data=>
      {
        
       
        
        for(let i=0;i<5;i++)
        {
          let obj: Company = JSON.parse(data[i].toString());
        obj.userName=this.dataservice.getUsername();
        this.company[i]=obj;
        this.company[i].previousClose_change=this.company[i].previousClose+this.company[i].change;
        
        }
        
        
      },err=>{
        console.log(err.message);
      }
    );
    
}
    savedata(comp:Company)
  {
  
    this.dataservice.saveStock(comp);
    
  }
 

}
