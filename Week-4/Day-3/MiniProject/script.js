let attempt = 0;

function getRandomIntInclusive(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min; //Максимум и минимум включаются
}

function compareNumbers(userNumber,computerNumber) {
    
    if (userNumber == computerNumber) {
        alert('WINNER');
        return;    
    } else {
        attempt += 1;
        if (attempt > 3) {
            alert('out of chances');  
            return;   
        }   

        if (userNumber > computerNumber) {
            alert('Your number is bigger then the computer’s, guess again');     
        } else {
            alert('Your number is smaller then the computer’s, guess again');     
        }            
        userNumber = Number(prompt('Enter a number between 0 and 10'));   
        compareNumbers(userNumber,computerNumber);       
    }    
}

function playTheGame() {
    attempt = 0;

    if (confirm('Would you like play the game?')) { 
        while (true) {
            let userNumber = Number(prompt('Enter a number between 0 and 10'));   
            if (isNaN(userNumber)) {
                alert('Sorry Not a number, Goodbye');        
            } else if (userNumber < 0 || userNumber > 10) {
                alert('Sorry it’s not a good number, Goodbye');     
            } else {
                computerNumber = getRandomIntInclusive(0, 10);
                compareNumbers(userNumber,computerNumber);
                break;
            }
        }

    } else {
        alert('No problem, Goodbye');
    }   
}