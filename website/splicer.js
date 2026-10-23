const alphabet = [
    "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", 
    "P", "Q", "R", "S", "T", 
    "U", "V", "W", "X", "Y", 
    "Z"
];
let comb = "";

let converted = [];
export let alphaPi = "";

export function splice(pistring) {
    converted = [];
    pistring = pistring.replace(".", "");

    for (let i = 0; i < pistring.length; i++) {
        comb = pistring.slice(i, i+2);
        comb = parseInt(comb); //gets rid of 0s at start
        //05 -> 5

        if (comb >= 26) { //0-25
            if (comb <= 78) {
                comb = comb % 26;
            } else {
                continue;
            }
        }
        converted.push(alphabet[comb]);
        
        alphaPi = converted.join("");
    }
    return alphaPi
}
