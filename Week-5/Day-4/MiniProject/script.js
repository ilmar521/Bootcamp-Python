let color = null;
let area = document.getElementById('area');
let mouseClick = false;



for (let i = 0; i < 1000; i++) {
    let div = document.createElement('div');
    div.classList.add('fill');
    div.addEventListener('mousedown', mousedownFillArea);
    div.addEventListener('mouseup', mouseupFillArea);
    div.addEventListener('mousemove', mousemoveFillArea);
    area.appendChild(div); 
}

document.getElementById('clear-button').addEventListener('click', () => {
    for (fill of area.children) {
        fill.style.backgroundColor = 'rgb(231, 227, 227)';     
    }    
})

let colors = document.querySelectorAll('.color');
for (color of colors) {
    color.addEventListener('click', chooseColor);    
}

function chooseColor(event) {
    color = event.target.style.backgroundColor;    
}

function mousedownFillArea(event) {
    mouseClick = true;
    event.target.style.backgroundColor = color;    
}
function mouseupFillArea(event) {
    mouseClick = false;
    event.target.style.backgroundColor = color;    
}
function mousemoveFillArea(event) {
    if (mouseClick) {
        event.target.style.backgroundColor = color;  
    }
}

// function clickOnFillArea(event) {
//    event.target.style.backgroundColor = color;    
// }

