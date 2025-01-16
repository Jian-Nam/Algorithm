function f(number){
    let quotient = Math.floor(number / 2)
    let remain = number % 2
    let value = 1
        
    while(remain === 1){
        remain = quotient % 2
        quotient =  Math.floor(quotient / 2)
        value *= 2
    }
    
    return number + Math.ceil(value / 2)
    
}

function solution(numbers) {
    var answer = [];
    for(n of numbers){
        answer.push(f(n))
    }

    return answer;
}