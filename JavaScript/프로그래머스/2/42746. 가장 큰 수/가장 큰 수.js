function solution(numbers) {
    var answer = '';
    // 문자열로 정렬하면 사전순정렬(내림차순)
    let sortString = numbers.map(n => String(n))
    .sort((a, b) => (b + a) - (a + b)); // 303 - 330 문자열이 자동으로 숫자로 형변환
    // 내림차순
    
    answer = sortString.join('');
    return answer[0] === '0' ? '0' : answer;
    // numbers 배열에 0밖에 없을 경우에만 [0]이 0이됨 '000' -> '0'
}