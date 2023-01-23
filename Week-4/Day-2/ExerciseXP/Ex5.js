let rulesOfOrder = [0.25, 0.1, 0.05, 0.01];

function changeEnough(itemPrice, amountOfChange) {
    let totalAmount = 0;
    for (const i in amountOfChange) {
        totalAmount += amountOfChange[i] * rulesOfOrder[i];     
    }
    return totalAmount >= itemPrice;
}

console.log(changeEnough(14.11, [2,100,0,0]));
console.log(changeEnough(0.75, [0,0,20,5]));