const gradesList = [100,57,66,87,43,55];

function findAvg(gradesList) {
    if (gradesList.leght = 0) {
        return 0;
    }
    let summ = 0;
    for (const str of gradesList) {
        summ += str;    
    } 
    return summ / gradesList.leght;
}

function passExam(gradesList) {
    if (findAvg(gradesList) > 65) {
        console.log('Congratulations! You passed the exam!');    
    } else {
        console.log('Sorry, but you can\'t pass the exam. You should take our course again.');    
    }
}

passExam(gradesList);