import { getVars } from './config.js';

export async function getpi() {
    const { pidigits, outputTxt, statusTxt } = getVars();
    
    try {
        let fullPi = "";
        let fetched = 0;
        let batchSize = 1000;

        statusTxt.innerText = `getting ${pidigits} of pi...`;

        while (fetched < pidigits) {
            const response = await fetch(`https://api.pi.delivery/v1/pi?start=${fetched}&numberOfDigits=${batchSize}`);
            const data = await response.json(); //converts from json to js object
            fullPi = fullPi + data.content;
            fetched += batchSize;
        }

        statusTxt.innerText = "loaded successfully!!";
        let piString = fullPi.slice(0, pidigits);
        return piString
    } catch (error) { //error is basically just data about what went wrong
        statusTxt.innerText = "couldnt get pi :(";
        console.error(error);
        throw error;
    }
}