import {pidigits, includeascii, maxsearch, search, outputTxt} from '/config.js'
import Decimal from 'https://cdn.skypack.dev/decimal.js';


Decimal.set({precision: pidigits + 2});

export const pistring = Decimal.acos(-1).tostring();
//acos(-1) = pi

export function getpi() {
    outputTxt.textContent = pistring;
}