function solution(clothes) {
    const map = new Map();
    for (let [name, type] of clothes) {
        if (!map.has(type)) map.set(type, []);
        map.get(type).push(name);
    }
    
    var answer = 1;
    for (let [type, items] of map) {
        answer *= (items.length + 1) // +1 하는 이유 : 안 입는 경우 포함
    }
    
    return answer - 1; // 아무것도 안 입는 경우 뺴기
}

// 전체(각 종류별로 하나씩) - 아무것도 안입기