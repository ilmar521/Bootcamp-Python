let family = {
    members: 4,
    lastName: 'Lunev',
    location: 'Israel'
}

for (const x in family) {
    console.log(x);  
}

for (const x in family) {
    console.log(family[x]);  
}