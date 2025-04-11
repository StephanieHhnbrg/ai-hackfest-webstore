import {Component, OnDestroy, OnInit} from '@angular/core';
import {ActivatedRoute, RouterOutlet} from '@angular/router';
import {ToolbarComponent} from './components/toolbar/toolbar.component';
import {TrackerService} from './services/tracker.service';
import {Subscription} from 'rxjs';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, ToolbarComponent, TrackerService],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit, OnDestroy {

  private subscriptions: Subscription[] = [];

  constructor(private tracker: TrackerService, private route: ActivatedRoute) {

  }

  public ngOnInit() {
    this.tracker.recordStart();

    this.subscriptions.push(this.route.queryParams
      .subscribe(params => {
        let source = params['utm_source'];
        let medium = params['utm_medium'];
        let campaign = params['utm_campaign'];
        let content = params['utm_content'];
        if(source && medium && campaign && content) {
          this.tracker.recordUtm({source, medium, campaign, content})
        }
      }));
  }

  public ngOnDestroy() {
    this.subscriptions.forEach(s => s.unsubscribe());
  }

}
