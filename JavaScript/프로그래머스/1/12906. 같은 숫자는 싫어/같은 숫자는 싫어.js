function solution(arr)
{
    var answer = [];

    for (let i=0; i<arr.length; i++){
        if (i===0 || arr[i-1] != arr[i]) answer.push(arr[i])
    }
    
    return answer;
}

function solution(arr)
{
    // 현재 val이 그 다음 인덱스 원소와 같지 않으면 남김
    return arr.filter((val,index) => val != arr[index+1]);
}
