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
         for (let i=0;i<5;i++) 
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
        let employee1 =employeeString;
        console.log(employeeString)
        this.company[i]=employee1
          
         }
  
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
