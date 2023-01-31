let divAnimate = document.getElementById('animate');
let leftPos = 0;

function myMove() {
    leftPos = 0;
    divAnimate.style.left = leftPos + 'px';  
    let id = setInterval(() => {
        leftPos += 1;
        divAnimate.style.left = leftPos + 'px'; 
        if (leftPos == 350) {
            clearInterval(id);
        }        
    }, 1);    
}