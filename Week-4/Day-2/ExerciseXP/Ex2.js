function calculateTip() {
    let bill = Number(prompt('Enter amount of bill'));

    if (isNaN(bill)) {
        console.log('You entered invalid value of bill!');
    } else {
        let percentTips = 0;
        if (bill < 50) {
            percentTips = 20;    
        } else if (bill <= 200) {
            percentTips = 15;   
        } else {
            percentTips = 10;   
        }
        console.log(`bill - ${bill}; tips - ${bill * (percentTips / 100)}`);
    }
}

calculateTip();