// 가격이떨어지지 않은 기간은 몇 초인지 return

function solution(prices) {
    let len = prices.length;
    let answer = Array(prices.length).fill(0);
    
    // "가격이 떨어지지 않은 기간"은 가격이 떨어지는 순간까지의 시간
    // 아래 코드는 떨어졌다가 다시 오르면 또 카운트
    // for (let i=0; i<len-1; i++) {
    //     for (let j=i+1; j<len; j++) {
    //         if (prices[i] <= prices[j]) answer[i]++
    //     }
    // }
    
    for (let i=0; i<len-1; i++) {
        for (let j=i+1; j<len; j++) {
            answer[i]++; // 일단 카운트하고
            if (prices[i] > prices[j]) break; // 떨어지면 break
        }
    }
    
    return answer;
}