function solution(wallpaper) {
    const lenx = wallpaper.length;
    const leny = wallpaper[0].length;
    
    let lux = 51;
    let luy = 51;
    let rdx = 0;
    let rdy = 0;
    
    for(let x = 0; x < lenx; x++){
        for(let y = 0; y < leny; y++){
            if(wallpaper[x][y]=== "#"){
                lux = Math.min(x, lux);
                luy = Math.min(y, luy);
                rdx = Math.max(x, rdx);
                rdy = Math.max(y, rdy);
            }
        }
    }
    var answer = [lux, luy, rdx + 1, rdy + 1];
    return answer;
}