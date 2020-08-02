import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import  {Company} from '../company.model'
import { Router } from '@angular/router';
import { stringify } from 'querystring';
@Component({
  selector: 'app-company',
  templateUrl: './company.component.html',
  styleUrls: ['./company.component.css']
})
export class CompanyComponent implements OnInit {

company:Company[];

  constructor(private dataservice:DataService,private router: Router) { 
   

 
  }

  ngOnInit() {
   
    this.dataservice.getStocks().subscribe((data:any)=> {
        
        console.log(data);
        // for (let i in JSON.parse(data)) 
        // {
        //   // let u:Company = new Company();
        //   // Object.assign(u , Company[i]);
        //   // this.company[i] = u;
        //   // console.log("user:" + this.company[i].Ask);
        //   let obj: Company = JSON.parse(data[i].toString());
        //   // obj.userName=this.dataservice.getUsername();
        //   this.company[i]=obj;
        // }
  
    }, (error) => {
      console.log('Error! ', error.text);
     
    }) ;
   
  }
//   }    
//     this.dataservice.getStocks().subscribe(
//       (data:any)=>
//       {
//         console.log(data);
         
          
//         for(let i=0;i<5;i++)
//         {
//           let obj: Company = JSON.parse(data[i]);
//           console.log("ask value"+obj.Ask)
//           //obj.userName=this.dataservice.getUsername();
//           this.company[i]=obj;
//           //this.company[i].previousClose_change=this.company[i].previousClose+this.company[i].change;
//         }
        
        
//       },err=>{
//         console.log(err.message);
//       }
//     );
    
// }
    savedata(comp:Company)
  {
  
    this.dataservice.saveStock(comp);
    
  }
 

}
