// 네트워크 개수

function solution(n, computers) {
    var answer = 0;
    let visited=Array(n).fill(false);
    
    function bfs(start) {
        visited[start] = true;
        let queue = [start];
        let queueIndex = 0;
        
        while (queueIndex < queue.length) {
            let node = queue[queueIndex++];
            
            // 현재 노드와 연결된 모든 컴퓨터 확인
            for (let i = 0; i < n; i++) {
                // 연결되어 있고 && 방문하지 않았다면
                if (computers[node][i] === 1 && !visited[i]) {
                    visited[i] = true;
                    queue.push(i);
                }
            }
        }
    }
    
    for (let i=0; i<n; i++) {
        if (!visited[i]) {
            bfs(i);
            answer++;
        }
    }
    return answer;
}