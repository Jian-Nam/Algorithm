function solution(players, callings) {
    var p_dict = {};
    for(i in players){
        p_dict[players[i]] = parseInt(i);
    }
    
    for(c of callings){
        index = p_dict[c]
        front = players[index - 1]
        
        players[index - 1] = c
        players[index] = front
        
        p_dict[c] -= 1
        p_dict[front] += 1
        // console.log(players)
        // console.log(p_dict)
    }
    return players;
}