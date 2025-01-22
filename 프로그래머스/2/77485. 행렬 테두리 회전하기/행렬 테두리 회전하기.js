function solution(rows, columns, queries) {
    const matrix = [...new Array(rows)].map((_, i) => {
        return [...new Array(columns)].map((_, j) => (i * columns + j + 1))
    })
    
    
    function rotate(x1, x2, y1, y2) {
        let currentValue = matrix[x1][y1]
        let minimumValue =  matrix[x1][y1]
        for(let y = y1; y < y2 ; y++){
            const tmp = matrix[x1][y+1]
            if(tmp < minimumValue) minimumValue = tmp
            matrix[x1][y+1] = currentValue
            currentValue = tmp
        }
        for(let x = x1; x < x2 ; x++){
            const tmp = matrix[x+1][y2]
            if(tmp < minimumValue) minimumValue = tmp
            matrix[x+1][y2] = currentValue
            currentValue = tmp
        }
        for(let y = y2; y > y1 ; y--){
            const tmp = matrix[x2][y-1]
            if(tmp < minimumValue) minimumValue = tmp
            matrix[x2][y-1] = currentValue
            currentValue = tmp
        }
        for(let x = x2; x > x1 ; x--){
            const tmp = matrix[x-1][y1]
            if(tmp < minimumValue) minimumValue = tmp
            matrix[x-1][y1] = currentValue
            currentValue = tmp
        }
        return minimumValue
    }
    var answer = [];
    for(q of queries){
       let {0: x1, 1: y1, 2: x2, 3: y2} = q
       x1 -= 1
       x2 -= 1
       y1 -= 1
       y2 -= 1
       answer.push(rotate(x1, x2, y1, y2))
   }

    return answer;
}