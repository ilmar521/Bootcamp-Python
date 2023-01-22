const numbers = [5,0,9,1,7,4,2,6,3,8];

function bubbleSort(arr) {   
    for (let x = 0; x < arr.length; x++) {
       for (let y = 0; y < arr.length; y++) {
            if (arr[y] > arr[y + 1]) {
                let swap = arr[y];
                arr[y] = arr[y + 1];
                arr[y + 1] = swap;
            } 
       }  
    }
    return arr;
}

function bubbleSortReverse(arr) {   
    for (let x = 0; x < arr.length; x++) {
       for (let y = 0; y < arr.length; y++) {
            if (arr[y] < arr[y + 1]) {
                let swap = arr[y + 1];
                arr[y + 1] = arr[y];
                arr[y] = swap;
            } 
       }  
    }
    return arr;
}

console.log(bubbleSort(numbers));
console.log(bubbleSortReverse(numbers));