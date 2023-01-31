let inputLetters = document.getElementById('letters');
inputLetters.addEventListener('input', inputProcess);

function inputProcess() {
    let str = inputLetters.value;
    if (/[^a-z]/i.test(str)) {
        inputLetters.value = str.slice(0,-1);   
    }
}
