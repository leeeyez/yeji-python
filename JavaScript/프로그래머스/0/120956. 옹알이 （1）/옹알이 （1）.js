function solution(babbling) {
    const words = ["aya", "ye", "woo", "ma"];
    let answer = 0;
    
    for (let word of babbling) {
        // 발음 가능한 옹알이 모두를 " "로 치환
        for (let w of words) {
            word = word.replaceAll(w, " ");
        }
        // 공백 제거한 길이가 0이면 모두 발음 가능 -> answer += 1
        if (word.trim().length === 0) answer += 1
    }
    return answer;
}