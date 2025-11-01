function solution(citations) {
    let n = citations.length;
    
    // H는 0부터 n까지 가능
    for (let h = 0; h <= n; h++) {
        // h번 이상 인용된 논문 개수
        let count = citations.filter(c => c >= h).length;
        
        if (count >= h) {
            answer = h; // 최댓값 갱신
        }
    }
    
    return answer;
}

// 이진 탐색 (O(logn))
function solution(citations) {
    let left = 0; // H의 최솟값
    let right = citations.length; // H의 최댓값
    let answer = 0;
    
    while (left <= right) {
        let h = Math.floor((left + right) / 2); // 중간값 (floor = 내림)
        let count = citations.filter(c => c >= h).length; // h번 이상 인용된 논문 개수
        
        if (count >= h) {
            answer = h; // 갱신
            left = h + 1; // 더 큰 값이 있나 탐색
        } else {
            right = h - 1; // 범위를 줄임
        }
    }
    
    return answer;
}