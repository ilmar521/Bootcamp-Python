let colors = ["green", "red", "blue"];
let suffixes = ['st', 'nd', 'rd'];

for (let i = 0; i < colors.length; i++) {
    console.log(`My ${i + 1}${suffixes[i]} choice is ${colors[i]}`);
}