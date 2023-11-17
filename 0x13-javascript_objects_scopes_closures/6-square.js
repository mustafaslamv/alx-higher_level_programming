#!/usr/bin/node

const square = require('./5-square.js');
class Square extends square {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let line = '';
        for (let j = 0; j < this.width; j++) {
          line += 'C';
        }
        console.log(line);
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
