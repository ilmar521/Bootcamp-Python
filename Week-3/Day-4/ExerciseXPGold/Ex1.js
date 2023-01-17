let word = prompt("Which language do you speak?");
let wordLower = word.toLowerCase();

switch (wordLower) {
    case "french":
        console.log("Bonjour");
        break;
    case "english":
        console.log("Hello");
        break;
    case "hebrew":
        console.log("Shalom");
        break;
    default:
        console.log("01110011 01101111 01110010 01110010 01111001");
}