function solution(n, left, right) {
    var len = n * n
    var arr = []
    for(var i = left; i < right + 1; i++){
        var row = Math.floor(i / n)
        var col = i % n
        if(row > col)   { arr.push(row + 1) }
        else            { arr.push(col + 1) }
    }

    return arr;
}