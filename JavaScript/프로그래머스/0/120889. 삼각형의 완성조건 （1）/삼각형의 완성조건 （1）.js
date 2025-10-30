function solution(sides) {
    var answer = 2;
    arr = [...sides].sort((a,b) => a-b);
    
    if (arr[2] < arr[0] + arr[1]) {
        answer = 1
    }
    return answer;
}