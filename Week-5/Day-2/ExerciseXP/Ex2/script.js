let form = document.forms[0];
let fname = form.elements.fname;
let lname = form.elements.lname;

console.log(form);

// Retrieve the inputs by their id and console.log them.
console.log(document.getElementById('fname'), document.getElementById('lname'));

// Retrieve the inputs by their name attribute and console.log them.
console.log(fname, lname);

form.addEventListener('submit', submitForm);

function submitForm(e) {
    if (fname.value == '' || lname.value == '') {
        alert('Please fill in all fields on form before submitting!');
        return;
    }    
    let ulElement = document.querySelector('.usersAnswer');
    let li_fname = document.createElement('li');
    let li_lname = document.createElement('li');  
    li_fname.innerHTML = fname.value;
    li_lname.innerHTML = lname.value;
    ulElement.appendChild(li_fname);
    ulElement.appendChild(li_lname);
    e.preventDefault();
}