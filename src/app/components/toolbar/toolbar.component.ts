import { Component } from '@angular/core';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatIconModule} from '@angular/material/icon';
import {TrackingButtonComponent} from '../tracking-button/tracking-button.component';
import {MatButtonModule} from '@angular/material/button';

@Component({
  selector: 'app-toolbar',
  imports: [MatToolbarModule, MatButtonModule, MatIconModule, TrackingButtonComponent],
  templateUrl: './toolbar.component.html',
  styleUrl: './toolbar.component.css'
})
export class ToolbarComponent {

}
