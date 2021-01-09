import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MyRatingsComponent } from './my-ratings.component';

describe('MyRatingsComponent', () => {
  let component: MyRatingsComponent;
  let fixture: ComponentFixture<MyRatingsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MyRatingsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MyRatingsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
