function move(start, keyword, park){
    let dir_dict = {"E": [0, 1], "N": [-1, 0], "W": [0, -1], "S": [1, 0]}
    let [direction, distance] = keyword.split(" ")
    direction = dir_dict[direction]
    distance = parseInt(distance)
    
    let di = start[0] + direction[0] * distance
    let dj = start[1] + direction[1] * distance
    
    if(di < 0 || di >= park.length || dj < 0 || dj >= park[0].length){
        return false
    }
    for (let i = 1; i < (distance + 1); i++){
        if(park[start[0] + direction[0] * i][start[1] + direction[1] * i] == "X"){
            return false
        }
    }
    return [di, dj]
}

function solution(park, routes) {
    let start;
    for(let i= 0; i < park.length; i++){
        for (let j = 0; j < park[0].length; j++){
            let spot = park[i][j];
            if(spot === "S"){
                start = [i, j];
            }
        }
    }
    
    let position = start
    for(let r of routes){
        let destination = move(position, r, park);
        if(destination){
            position = destination
        }
    }
    

    return position;
}