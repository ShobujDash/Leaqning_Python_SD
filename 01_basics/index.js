let day = new Date().getDay();

// if (data === 0) {
//   console.log('sunday')
// } else if (data === 1) {
//   console.log('monday')
// }else if (data === 2) {
//   console.log('tuesday')
// }

// console.log(data)

switch (day) {
  case 0:
    console.log("sun");
    break;
  case 1:
    console.log('mon')
    break;
  case 2:
    console.log('tus')
    break;
  case 3:
    console.log('thus')
    break;
  case 4:
    console.log('wed')
    break;
  case 5:
    console.log('fri')
    break;
  case 6:
    console.log('sat')
    break;
}


let days = ['sun', 'mon', 'tues', 'wed', 'thus', 'fri', 'sat'];

console.log(days[day])
console.log('hi')