function recursion(k, dungeons, count){
    if(dungeons.length == 0){
        return count
    }
    var result = []
    for (var i = 0; i < dungeons.length; i++){
        const n_dungeons = dungeons.filter((value, index, arr) => {
            return index != i
        })
        if(dungeons[i][0] <= k){
            result.push(recursion(k - dungeons[i][1], n_dungeons, count + 1))
        }else{
            result.push(recursion(k, n_dungeons, count))
        }
    }
    return Math.max(...result)
}

function solution(k, dungeons) {

    var answer = -1;
    return recursion(k, dungeons, 0);
}