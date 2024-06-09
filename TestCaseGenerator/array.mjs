Array.prototype.str = function(){
    return JSON.stringify(this);
}

Array.prototype.itemStr = function(){
    return this.map(item => JSON.stringify(item)).join("\n");
}

Array.prototype.repeat = function(size){
    if(this.length <= 0){
        return [];
    }

    const res = [];
    while(res.length < size){
        for(let i = 0; i < this.length && res.length < size; i++){
            res.push(this[i]);
        }
    }

    return res;
}

Array.prototype.fromRandom = function(len){
    return Array.from({length: len}, () => {
        return this[Math.floor(Math.random() * this.length)];
    });
}

Array.prototype.addBefore = function(array){
    return [...array, ...this];
}

Array.prototype.addAfter = function(array){
    return [...this, ...array];
}

Array.prototype.add = function(item){
    this.push(item);
    return this;
}

Array.prototype.chunkify = function(n){
    const arr = [];
    
    for(let i = 0; i < this.length; i += n){
        arr.push(this.slice(i, i + n));
    }

    return arr;
}

Array.prototype.sumTable = function(){
    const size = this.length;
    const table = new Map();
    for(let i = 0; i < size - 1; i++){
        for(let j = i + 1; j < size; j++){
            const sum = this[i] + this[j];
            if(!table.has(sum)){
                table.set(sum, {val: 1});
            }
            else{
                table.get(sum).val++;
            }
        }
    }

    const array = Array.from(table, ([key, val]) => ([key, val.val]));
    array.sort((a, b) => a[1] - b[1]);
    return array;
}

export function newArray(value, length){
    return Array.from({length: length}, () => value);
}

export function arrayFromTo(min, max){
    const start = Math.min(min, max);
    const end = Math.max(min, max);
    return [...Array.from(Array(end - start), (_, i) => i + min)];
}

Array.prototype.sortArray = function(){
    return this.sort((a, b) => a - b);
}

Array.prototype.reshape = function(n){
    const size = Math.floor(this.length / n);
    const answer = new Array(size);
    
    for(let i = 0; i < size; i++){
        answer[i] = this.slice(i * n, (i + 1) * n);
    }

    return answer;
}

Array.prototype.removeDuplicates = function(){
    const items = {};
    const answer = [];
    for(let i = 0; i < this.length; i++){
        const n = this[i];
        if(items[n] == null){
            answer.push(n);
            items[n] = true;
        }
    }

    return answer;
}

Array.prototype.duplicates = function(){
    let index = 0;
    let prev = null;
    for(let i = 0; i < this.length; i++){
        if(prev !== this[i]){
            this[index++] = this[i];
        }
        prev = this[i];
    }

    return this.slice(0, index);
}

Array.prototype.rotate = function(k){
    k = k % this.length;
    const answer = Array(this.length);
    for(let i = 0; i < this.length; i++){
        answer[i] = this[(this.length - k + i) % this.length];
    }

    return answer;
}

Array.prototype.cut = function(size){
    return this.splice(0, size);
}

Array.prototype.adjacentPairs = function(){
    const pairs = [];
    for(let i = 1; i < this.length; i++){
        pairs.push([this[i-1], this[i]]);
    }
    return pairs;
}
