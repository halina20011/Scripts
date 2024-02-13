import * as array from "./array.mjs";
import * as random from "./random.mjs";
import * as binaryTree from "./binaryTree.mjs";
import * as string from "./string.mjs";
import * as design from "./design.mjs";

Object.assign(globalThis, array);
Object.assign(globalThis, random);
Object.assign(globalThis, binaryTree);
Object.assign(globalThis, string);
Object.assign(globalThis, design);

String.prototype.str = function(){
    return `"${this}"`;
}

Number.prototype.str = function(){
    return `"${this}"`;
}

// [...Array(100).keys()].fromRandom(100);


const multipleOf = (n, len) => {
    return Array.from({length: len}, (_,i) => (i * n));
}

function matrix(x, y, fill){
    return Array.from({length: y}, () => {
        return Array.from({length: x}, () => fill);
    });
}

function dec2Bin(dec){
    return (dec >>> 0).toString(2);
}

Array.prototype.randomRotate = function(){
    const k = r(0, this.length);
    return this.rotate(k);
}

Array.prototype.rotateJoin = function(arr2){
    const arr = [];
    
    for(let i = 0; i < this.length; i++){
        arr.push(this[i]);
        arr.push(arr2[i]);
    }

    return arr;
}

function run(count, f){
    for(let i = 0; i < count; i++){
        f();
    }
}

const l = console.log;

// node usefullFunctions.js | tee /dev/tty | xclip -sel clip
function main(){
    // const min =  1;
    // const max =  10000;
    // const max =  1001;
    // const size = r(10000,50000);
    // const d = new Design([
    //     () => { return "n"; }, () => { return r(1, 500).toString();}, () => { return set.fromRandom(2).join("");}
    // ]);

    const f = () => {
        // const v = r(0,100);
        // l(fromRegEx(/[0-9]/).fromRandom(v).join("").str());
        // const tree = arrayFromTo(1, 10000).shuffle().toBinaryTree();
        // l(tree.binaryTreeDescription().str());
        // l(fromRegEx(/[0-9]/).random.join("").str());
        // l(d.generateLen(50000).str());
        // l(randomArrayFunc(0, 100000, (index, val) => {return index == val;}, 100000).str());
        // l(fromRegEx(/[a-z ]/).fromRandom(1000).join("").str());
        // const max = 2000;
        // const s1 = r(450, 500);
        // l(randomArray(1, max, s1).str());
        // const s2 = r(450, 500);
        // l(randomArray(1, 1000000001, 100).removeDuplicates().str());
        const array = randomArray(-500, 500, 400);
        const table = array.sumTable();
        if(table[0][1] == 1){
            l(array.sortArray().str());
            l(table[0][0]);
        }
        // l(randomArray(0, 10, size).str());
        // l(r(0, 100001));
        // l(randomMatrix(1,1, 20, 20).str());
        // const m = r(20,200);
        // const n = r(20,200);
        // const n = 200;
        // const m = 200;
        // l(r(min, max));
        // l(r(1, 1000000001));
        // l(randomBinMatrix(m, n).str());
        // const size = r(1, fullNodeCount(9));
        // l(randomArray(1, 10000, 100000).str());
        // l(randomArray(50000, 50001, 50000).str());
        // const n = () => l(arrayFromTo(0, 10).fromRandom(1000).join("").str());
        // l();
        // l(fromRegEx(/[a-z]/).fromRandom(50000).join("").str());
        // l(size);
        // l(fromRegEx(/[a-z]/).fromRandom(50000).join("").str().cost());
        // const ar1 = ["Solution"]
        // const ar2 = [[arrayFromTo(0, 50)]];
        // const shuffle = newArray("shuffle", 8500);
        // const repeat = newArray("reset", 1500);
        // const arr = [...shuffle, ...repeat];
        // arr.shuffle();
        // ar2.push(...newArray([], 10000));
        // ar1.push(...arr);
        // l(ar1.str());
        // l(ar2.str());
        // l(randomArray(100, 101, size - 1).str());
        // console.log(randomArray(1, 2, 3000).str());
        // console.log(12);
        // l(randomArray(30, 101, 100000).str());
        // const n = r(min, max+1);
        // const k = r(1, Math.pow(2, n-1)+1);
        // console.log(n);
        // console.logMath.(k);
        // const arr = arrayFromTo(0, 100000);
        // arr[1] = arr[0];
        // console.log(arr.str());
        // console.log(string.str());
        // l(randomMatrix(1, 100001, 10000, 2).str());
        // console.log(r(min, max));
        // const m = r(min, max);
        // const n = r(min, max);
        // console.log(randomBinMatrix(n, m).map(row => row.sort((a, b) => b - a)).str());
        // console.log(randomMatrix(-1000, 1001, n, m).str());
        // l(randomMatrix(0, 256, 200, 200).str());
        // l(randomBinString(10000).str());
        // l(r(1, 30));
        // l(r(1, 30));
        // l(r(300, 1000));
        // console.log(randomMatrix(0, 0, n, m).map(row => row.sort((a, b) => b - a)).str());
        // console.log(r(min, m));
        // console.log(m);
        // l(randomArray(0, 5, 8).str());
        // const arr = [1,2,3,4,5,6,7].sortArray();
        // const s = r(2, 1000001);
        // const arr = arrayFromTo(1, s).shuffle().cut(100000);
        // l(arr.str());
        // l(r(100000,1000000001));
        // l(randomArray(0,1000, 1000).removeDuplicates().adjacentPairs().shuffle().str());
        // const n = 100;
        // const arr = randomArray(1,n,n*2/3).sortArray().duplicates();
        // console.log(arr.str());
        // console.log(100);
        // l(createTreeArrayShort(randomTree(0, 100000, 5000)).str());
        // const tree = bst(arr, 0, arr.length - 1);
        // console.log(createTreeArrayShort(tree).str());
        // console.log(r(min, arr.length));
    }
    run(8, f);
    // l(randomArray(0, 1, 100000).str());
    // l(randomArray(10000, 10001, 99999).str());
    // l(randomArray(1000000000, 1000000001, 100000).str());
    // console.log(randomArray(0, 1000, 20000).str());
    // console.log(linkedListRandom(-1000, 1000, 1000).str());
    // console.log(Array.from({length:10000}, () => 2147483647).str());
    // console.log(Array.from({length:10000}, () => -2147483648).str());
    // console.log(fromASCII(100));
    // console.log(fromRegEx(/[a-z]/).fromRandom(200).join("").stringFromMagazine(100).itemStr());
    // console.log(fromRegEx(/[a-zA-Z]/).fromRandom(1000).join(""));
    // console.log(randomBinArray(100000).join("").replace(/0/g, "N").replace(/1/g, "Y").str());
    // console.log(Array.from({length: 1000}, () => '(').join("") + Array.from({length: 1000}, () => ')').join(""));
    // console.log(generateChain(0, 1000, 1000, 5).str());
}

main();
