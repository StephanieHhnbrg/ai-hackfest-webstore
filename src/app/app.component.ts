import {Component, OnDestroy, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {ToolbarComponent} from './components/toolbar/toolbar.component';
import {TrackerService} from './services/tracker.service';
import {Subscription} from 'rxjs';

@Component({
  selector: 'app-root',
  imports: [ToolbarComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit, OnDestroy {

  private subscriptions: Subscription[] = [];

  constructor(private tracker: TrackerService,
              private router: Router,
              private route: ActivatedRoute) {

  }

  public ngOnInit() {
    this.tracker.recordStart();

    this.subscriptions.push(this.route.queryParams
      .subscribe(params => {
        let campaign = params['utm_campaign'];
        let userId = params['utm_user_id'];
        if(campaign && userId) {
          this.tracker.recordUtm({campaign, userId});
          this.router.navigate([], {
            queryParams: {},
            replaceUrl: true
          });
        }
      }));
  }

  public ngOnDestroy() {
    this.subscriptions.forEach(s => s.unsubscribe());
  }

}
