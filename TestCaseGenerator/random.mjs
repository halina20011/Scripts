export function randomArray(min, max, len){
    return Array.from({length: len}, () => {
        return Math.floor(Math.random() * (max - min) + min);
    });
}

export function randomArrayFunc(min, max, func, len){
    return Array.from({length: len}, (_v, i) => {
        let v = Math.floor(Math.random() * (max - min) + min);
        while(func(i, v)){
            v = Math.floor(Math.random() * (max - min) + min);
        }
        return v;
    });
}

Array.prototype.shuffle = function(){
    for(let i = 0; i < this.length; i++){
        const rIndex = r(0, this.length);
        const t = this[i];
        this[i] = this[rIndex]
        this[rIndex] = t;
    }

    return this;
}

export function randomMatrix(min, max, m, n){
    const rand = () => {
        return Math.floor(Math.random() * (max - min) + min);
    }
    const answer = new Array(m);
    for(let y = 0; y < m; y++){
        answer[y] = new Array(n);
        for(let x = 0; x < n; x++){
            answer[y][x] = rand();
        }
    }
    return answer;
}

export const r = (min, max) => {
    return Math.floor(Math.random() * (max - min) + min);
}

export const randomBin = () => {
    return Math.round(Math.random());
}

export const randomBinString = (size) => {
    let ans = "";
    for(let i = 0; i < size; i++){
        ans += Math.round(Math.random());
    }
    return ans;
}

export const randomBinArray = (len) => {
    return Array.from({length: len}, _ => randomBin());
}

export function randoMatrix(x, y, min, max){
    return Array.from({length: y}, () => {
        return Array.from({length: x}, _ => r(min, max));
    });
}

export function randomString(len, options){
    let str = "";
    let availableChars = "";

    for(const option of options){
        console.log(option);
        if(option == "UPPER"){
            availableChars += generateSymbolList(65, 90).join("");
        }
        else if(option == "LOWWER"){
            availableChars += generateSymbolList(97, 122).join("");
        }
        else if(option == "DIGITS"){
            availableChars += generateSymbolList(48, 57).join("");
        }
        else if(option == "SYMBOLS"){
            availableChars += generateSymbolList(33, 47).concat(generateSymbolList(58, 64)).join("");
        }
        else{
            console.error(`option ${option} not available`);
        }
    }
    const size = availableChars.length;
    for(let i = 0; i < len; i++){
        const char = availableChars[Math.floor(Math.random() * size)];
        str += char;
    }

    return str;
}

Array.prototype.randomFromMatrix = function(n, m){
    const size = n * m;
    const arr = this.fromRandom(size);
    return arr.chunkify(n).map(i => i.join(""));
}

export function randomBinMatrix(n, m){
    return Array.from({length: m}, () => {
        return Array.from({length: n}, () => randomBin());
    });
}

export function randomBinMatrixString(n, m){
    return Array.from({length: m}, () => {
        return Array.from({length: n}, () => randomBin()).join("");
    });
}

export function linkedListRandom(min, max, len){
    return Array.from({length: len}, () => {
        return [r(min,max), r(0, len)];
    });
}
