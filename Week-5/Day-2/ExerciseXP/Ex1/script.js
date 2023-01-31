let article = document.querySelector('article');
console.log(article.firstElementChild);
article.removeChild(article.lastElementChild);

let h1 = document.querySelector('h1');
h1.addEventListener('mouseover', onMouseOverH1);

let paragraph = document.getElementById('fadeParagraph');
paragraph.addEventListener('mouseover', onMouseOverParagraph);
paragraph.addEventListener('mouseleave', onMouseLeaveParagraph);

let h2 = document.querySelector('h2');
h2.addEventListener('click', onClickH2);

let h3 = document.querySelector('h3');
h3.addEventListener('click', onClickH3);

let button = document.createElement('button');
button.innerHTML = 'Make all BOLD!';
article.appendChild(button);
button.addEventListener('click', onClickbutton);

function onClickH2() {
    this.style.backgroundColor = 'red';    
}

function onClickH3() {
    this.style.display = 'none';    
}

function onClickbutton() {
    article.style.fontWeight = 'bold';    
}

function onMouseOverH1() {
    this.style.fontSize = `${Math.floor(Math.random() * 101)}px`;
}

function onMouseOverParagraph() {
    this.style.opacity = 1;
    this.style.transition = `opacity 1000ms`;
    this.style.opacity = 0;
  
    // setTimeout(() => {
    // }, 1000);
}

function onMouseLeaveParagraph() {
    this.style.opacity = 0;
    this.style.transition = `opacity 1000ms`;
    this.style.opacity = 1;
    
    // setTimeout(() => {
    //     this.style.opacity = 1;
    // }, 10);
}