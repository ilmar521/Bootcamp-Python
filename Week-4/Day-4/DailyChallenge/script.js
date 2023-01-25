function showSong() {
    let amBottles = 0;  
    let dropBottles = 0; 
    while (isNaN(amBottles) || amBottles == 0) {
        amBottles = Number(prompt("Enter number of bottles"));
    }       

    while (amBottles > 0) {
        dropBottles += 1;
        console.log(`${amBottles} ${amBottles == 1 ? "bottle":"bottles"} of beer on the wall`);    
        console.log(`${amBottles} ${amBottles == 1 ? "bottle":"bottles"} of beer`);  
        
        if (amBottles > dropBottles) {
            amBottles -= dropBottles;
            console.log(`Take ${dropBottles} down, pass ${dropBottles == 1 ? "it":"them"} it around`);  
            console.log(`${amBottles} ${amBottles == 1 ? "bottle":"bottles"} of beer on the wall`);           
        } else {
            dropBottles = amBottles;
            amBottles = 0;
            console.log(`Take ${dropBottles} down, pass ${dropBottles == 1 ? "it":"them"} it around`);  
            console.log(`no bottle of beer on the wall`);               
        }
        console.log(``);   
    }
} 

showSong();