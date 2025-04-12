import { Injectable } from '@angular/core';
import {UtmParameters} from '../data/utm.data';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {environment} from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class TrackerService {

  private start: number = -1;
  private utm: UtmParameters | undefined;

  constructor(private http: HttpClient) { }

  public recordStart() {
    this.start = Date.now();
    let endpoint = environment.webpageCallEndpoint;
    this.callGCloudRun(endpoint, {});
  }

  public recordUtm(utm: UtmParameters) {
    if (utm) { return; }
    this.utm = utm;
    let endpoint = environment.utmEndpoint;
    this.callGCloudRun(endpoint, {utm});
  }


  public recordEvent() {
    let duration = Date.now() - this.start; // ms
    let endpoint = environment.buttonClickEndpoint;
    let payload = this.utm ? { utm: this.utm, duration} : {duration};
    this.callGCloudRun(endpoint, payload);
  }

  private callGCloudRun(endpoint: string, payload: any) {
    if (endpoint.length == 0) { return; }

    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
      })
    };
    this.http.post<JSON>(endpoint, JSON.stringify(payload), httpOptions).subscribe({
      next: (response) => console.log('Success:', response),
      error: (err) => console.error('HTTP error:', err)
    });
  }
}
