
let body = document.querySelector('body');
body.style.fontSize = '18px';
let divElem = document.querySelector('div');
divElem.style.backgroundColor = '#ADD8E6';
divElem.style.padding = '10px';

let ulElements = document.getElementsByTagName('ul');
let users = [];

for (ul of ulElements) {
    let elForRemove = []; 
    for (const li of ul.children) {
        users.push(li.innerHTML);
        if (li.innerHTML == 'John') {
            elForRemove.push(li);
        } else if (li.innerHTML == 'Pete') {
            li.style.border = '1px solid black';           
        }
    }
    for (i of elForRemove) {
        ul.removeChild(i);      
    }
}

if (divElem.style.backgroundColor == "rgb(173, 216, 230)") {
    console.log(`Hello ${users[0]} and ${users[1]}`);    
}

