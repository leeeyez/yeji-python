function solution(phone_book) {
    var answer = true;
    phone_book.sort(); // 문자열 사전순으로 정렬 -> 접두어끼리는 반드시 “이웃”
    var pl = phone_book.length
    
    // 효율성 테스트 시간초과 (2개)
    // for (let i = 0; i < pl; i++) {
    //     for (let j = i+1; j < pl; j++) {
    //         if (phone_book[j].startsWith(phone_book[i])) {
    //             return false
    //         }
    //     }
    // }
    
    // 이미 사전순으로 sort했기 때문에 이웃끼리만 비교해도 된다.
    for (let i = 0; i < pl-1; i++) {
        if (phone_book[i+1].startsWith(phone_book[i])) {
            return false
        }
    }
    return answer;
}