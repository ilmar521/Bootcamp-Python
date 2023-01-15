let num1 = prompt("Please enter first number");

if (num1 != null) {

    num1 = parseInt (num1);

    let num2 = prompt("Please enter second number");

    if (num2 != null) {
        num2 = parseInt (num2);

        let operation = prompt("Please enter sign of operation <+;-;*;/>");

        if (operation == '+') {
            console.log(num1 + num2);
        } else if (operation == '-') {
            console.log(num1 - num2);
        } else if (operation == '*') {
            console.log(num1 * num2);
        } else if (operation == '/') {
            console.log(num1 / num2);
        } else {
            console.log("You should enter type of operation!");  
        }

    }  else {
        console.log("You should enter second number");
    }
 
} else {
    console.log("You should enter first number");
}