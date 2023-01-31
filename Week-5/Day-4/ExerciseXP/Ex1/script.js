setTimeout(HelloWorld, 2000);
setTimeout(addParagraph, 2000);
let idInterval = setInterval(addParagraphInterval, 2000);
document.getElementById('clear').addEventListener('click', () => {clearInterval(idInterval)});

function HelloWorld() {
    console.log('Hello world!');       
}

function addParagraph() {
    let div = document.getElementById('container');
    let p = document.createElement('p');
    p.innerHTML = 'Hello World';
    div.appendChild(p);     
}

function addParagraphInterval() {
    let div = document.getElementById('container');
    if (div.getElementsByTagName('p').length == 5) {
        clearInterval(idInterval);
    }
    let p = document.createElement('p');
    p.innerHTML = 'Hello World';
    div.appendChild(p);      
}