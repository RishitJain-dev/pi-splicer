import { alphaPi } from './splicer.js'
import { getVars } from './config.js';

export function searchString(final) {
    const { pidigits, maxsearch, searchValue, statusTxt, outputTxt } = getVars();
    let searchTerm = searchValue.toUpperCase()
    if (searchTerm.length > maxsearch) {
        statusTxt.innerText = "too long of a search, will take years to finish"
        return
    }   
    let indexPosition = final.indexOf(searchTerm);
    if (indexPosition == -1) {
        statusTxt.innerText = `${searchTerm} is not in ${pidigits} digits of pi, you will need to increase search range.`;
        return
    }
    outputTxt.innerText = `we found "${searchValue}" beginning at digit ${indexPosition} of pi!`
}