import { Injectable } from '@angular/core';
import {UtmParameters} from '../data/utm.data';

@Injectable({
  providedIn: 'root'
})
export class TrackerService {

  private start: number;
  private utm: UtmParameters;

  constructor() { }

  public recordStart() {
    this.start = Date.now();
    // TODO: backend call
  }

  public recordUtm(utm: UtmParameters) {
    if (utm) { return; }
    this.utm = utm;
    // TODO: backend call
  }


  public recordEvent() {
    let time = Date.now() - this.start;
    // TODO: backend call
  }
}
