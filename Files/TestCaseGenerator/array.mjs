Array.prototype.str = function(){
    return JSON.stringify(this);
}

Array.prototype.itemStr = function(){
    return this.map(item => JSON.stringify(item)).join("\n");
}

Array.prototype.fromRandom = function(len){
    return Array.from({length: len}, () => {
        return this[Math.floor(Math.random() * this.length)];
    });
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
