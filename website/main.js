import { getpi } from './pifinder.js'
import { splice } from './splicer.js'
import { searchString } from './search.js'
import { getVars } from './config.js';

export async function runSplicer() {
    const { statusTxt } = getVars();
    statusTxt.innerText = "working...";

    let piString = await getpi();
    let alphaPi = splice(piString);
    searchString(alphaPi);
}

document.getElementById("spliceButton").addEventListener("click", runSplicer);