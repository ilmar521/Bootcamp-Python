let box = document.getElementById('box');
let target = document.getElementById('target');
box.setAttribute('draggable', 'true');

target.addEventListener('dragover', function (event) {
    event.preventDefault();   
})
target.addEventListener('drop', function (event) {
    event.preventDefault();
    let id = event.dataTransfer.getData("id");  
    let box = document.getElementById(id)
    event.target.appendChild(box);      
})

box.addEventListener('dragstart', function (event) {
    event.dataTransfer.setData('id', event.target.id);    
});

