function solution(participant, completion) {
    var answer = '';
    
    // 1차 시도
    // participant.forEach(p => {
    //     if (!completion.includes(p)) answer += p
    // }) // -> 동명이인 확인 불가
    
    // ------------------------------------------------
    
    // 2차 시도 : 효율성 통과 X (시간 초과)
    // completion.forEach((c) => {
    //     if (participant.includes(c)) {
    //         participant.splice(participant.indexOf(c), 1) // 해당 원소 인덱스 통해 삭제
    //     }
    // })
    // answer = participant[0]
    
    // ------------------------------------------------
    
    const map = new Map();
    
    // 참가자 등록 (이름 : 수) - 동명이인 3명이면 예지: 3
    participant.forEach(p => {
        map.set(p, (map.get(p) || 0) + 1)
    });
    
    // 완주한 사람 수 빼기
    completion.forEach(c => {
        map.set(c, map.get(c) - 1)
    });
    
    // 수가 0 이상인 이름이 있으면 출력
    for (let [name, cnt] of map) {
        if (cnt > 0) return name
    }
}