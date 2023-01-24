const display = document.querySelector('#display');
let lastActivity = '';

function number(num) {
    display.innerText += num; 
    lastActivity = num;    
}

function operator(oper) {
    display.innerText += oper; 
    lastActivity = num;     
}

function equal() {
    display.innerText = eval(display.innerText).toFixed(2);     
    lastActivity = '';
}

function clearFunc() {
    display.innerText = '';     
    lastActivity = '';
}

function reset() {
    display.innerText = '';     
    lastActivity = '';
}


