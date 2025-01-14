function solution(word) {
    const alphabets = ["A", "E", "I", "O", "U"];
    
    class Alphabet{
        constructor(index){
            this.index = index
            this.alp = "."
            this.children = null
            if(this.index < 6){
                this.children = new Alphabet(this.index + 1)
            }
        }
        next(){
            if(this.index === 5) return true
            if(this.alp === "."){
                this.alp = "A";
                return false
            } else {
                const result = this.children.next();
                if(result){
                    return this.upper()
                }
            }
                
        }
        upper(){
            for(let i = 0; i< 4; i++){
                if(alphabets[i] === this.alp){
                    this.alp = alphabets[i + 1]
                    return false;
                }
            }
            this.alp = "."
            return true
        }
        toString(){
            if(this.index === 5) return "."
            return this.alp + this.children.toString()
        }
    }
    
    const wordLength = word.length

    for(let i = 0; i< 6 - wordLength; i++){
        word = word + "."
    }
    
    count = 0
    const A = new Alphabet(0)
    
    while(true){
        if(A.toString() === word) return count
        
        const result = A.next()
        if(result) break
        
        count++
    }
    
    var answer = 0;
    return answer;
}