import { pidigits, includeascii, maxsearch, search } from '/config'
import { pistring } from './pifinder'

alphabet = [
    "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", 
    "P", "Q", "R", "S", "T", 
    "U", "V", "W", "X", "Y", 
    "Z"
];


converted = [];
export let final = "";

export function splice(pidigits, pistring) {
    converted = [];
    pistring = pistring.replace(".", "");

    for (let i = 0; i <= length(pistring); i++) {
        comb = pistring.splice(i, i+2);

        if (comb > 26) {
            if (comb <= 78) {
                comb = comb % 26;
            }
        }
        if (comb < 10) {
            if (length(comb) == 2) {
                comb = comb.replace("0", "");
            }
        }
        converted.append(alphabet[comb]);
        
        final = "".join(converted);
        return final
    }
}
