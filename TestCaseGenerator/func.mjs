export function randomArrayMointain(len){
    // create a middle point
    const minM = 1, maxM = len - 1;
    const peek = Math.floor(Math.random() * (maxM - minM) + minM);
    // if the a peek is on left side calculate step
    const step = (peek < len / 2) ? Math.ceil(len - peek / peek) : 1;
    console.log(step);
    const arr = new Array(len);
    let currPos = 0;
    for(let i = 0; i < len; i++){
        if(i <= peek){
            arr[i] = currPos;
            currPos += step;
        }
        else{
            arr[i] = currPos;
            currPos--;
        }
    }

    return arr;
}

export function guass(mean, sigma){
    const u1 = 1 - Math.random();
    const u2 = 1 - Math.random();
    const z = Math.sqrt(-2 * Math.log(u1)) * Math.cos(2.0 * Math.PI * u2);

    return Math.round(mean + sigma * z);
}

export function generateChain(min, max, len, sigma = 1.5){
    return Array.from({length: len}, () => {
        const v1 = r(min, max);
        const v = guass(v1, sigma);
        const v2 = Math.min(Math.max(min, v), max);

        const a = Math.min(v1, v2);
        const b = Math.max(v1, v2);

        if(a == b){
            return [a, b + 1];
        }
        return [a, b];
    });
}
