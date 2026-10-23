
// config.py
// define all variables and globals for all other files
export function getVars() {
    return {
        pidigits: parseInt(document.getElementById("piDigitsInput")?.value, 10) || 100,
        //how many digits of pi it will search thru

        //? checks if the thing exists
        // || is a fallback
        maxsearch: 20,
        // (RESTORED) limits how many characters you can search up at once.
        searchValue: document.getElementById("searchTermInput")?.value || "CNDOEIZFEC",
        // enter search here and it will find it
        statusTxt: document.getElementById("statusTxt"),
        outputTxt: document.getElementById("resultTxt")
    };
}