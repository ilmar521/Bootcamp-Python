let attempt = 0;

function checkWord(user1Word, user2Word, user2Letter, user2Arr) {
    
    user2Arr.push(user2Letter);
    let index = [];
    for (let i = 0; i < user1Word.length; i++) {
        if (user1Word[i] === user2Letter) index.push(i);
    }
  
    let user2WordArr = user2Word.split('');
    for (const i of index) {
        user2WordArr[i] = user2Letter;
    }
    user2Word = user2WordArr.join('');

    console.log(user2Word);

    if (user1Word == user2Word) {
        alert('CONGRATS YOU WIN');
        return;    
    } else {
        attempt += 1;
        if (attempt > 10) {
            alert('YOU LOSE');  
            return;   
        }   
        
        while (true) {
            user2Letter = prompt('Enter a letter'); 
            if (user2Arr.indexOf(user2Letter) > -1) {
                alert('You can\'t choose the same letter as before!');     
            } else {
                break;
            } 
        }
        checkWord(user1Word, user2Word, user2Letter, user2Arr);     
    }    
}

function playTheGame() {
    attempt = 0;

    if (confirm('Would you like play the game?')) { 
        while (true) {
            let user1Word = prompt('Enter a word');   
            if (user1Word.length < 8) {
                alert('You should enter word which have at least 8 letters');           
            } else {
                let user2Word = '*'.repeat(user1Word.length);
                console.log(user2Word);
                let user2Arr = [];
                let user2Letter = prompt('Enter a letter');  
                checkWord(user1Word, user2Word, user2Letter, user2Arr);
                break;
            }
        }
    } else {
        alert('No problem, Goodbye');
    }   
}

