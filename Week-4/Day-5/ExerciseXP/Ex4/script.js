let arrBooks = [
    {
        title: 'Harry Potter and the Philosopher\'s Stone',
        author: 'JKRolling',
        image : 'https://www.wizardingworld.com/_next/image?url=%2Fimages%2Fproducts%2Fbooks%2FUK%2Frectangle-1.jpg&w=1320&q=75',
        alreadyRead : true
    },
    {        
        title: 'Harry Potter and the Chamber of Secrets',
        author: 'JKRolling',
        image : 'https://www.wizardingworld.com/_next/image?url=%2Fimages%2Fproducts%2Fbooks%2FUK%2Frectangle-2.jpg&w=1320&q=75',
        alreadyRead : false
    }
]

let divElem = document.querySelector('.listBooks');
let tableElem = document.createElement('table');
divElem.appendChild(tableElem);

for (const book of arrBooks) {
    let trElem = document.createElement('tr');
    let tdBookElem = document.createElement('td'); 
    let tdImageElem = document.createElement('td'); 
    tableElem.appendChild(trElem);
    trElem.appendChild(tdBookElem);
    trElem.appendChild(tdImageElem);   
    let imageElem = document.createElement('img');  
    tdBookElem.innerHTML = book.title + ' written by ' + book.author;
    imageElem.setAttribute('src', book.image);
    imageElem.style.width = '100px';
    imageElem.style.height = '100px';  
    tdBookElem.style.border = '1px solid black';
    tdImageElem.style.border = '1px solid black';
    if (book.alreadyRead) {
        trElem.style.backgroundColor = 'red';
    }
    tdImageElem.appendChild(imageElem);
}


