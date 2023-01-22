const str = prompt('Enter the string');
let arr = str.split(',');

function longestWord(arr) {
    let long = 0;
    for (const x of arr) {
        if (x.length > long) {
            long = x.length;
        }
    }   
    return long;
}

function showFrame(arr) {
    let maxLong = longestWord(arr);
    console.log("*".repeat(maxLong + 4));  
    for (const x of arr) {
        if (x.length < maxLong) {
            console.log("* " + x + " ".repeat(maxLong - x.length) + " *");      
        } else {
            console.log(`* ${x} *`);     
        }
    } 
    console.log("*".repeat(maxLong + 4));       
}

showFrame(arr);

