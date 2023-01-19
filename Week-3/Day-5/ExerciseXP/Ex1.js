const people = ["Greg", "Mary", "Devon", "James"];

//Review arrays

people.shift();
people[people.indexOf("James")] = "Jason";
people.push("Kirill");

console.log(people.indexOf("Mary"));
let peopleNew = people.slice(1,3);

console.log(peopleNew.indexOf("Foo"));

let last = peopleNew[peopleNew.length - 1];
console.log(last);

//Loops

for (let i = 0; i < people.length; i++) {
    console.log(people[i]);         
}

for (let i = 0; i < people.length; i++) {
    if (people[i] == "Jason") {
        break;
    }    
}
