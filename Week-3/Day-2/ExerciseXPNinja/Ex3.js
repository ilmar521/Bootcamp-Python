let str = prompt('Enter string which contains word \"Nemo\"');

let indexNemo = str.indexOf("Nemo");

if (indexNemo >= 0) {
    console.log(`I found Nemo at ${indexNemo}`)
} else {
    console.log(`I can’t find Nemo`)
};