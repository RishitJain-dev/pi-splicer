import { alphaPi } from './splicer.js'
import { getVars } from './config.js';

export function searchString(alphaPi) {
    const { pidigits, maxsearch, searchValue, statusTxt, outputTxt } = getVars();
    let searchTerm = searchValue.toUpperCase()
    if (searchTerm.length > maxsearch) {
        statusTxt.innerText = "too long of a search, will take years to finish"
        return
    }
    let final = alphaPi.replaceAll("@", "");
    let indexPosition = final.indexOf(searchTerm);
    if (indexPosition == -1) {
        outputTxt.innerText = `${searchTerm} is not in ${pidigits} digits of pi, you will need to increase search range.`;
        return
    } else {
        let placeholderCount = 0;
        let normalCount = 0;
        for (let i = 0; normalCount <= indexPosition; i++) {
            if (alphaPi[i] === "@") {
                placeholderCount += 1;
            } else {
                normalCount += 1;
            }
        }

        outputTxt.innerText = `we found "${searchValue}" beginning at digit ${indexPosition + placeholderCount} of pi!`
    }
}
