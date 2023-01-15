let str1 = "mix";
let str2 = "pod";

let substr1 = str1.substring(0, 2);
let substr2 = str2.substring(0, 2);

let finalStr1 = str1.replace(substr1, substr2);
let finalStr2 = str2.replace(substr2, substr1);

console.log(finalStr1 + " " + finalStr2);