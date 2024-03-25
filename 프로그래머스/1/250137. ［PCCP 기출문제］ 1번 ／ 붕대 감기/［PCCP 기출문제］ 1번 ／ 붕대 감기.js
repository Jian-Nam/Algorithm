function solution(bandage, health, attacks) {
    const [duration, heal, bonus] = bandage;
    
    var current_time = 0;
    var hp = health
    
    for(i in attacks){
        var [time, attack] = attacks[i];
        var time_between =  time - (current_time + 1);
        var bonus_flag = Math.floor(time_between / duration)
        
        var heal_amount = time_between * heal + bonus_flag * bonus
        hp = Math.min(health, hp + heal_amount);
        
        hp -= attack
        if(hp <= 0){
            return -1
        }
        current_time = time
    }
    
    
    return hp;
}