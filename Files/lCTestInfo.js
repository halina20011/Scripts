function isValidUrl(url){
    try{
        return Boolean(new URL(url));
    }
    catch(_e){
        return false;
    }
}

function toInt(str){
    if(typeof str === "number"){
        return str;
    }

    let r = 0;
    for(let i = 0; i < str.length; i++){
        const code = str.charCodeAt(i) - 48;
        if(code < 0 || 9 < code){
            return r;
        }
        r = 10 * r + code;
    }

    return r;
}

const compare = (val1, val2) => {
    const v1 = toInt(val1);
    const v2 = toInt(val2);
    if(v1 == 0 || v2 == 0){
        return null;
    }

    return parseFloat((v2 / v1).toFixed(2));
}

const create = (name, result, expexted) => {
    return {"name": name, "result": result, "expexted": expexted, "compared": compare(result, expexted)};
}

function main(){
    const url = process.argv[2];
    if(!isValidUrl(url)){
        console.log(`invalid url: ${url}`);
        return;
    }
    console.log(url);

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 10000);
    fetch(url, {signal : controller.signal})
        .then(r => r.json())
        .then(t => {
            const data = [
                create("language", t.lang, t.expected_lang),
                create("runtime", t.status_runtime, t.expected_status_runtime),
                create("memory", t.memory, t.expected_memory),
            ];

            console.table(data);
        })
        .catch(err => console.error(err));
}

main();
