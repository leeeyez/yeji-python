function solution(s){
    var answer = true;
    var arr = s.split('')
    
//     open = 0
//     isClose = false
    
//     for (let i=0; i<arr.length; i++) {
//         if (arr[i] === '(') {
//             if (open > 0 && isClose === true) return false
//             else if (open === 0 && isClose === true) return false
//             else open++
//         } else {
//             if (open === 0) return false
//             else {
//                 open--
//                 isClose = true
//             }
//         }
        
//         if (open === 0 && isClose === true) isClose = false

//     }
    var open = 0;
    for (let i=0; i<arr.length; i++) {
        if (arr[i] === '(') open++
        else open--
        
        if (open < 0) return false // 음수로 넘어가면 불가능
    }
    answer = open === 0

    return answer;
}

function solution(s){
    let cum = 0
    for (let paren of s) {
        cum += paren === '('? 1: -1 // 삼항연산자로 표현 가능
        if(cum < 0) {
            return false
        }
    }
    return cum === 0? true: false;
}