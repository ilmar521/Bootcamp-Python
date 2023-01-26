let planets = [
    {planetName: 'Mercury', color: 'red', moonAmount: 0},
    {planetName: 'Venice', color: 'green', moonAmount: 0},
    {planetName: 'Earth', color: 'blue', moonAmount: 1},
    {planetName: 'Mars', color: 'brown', moonAmount: 0},
    {planetName: 'Jupiter', color: 'green', moonAmount: 2},
    {planetName: 'Uran', color: 'yellow', moonAmount: 1},
    {planetName: 'Saturn', color: 'grey', moonAmount: 1},
    {planetName: 'Neptun', color: 'black', moonAmount: 0}
]

let section = document.getElementsByClassName('listPlanets')[0];

for (const obj of planets) {
    let newPlanet = document.createElement('div');
    newPlanet.style.backgroundColor = obj.color;    
    newPlanet.className = 'planet';
    section.appendChild(newPlanet);
    if (obj.moonAmount > 0) {
        for (let i = 0; i < obj.moonAmount; i++) {     
            let newMoon = document.createElement('div');
            newMoon.className = 'moon';
            newPlanet.appendChild(newMoon);            
        }
    }
}