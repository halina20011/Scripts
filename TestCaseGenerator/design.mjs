export class Design{
    constructor(f = []){
        this.fLength = f.length;
        this.f = f;
    }

    generate(){
        return this.f.map(fu => { return fu(); });
    }

    generateLen(len){
        return Array.from({length: len}, () => { return this.generate(); });
    }
}
