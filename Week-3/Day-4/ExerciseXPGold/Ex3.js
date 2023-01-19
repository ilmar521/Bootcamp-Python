let word = prompt("Enter a verb");
let wLeght = word.length;

if (wLeght >= 3 && word.substring(wLeght - 3, wLeght) == "ing") {
    console.log(word + "ly");
} else if (wLeght >= 3 && word.substring(wLeght - 3, wLeght) != "ing") {
    console.log(word + "ing");
} else {
    console.log(word);
}