function solution(progresses, speeds) {
    var answer = [];
    
    // 각 작업이 며칠째에 배포되는지 answer에 저장 [7,7,9]
    progresses.forEach((p, i) => {
        if (i===0) answer.push(Math.ceil((100 - p) / speeds[i]));
        else {
            answer.push(Math.max(Math.ceil((100 - p) / speeds[i]), answer[i-1]))
        }
    })

    // {7: 2, 9:1} 형태로 변환
    var map = new Map();
    answer.forEach(x => {
        map.set(x, (map.get(x) || 0) + 1)
    })
    
    // day만 ranswer에 저장
    var ranswer = [];
    for (let [day, cnt] of map) {
        ranswer.push(cnt)
    }
    
    return ranswer;
}