const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let lenghtOfUsers = users.length;

if (lenghtOfUsers == 0) {
    console.log('no one is online');
} else if (lenghtOfUsers == 1) {
    console.log(`${users[0]} is online`);
} else if (lenghtOfUsers == 2) {
    console.log(`${users[0]} and ${users[1]} is online`);
} else if (lenghtOfUsers > 2) {
    console.log(`${users[0]} and ${users[1]} and ${lenghtOfUsers - 2} more are online`);
}