export function fromRegEx(regex){
    let letters = "";
    for(let i = 32; i < 127; i++){
        letters += String.fromCharCode(i);
    }
    const r = new RegExp(regex, "g");
    const m = letters.match(r);
    return m;
}

String.prototype.toSafe = function(){
    return (this + '').replace(/[\\"']/g, "\\$&").replace(/\u0000/g, '\\0');
}

export function fromASCII(len){
    str = "";
    for(let i = 0; i < len; i++){
        str += String.fromCharCode(r(33, 127));
    }

    return JSON.stringify(str);
}

export function generateSymbolList(start, end){
    const symbolList = [];

    for(let i = start; i <= end; i++){
        const symbol = String.fromCharCode(i);
        symbolList.push(symbol);
    }

    return symbolList;
}

String.prototype.charCodeCost = function(){
    let cost = 0;
    for(let i = 0; i < this.length; i++){
        cost += this.charCodeAt(i) + 1;
    }

    return cost;
}
