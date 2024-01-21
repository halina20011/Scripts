export function randomTree(min, max, size){
    if(size < 0){
        return null;
    }
    size--;
    const root = new Node(r(min, max));
    const random = r(0, 4);
    // 0    no children
    // 1    left child
    // 2    right child
    // 3    both
    if(random == 1 || random == 3){
        root.left = randomTree(min, max, size);
    }
    if(random == 2 || random == 3){
        root.right = randomTree(min, max, size);
    }

    return root;
}

// function randomNTree(min, max, maxChildren, count){
//     const answer = [];
//     
// }

// bst
class Node{
    constructor(data){
        this.data = data;
        this.right = null;
        this.left = null;
    }
}

export function bst(arr, left, right){
    if(right < left){
        return null;
    }

    const m = left + Math.floor((right - left) / 2);
    const root = new Node(arr[m]);
    root.left = bst(arr, left, m - 1);
    root.right = bst(arr, m + 1, right);

    return root;
}

export function buildShort(array){
    const stack = [];
    const tree = new Node(array[0]);
    stack.push(tree);
    let index = 1;
    while(stack.length && index < array.length){
        let levelSize = stack.length;
        while(levelSize--){
            const parent = stack.shift();
            if(array[index] != null && !isNaN(array[index])){
                const left = new Node(array[index]);
                parent.left = left;
                stack.push(left);
            }
            index++;
            if(array[index] != null && !isNaN(array[index])){
                const right = new Node(array[index]);
                parent.right = right;
                stack.push(right);
            }
            index++;
        }
    }

    return tree;
}

export function createTreeArrayShort(tree){
    const stack = [];
    const array = [];
    stack.push(tree);
    let continueToNextLevel = true;
    while(stack.length && continueToNextLevel == true){
        let levelSize = stack.length;
        continueToNextLevel = false;
        while(levelSize--){
            const tr = stack.shift();
            array.push(((tr == null) ? null : tr.data));
            if(tr != null){
                if(tr.left != null || tr.right != null){
                    continueToNextLevel = true;
                }
                stack.push(tr.left);
                stack.push(tr.right);
            }
        }
    }

    return array;
}

// height is number of levels without root level counted
//      1
//    2   3
//  4  5 6 7
//  height = 2 
//  2 ^ (2 + 1) - 1 = 8 - 1 = 7
export function fullNodeCount(height){
    return Math.pow(2, height + 1) - 1;
}

