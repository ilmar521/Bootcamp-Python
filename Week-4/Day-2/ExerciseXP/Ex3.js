let divisor = Number(prompt('Enter a divisor'));

function isDivisible(divisor) {
    let summ = 0;
    let str = '';

    for (let i = 0; i <= 500; i++) {
        if (i % divisor == 0) {
            summ += i;
            str += i + ' ';    
        }       
    }

    console.log('Outcome: ' + str);
    console.log('Summ: ' + summ);
}

isDivisible(divisor);