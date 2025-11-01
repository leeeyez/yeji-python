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


function solution(progresses, speeds) {
    let answer = [0];
    let days = progresses.map((progress, index) => Math.ceil((100 - progress) / speeds[index])); // map을 통해 days로 바로 변환하여 저장 [7,7,9]
    let maxDay = days[0]; // maxDay 초깃값을 첫번째 배포날로 정함

    for(let i = 0, j = 0; i< days.length; i++){
        if(days[i] <= maxDay) { // maxDay보다 작게 걸리면 이전 작업과 같이 배포되므로 answer += 1
            answer[j] += 1;
        } else { // maxDay보다 길게 걸리면 maxDay 갱신 후 answer 그 다음 인덱스에 1
            maxDay = days[i];
            answer[++j] = 1;
        }
    }

    return answer;
}