let str = '';

for (let i = 0; i < 6; i++) {
    str += '* ';    
    console.log(str)   
}

for (let i = 0; i < 6; i++) {  
    str = '';
    for (let x = 0; x <= i; x++) {
        str += '* ';       
    }
    console.log(str)
}