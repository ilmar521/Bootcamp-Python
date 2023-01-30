let form = document.forms[0];

form.addEventListener('submit', submitForm);

function submitForm(e) {
    let radius = Number(form.elements.radius.value);
    if (isNaN(radius)) {
        alert('You should enter correct value of radius for calculating!');
        return;
    }  
    form.elements.volume.value = 4/3 * 3.14 * radius**3;    
    e.preventDefault();
}