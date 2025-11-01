function solution(array, commands) {
    var answer = [];
    for (let [i,j,k] of commands) {
        let cutArray = array.slice(i-1,j).sort((a,b) => a-b); // 자르고 오름차순 정렬
        answer.push(cutArray[k-1])
    }
    return answer;
}