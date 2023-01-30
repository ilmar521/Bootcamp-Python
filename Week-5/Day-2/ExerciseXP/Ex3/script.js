let allBoldItems = [];
let paragraph = document.querySelector('p');
paragraph.addEventListener('mouseover', mouseoverParagraph);
paragraph.addEventListener('mouseout', mouseoutParagraph);

function getBold_items() {
    allBoldItems = document.getElementsByTagName('strong');    
}

function highlight() {
    getBold_items();

    for (item of allBoldItems) {
        item.style.color = 'blue';
    }
}

function return_normal() {
    getBold_items();

    for (item of allBoldItems) {
        item.style.color = 'black';
    }
}


function mouseoverParagraph(params) {
    highlight();    
}

function mouseoutParagraph(params) {
    return_normal();    
}
