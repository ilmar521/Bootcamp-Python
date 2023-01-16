let strNumbers = prompt("Enter string of numbers separated by commas");
let arrNumbers = strNumbers.split(",");
let Summ = new Number(0);

arrNumbers.forEach(myFunction)

function myFunction(value, index, array) {
    Summ += Number(value);
};

console.log(Summ);