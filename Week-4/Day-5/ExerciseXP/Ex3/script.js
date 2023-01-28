let divElem = document.querySelector('div');
divElem.setAttribute('id','socialNetworkNavigation');

let ulElement = document.querySelector('ul');
let liElem = document.createElement('li');
let aElem = document.createElement('a');
aElem.innerHTML = 'Logout';
aElem.setAttribute('href', "#");
liElem.appendChild(aElem);
ulElement.appendChild(liElem);

console.log(ulElement.firstElementChild.textContent);
console.log(ulElement.lastElementChild.textContent);