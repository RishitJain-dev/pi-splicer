import { pidigits, includeascii, maxsearch, search, outputTxt, statusTxt } from "./config";

spinners = ["▖", "▘", "▝", "▗"]

export function search() {
    let searchTerm = search.upper()
    if (length(searchTerm) > maxsearch) {
        statusTxt.innerText = "too long of a search, will take years to finish"
        return
    }

    
}