const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ['banana', 'orange', 'apple'];

function myBill() {
    let price = 0;
    for (const item of shoppingList) {
        if (item in stock) {
            if (stock[item] > 0) {
                price += prices[item]; 
                stock[item] -= 1;    
            }    
        }   
    }
    return price; 
}

let totalPrice = myBill();
console.log('Total price - ' + totalPrice);