import { Component } from '@angular/core';
import {TrackingButtonComponent} from '../tracking-button/tracking-button.component';
import {MatCardModule} from '@angular/material/card';
import {CommonModule} from '@angular/common';

@Component({
  selector: 'app-mock-store',
  imports: [CommonModule, MatCardModule, TrackingButtonComponent],
  templateUrl: './mock-store.component.html',
  styleUrl: './mock-store.component.css'
})
export class MockStoreComponent {

  public data: {name: string, subtitle: string, desc: string, imgUrl: string}[] = [
    { name: "Desert Rose", subtitle: "Adenium obesum", desc: " Known for its thick, swollen trunk and striking pink to red trumpet-shaped flowers, the Desert Rose is a drought-tolerant plant native to Africa and the Arabian Peninsula. Often grown in pots, it's a favorite for bonsai-style displays.", imgUrl: "assets/flower_1.jpg"},
    { name: "Hibiscus", subtitle: "Hibiscus rosa-sinensis", desc: "A symbol of tropical beauty, the Hibiscus blooms with large, vivid flowers in a range of colors. This red variety is often associated with love and passion, and it attracts hummingbirds and butterflies." , imgUrl: "assets/flower_2.jpg"},
    { name: "Bird of Paradise", subtitle: "Strelitzia reginae", desc: "With its dramatic orange and blue (or sometimes red and yellow) flower resembling a bird in flight, this plant thrives in humid, tropical environments. It's a statement piece in gardens and floral arrangements." , imgUrl: "assets/flower_3.jpg"},
    { name: "Brazilian Red Cloak", subtitle: "Megaskepasma erythrochlamys", desc: "This flower stands out with its elaborate red-pink bracts and lush foliage. Common in tropical rainforests and gardens, it's admired for its ornamental value and striking visual appeal." , imgUrl: "assets/flower_4.jpg"},
  ];
}
