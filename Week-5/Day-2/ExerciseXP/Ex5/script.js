let divElement = document.querySelector('div');

divElement.addEventListener('mouseover', mouseoverDivElement);
divElement.addEventListener('mouseout', mouseoutDivElement);
divElement.addEventListener('click', clickDivElement);
divElement.addEventListener('dblclick', dblclickrDivElement);

function mouseoverDivElement() {
    divElement.style.backgroundColor = 'red';    
}

function mouseoutDivElement() {
    divElement.style.backgroundColor = 'white';        
}

function clickDivElement() {
    divElement.style.width = '200px';   
    divElement.style.height = '40px';   
}

function dblclickrDivElement() {
    divElement.style.width = '100px';   
    divElement.style.height = '20px';    
}
