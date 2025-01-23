;

function solution(s) {

    const stringSet = {
        "{" : "}",
        "(" : ")",
        "[" : "]"
    }
    
    const openStrings = Object.keys(stringSet)
    const closeStrings = Object.values(stringSet)

    const doubledS = s + s

    
    function check(parenthesis){
        const stack = []
        for(p of parenthesis){
            if(openStrings.includes(p)){
                stack.push(p)
                continue
            }
            if(closeStrings.includes(p)){
                const lastOpen = stack.at(-1)
                if(lastOpen === undefined || stringSet[lastOpen] !== p) return false
                stack.pop()
            }
        }
        if( stack.length === 0) return true
        else return false
    }
    
    var answer = 0;
    for(let i = 0; i< s.length; i++){
        const parenthesis = doubledS.slice(i, i + s.length)
        if(check(parenthesis)) answer += 1
    }

    return answer;
}