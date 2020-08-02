
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {Router} from '@angular/router';
import { Company } from './company.model';
import { Observable } from 'rxjs';
import { User } from './user.model';
//import { SrvRecord } from 'dns';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type':  'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private userUrl = 'http://localhost:5000/';
  private baseUrl;
  authenticated = false;
  marketCap:string;
  username:string="muskan"
  data:string[]
  constructor(private http: HttpClient,private router: Router) { }
  setOption(value) { 
    console.log("in setter set option "+value);
    this.data = value;  
  }  
  
  getmarketCap() {
    console.log("in getter will give "+this.marketCap);
 
    return this.marketCap;  
  } 
  setmarketCap( value) { 
    console.log("in setter set option "+value);
    
    this.marketCap = value;  
  }  
  
  getOption() {
    // console.log("in getter giving option "+this.data);
 
    return this.data;  
  } 
   public loginUser(user)
   {      
     console.log()
     var a=user.userName;
     var b=user.passWord;
    return this.http.get(this.userUrl+"/loggedin?user="+a+"&password="+b) ;
  }
  
  getUsername() {
    console.log("in getter giving  "+this.username );
   
    return this.username;  
  } 
  setUsername( value:string) { 
    console.log("in setter got option "+value);

    this.username = value;  
  }  
  
  
  getStocks()//: Observable<string[]>
  {
    
    // return this.http.get(this.userUrl+"/stockMarket?cap="+this.getmarketCap());
    return this.http.get<String[]>(this.userUrl+"/stockMarket?cap="+this.getmarketCap());
    // return this.http.get(this.userUrl+"/loggedin?user=Aish11&password=2345") ;
  }
   saveStock(comp:Company) {
    console.log("Username will save stocks  "+this.getUsername());
    
    //  console.log( "received  user "+comp.userName);
    return this.http.post('http://localhost:8080/user-portal/stocks', comp,httpOptions).subscribe(data => {
     if (data) {
         
     
         alert('Company saved in succesfully');
         
     } 
   }, (error) => {
     console.log('Error! ', error.text);
    
   }) ;
   
 }
 getcompanies()
 {
  console.log("Username retrive from spring  "+this.getUsername());
  
  return this.http.get<Company[]>(`${this.baseUrl}/${this.username}`);
  
 }
//  deleteStock(comp:Company) {
//   console.log("got this "+comp.userName);
//   console.log("Username will delete stocks  "+this.getUsername());
  
//  return this.http.post('http://localhost:8080/user-portal/stocks/saved',comp,httpOptions).subscribe(data => {
//   if (data) {
      
//       // console.log(data);
//       alert('Company deleted  succesfully');
      
//   } 
// }, (error) => {
//   console.log('Error! ', error.text);
//  alert('Company delete  unsuccesful');
// }) ;

// }
}








