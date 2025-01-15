function validateRoom(room){
    for (let i = 0; i < 5; i++){
        for (let j = 0; j < 5; j++){
            if(room[i][j] === "P"){
                const result = recursion(room, 0, i, j, [{i:i, j:j}])
                if(result === false) return false
            }
        }
    }
    return true
}

function recursion(room, distance, i, j, history){
    const current = room[i][j]
    if(distance === 1 && current === "X") return true
    if(distance >= 1 && current === "P") return false
    if(distance >= 2 && (current ==="X" || current ==="O") ) return true
    

        
    const directions = [{i:0, j:1},{i:0, j:-1},{i:-1, j:0},{i:1, j:0}]
    for(d of directions){
        const ni = i + d.i
        const nj = j + d.j

        if(ni < 5 && nj < 5 && ni >=0 && nj >= 0){
            if(validateHistory(history, ni, nj)=== false)continue;
            
            nhistory = history.slice()
            nhistory.push({i:ni, j:nj})
            const result = recursion(room, distance + 1, ni, nj, nhistory)
            if(result === false) {
                return false

            }
        }
    }
    return true
}

function validateHistory(history, ni, nj){
    for(h of history){
        if(h.i === ni && h.j === nj) return false
    }
    return true
}

function solution(places) {
    // 네가지 방향 순회
    // 배열 복사해서 전달
    var answer = [];
    for(let room = 0; room< 5; room++){
        const result = validateRoom(places[room])
        if(result === true) answer.push(1)
        else answer.push(0)
    }
    

    return answer;
}