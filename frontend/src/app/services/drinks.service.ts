import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { AuthService } from './auth.service';
import { environment } from 'src/environments/environment';
import { Drink } from 'src/app/models/Drink';


@Injectable({
  providedIn: 'root'
})
export class DrinksService {

  url = environment.apiServerUrl;

  public items: Drink[] = [];

  constructor(private auth: AuthService, private http: HttpClient) { }

  getHeaders() {
    const header = {
      headers: new HttpHeaders()
        .set('Authorization', `Bearer ${this.auth.activeJWT()}`)
    };
    return header;
  }

  getDrinks() {
    if (this.auth.can('get:drinks-detail')) {
      this.http.get(this.url + '/drinks-detail', this.getHeaders())
        .subscribe((res: any) => {

          this.items = res.drinks;
        });
    } else {
      this.http.get(this.url + '/drinks', this.getHeaders())
        .subscribe((res: any) => {
          console.log(res);
          this.items = res.drinks;
        });
    }

  }

  saveDrink(drink: Drink) {
    if (drink.id >= 0) { // patch
      this.http.patch(this.url + '/drinks/' + drink.id, drink, this.getHeaders())
        .subscribe((res: any) => {
          if (res.success) {
            this.items = res.drinks;
          }
        });
    } else { // insert     
      this.http.post(this.url + '/drinks', drink, this.getHeaders())
        .subscribe((res: any) => {
          if (res.success) {
            this.items = res.drinks;
          }
        });
    }

  }

  deleteDrink(drink: Drink) {
    delete this.items[drink.id];
    this.http.delete(this.url + '/drinks/' + drink.id, this.getHeaders())
      .subscribe((res: any) => {

      });
  }
}
