function solution(priorities, location) {
    var answer = 0;
    var maxP = Math.max(...priorities)
    var queue = priorities.map((x, i) => ({ priority: x, idx: i}))
    
    while (queue.length > 0) {
        const current = queue.shift(); // 맨 앞 꺼냄
        
        // max보다 우선순위가 작으면 뒤로
        if (current.priority < maxP) {
            queue.push(current)
        } else { // 최대 우선순위이면 answer++, maxP 갱신
            answer++
            maxP = Math.max(...queue)
            if (current.idx === location) return answer // 찾고자 하는 값이면 return
        }
    }
}

function solution(priorities, location) {
    var answer = 0;
    var queue = priorities.map((x, i) => ({ priority: x, idx: i}))
    
    while (queue.length > 0) {
        const current = queue.shift();
        
        // queue에 남은 것들 중 최대 우선순위 확인
        // 현재보다 높은 우선순위 있다면 true, 없다면 false
        const hasHigherPriority = queue.some(item => item.priority > current.priority);
        
        if (hasHigherPriority) {
            queue.push(current);  // queue에 push (맨 뒤로)
        } else {
            answer++;
            if (current.idx === location) return answer;
        }
    }
}