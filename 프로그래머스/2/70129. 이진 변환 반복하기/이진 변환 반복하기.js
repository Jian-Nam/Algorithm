function countZero(s){
    return [...s].reduce((acc, cur)=>{
        return cur === "0" ? acc + 1 : acc
    }, 0)
}

function toBinary(n){
    return n.toString(2)
}

function solution(s) {
    var answer = [0, 0];
    while(s !== "1"){
        const count = countZero(s)
        answer[0] += 1
        answer[1] += count
        s = toBinary(s.length - count)
    }

    
    return answer;
}