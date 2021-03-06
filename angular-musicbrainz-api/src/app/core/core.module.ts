import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BoldPipe } from './pipe/bold.pipe';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [BoldPipe],
  imports: [
    CommonModule,
    HttpClientModule
  ],
  exports: [BoldPipe]
})
export class CoreModule { }
