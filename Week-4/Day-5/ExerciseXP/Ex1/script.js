
console.log(document.getElementById('container'));

let ulElements = document.getElementsByTagName('ul');

ulElements[0].className += ' university attendance';

for (const ul of ulElements) {
    ul.className += ' student_list';
    ul.firstElementChild.innerHTML = 'Kirill';
    for (const li of ul.children) {
        if (li.innerHTML == 'Pete') {
            li.innerHTML = 'Richard';    
        }     
        if (li.innerHTML == 'Sarah') {
            ul.removeChild(li);            
        }
    }
}

