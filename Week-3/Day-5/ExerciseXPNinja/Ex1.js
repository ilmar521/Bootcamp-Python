let obj1 = {
    FullName: 'Lunev Kirill',
    Mass: 80,
    Height: 176,
    BMI: function () {
        return this.Mass / this.Height;
    }
}

let obj2 = {
    FullName: 'Lunev Lev',
    Mass: 45,
    Height: 154,
    BMI: function () {
        return this.Mass / this.Height;
    }
}

function compareObjects(obj1, obj2) {
    if (obj1.BMI() > obj2.BMI()) {
        return obj1.FullName;     
    } else {
        return obj2.FullName;     
    }
}

console.log(compareObjects(obj1, obj2));