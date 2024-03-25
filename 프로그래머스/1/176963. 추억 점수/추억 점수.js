function solution(name, yearning, photo) {
    let score = {};
    for(i in name){
        score[name[i]] = yearning[i];
    }
    var answer = [];
    for(p of photo){
        var total = 0;
        for(m of p){
            if(Object.keys(score).includes(m)){
                total += score[m];
            }
        }

        answer.push(total)
    }

    return answer;
}