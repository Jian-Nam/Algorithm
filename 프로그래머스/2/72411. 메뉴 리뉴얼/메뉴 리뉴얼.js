function countOne(value){
    return value.toString(2).split("").reduce((total, current) => total + (current === "1"), 0)
}

function backTrack(setMenu, binary, foods, binaryMap, index, result, course, maxCourse){
    const len = setMenu.length
    const count = countOne(binary)
    if( count < 2) return 
    if(len > maxCourse) return
    if(course.includes(len)) result[len].push({menu: setMenu, count: count})

    for(let i = index; i < foods.length; i++){
        const nFood = foods[i]
        backTrack(setMenu + nFood, binary & binaryMap[nFood], foods, binaryMap, i + 1, result, course, maxCourse)
    }
}

function solution(orders, course) {
    answer = []
    const map = {}
    
    // food 이진법으로 주문한 사람 표현
    orders.forEach((order, index)=>{
        for (food of order){
            //get or default
            map[food] = map[food] || 0
            map[food] += 2 ** index
        }
    })
    
    // 코스 요리 길이, 카운트(order 길이)
    const result = [...new Array(11)].map(()=>[])
    
    const foods = Object.keys(map).sort()
    backTrack("", 2**21-1, foods, map, 0, result, course, Math.max(...course))
    for(r of result){
        let maxCount = 0
        for({menu, count} of r){
            maxCount = Math.max(maxCount, count)
        }
        for({menu, count} of r){
            if(count === maxCount) answer.push(menu)
        }
        
    }
    answer.sort()


    

    return answer;
}