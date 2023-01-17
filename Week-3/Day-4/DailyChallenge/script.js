let arrSentence = ["This dinner is not that bad ! You cook well", "This movie is not so bad !", "This dinner is bad !"];

arrSentence.forEach(myFunc)

function myFunc(value, index, array) {
    let wordNot = value.indexOf("not");
    let wordBad = value.indexOf("bad");
    
    if (wordNot < wordBad && wordNot != -1) {
        let substr = value.substring(wordNot, wordBad + 3);
        console.log(value.replace(substr, 'good'));
    } else {
        console.log(value);
    }
};