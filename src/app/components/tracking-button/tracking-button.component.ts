import {Component, Input} from '@angular/core';
import {MatButtonModule} from '@angular/material/button';
import {MatIconModule} from '@angular/material/icon';
import {TrackerService} from '../../services/tracker.service';

@Component({
  selector: 'app-tracking-button',
  imports: [MatButtonModule, MatIconModule],
  templateUrl: './tracking-button.component.html',
  styleUrl: './tracking-button.component.css'
})
export class TrackingButtonComponent {

  @Input({ required: false }) public title = "";
  @Input({ required: false }) public icon = "";

  constructor(private tracker: TrackerService) {
  }
  public registerClick() {
    this.tracker.recordEvent();
  }
}
