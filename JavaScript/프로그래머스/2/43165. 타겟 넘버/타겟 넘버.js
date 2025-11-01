function solution(numbers, target) {
    var answer = 0;
    
    function dfs(idx, sum)  {
        if (idx === numbers.length) { // 모든 숫자 사용
            if (sum === target) answer++; // 다 사용했을 때 target 나오면 answer++
            return;
        }
        
        dfs(idx + 1, sum + numbers[idx]);
        
        dfs(idx + 1, sum - numbers[idx]);
    }
    
    dfs(0,0)
    return answer;
}

// bfs
// function solution(numbers, target) {
//     let answer = 0;
//     const queue = [[0, 0]]; // [index, sum]
    
//     while (queue.length > 0) {
//         const [index, sum] = queue.shift();
        
//         if (index === numbers.length) {
//             if (sum === target) answer++;
//             continue; // 다음 반복문으로 (아래 실행X)
//         }
        
//         queue.push([index + 1, sum + numbers[index]]);
//         queue.push([index + 1, sum - numbers[index]]);
//     }
    
//     return answer;
// }