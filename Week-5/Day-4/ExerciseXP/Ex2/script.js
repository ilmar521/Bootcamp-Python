// Copy the code above, to a structured HTML file.
// In your Javascript file, use setInterval to move the <div id="animate"> to the right side of the <div id="container">, when the button is clicked on.
// The <div id="animate"> should move 1px to the right every milisecond, until it reaches the end of the <div id="container">.
// Hint : use clearInterval as soon as the box reaches the right end side of the container
// Hint : check out the demonstration in the Course Noted named JS Functions

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