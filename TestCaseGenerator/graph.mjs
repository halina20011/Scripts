export function allPairs(from, length){
    const res = [];
    const n = from + length;
    for(let i = from; i < n; i++){
        for(let j = i + 1; j < n; j++){
            res.push([i, j]);
        }
    }

    return res;
}

export function randomGraph(connected){
    return
}

Array.prototype.adjacencyList = function(from, length){
    const nodes = new Map();
    this.forEach(c => {
        const a = c[0];
        const b = c[1];
        if(!nodes.has(a)){
            nodes.set(a, new Set());
        }
        if(!nodes.has(b)){
            nodes.set(b, new Set());
        }
        nodes.get(a).add(b);
        nodes.get(b).add(a);
    });

    const answer = [];
    for(let i = from; i < from + length; i++){
        const connected = (nodes.has(i)) ? Array.from(nodes.get(i).keys()) : [];
        answer.push(connected);
    }

    return answer;
}
