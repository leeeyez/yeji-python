function solution(n, k) {
    var answer = 0;
    const ggochi = parseInt(n / 10)
    
    answer = n * 12000 + (k-ggochi) * 2000
    return answer;
}