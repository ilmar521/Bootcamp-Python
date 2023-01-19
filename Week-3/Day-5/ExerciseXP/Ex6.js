const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }

let str = '';

for (const x in details) {
    str += x + ' ' + details[x] + ' ';
}

console.log(str.trim());