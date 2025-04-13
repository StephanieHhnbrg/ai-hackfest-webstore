import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MockStoreComponent } from './mock-store.component';

describe('MockStoreComponent', () => {
  let component: MockStoreComponent;
  let fixture: ComponentFixture<MockStoreComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MockStoreComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MockStoreComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
