const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let lenghtOfUsers = users.length;

switch (true) {
    case lenghtOfUsers == 1:
        console.log(`${users[0]} is online`);
        break;
    case lenghtOfUsers == 2:
        console.log(`${users[0]} and ${users[1]} is online`);
        break;          
    case lenghtOfUsers > 2:
        console.log(`${users[0]} and ${users[1]} and ${lenghtOfUsers - 2} more are online`);
        break;   
    default:    
    console.log('no one is online');       
}