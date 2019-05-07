// Angular
import { 
  Component, 
  OnInit,
  ChangeDetectionStrategy
 } from '@angular/core';
import { FormControl } from '@angular/forms';
// RxJs
import { Observable } from 'rxjs';
import { map, startWith } from 'rxjs/operators';
// Dummy data
import { SAMPLE_RESULTS } from '../../../sample-results';


@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  selector: 'app-search-component',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {
  // search vars
  queryString: string;
  searching: boolean;
  searchType: string;
  searchControl: FormControl;

  filteredResults$: Observable<string[]>;

  results = SAMPLE_RESULTS;

  constructor() { }

  ngOnInit() {
    this.searching = false;
    this.searchControl = new FormControl('');
    this.filteredResults$ = this.searchControl.valueChanges.pipe(
      startWith(''),
      map(val => this.filterResults(val)),
      map(val => val.slice(0, 4)));
  }

  filterResults(val: string): string[] {
    return val ? this.results.filter(v => v.toLowerCase().indexOf(val.toLowerCase()) === 0) : [];
  }

}