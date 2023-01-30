let form = document.forms[0];
form.addEventListener('submit', createStory);

function createStory(e) {
    let person = document.getElementById('person').value;    
    let verb = document.getElementById('verb').value;     
    let adjective = document.getElementById('adjective').value;     
    let place = document.getElementById('place').value;     
    let noun = document.getElementById('noun').value;     
    if (person == '' || verb == '' || adjective == '' || place == '' || noun == '') {
        alert('Please fill in all fields for creating a story');
        return;
    }
    document.getElementById('story').innerHTML = Story(Math.floor(Math.random() * 3),person,verb,adjective,noun,place);
    e.preventDefault();
}

function Story(type,person,verb,adjective,noun,place) {
    switch (type) {
        case 0:
            return `${person} ${verb} ${adjective} ${noun} at ${place}`;      
        case 1:            
            return `${adjective} ${noun} ${verb} in great ${place} when ${person} was there`;
        default:
            return `if ${noun} will be ${adjective} when ${person} ${verb} in this ${place}`;
    }
    
}