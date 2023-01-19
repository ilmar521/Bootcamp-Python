const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let firstLetters = [];

names.forEach(element => {
    firstLetters.push(element.substring(0,1));       
});

firstLetters.sort();
console.log(firstLetters.join(''));