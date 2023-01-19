let numb = 0;
do {
   numb = Number(prompt('Enter the number'));    
   if (isNaN(numb)) {
    numb = 0;
    alert("You must enter only numbers!");
   } 
}
while (numb < 10);