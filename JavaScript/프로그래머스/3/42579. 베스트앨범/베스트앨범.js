function solution(genres, plays) {
    
    const map = new Map();
    const len = genres.length;
    
    // key: 장르 / {idx, 재생횟수} 저장
    for (let i=0; i<len; i++) {
        if (!map.has(genres[i])) map.set(genres[i], []);
        map.get(genres[i]).push({ idx: i, play: plays[i]})
    }

    // 각 장르의 노래 총 재생횟수의 합을 통해 장르 순위 정렬
    const sorted = [...map].sort((a,b) => {
        const sumA = a[1].reduce((acc, cur) => acc + cur.play, 0) // 배열로 바꿨을 때 a[0]: key, a[1]: value 전체
        const sumB = b[1].reduce((acc, cur) => acc + cur.play, 0)
        
        return sumB-sumA // 내림차순
    })
    
    const sortedMap = new Map(sorted);
    
    // 장르 내에서 재생횟수, 고유번호에 따라 정렬
    for (let [key, values] of sortedMap) {
        values.sort((a,b) => {
            if (a.play === b.play) return a.idx-b.idx // 재생횟수 같은 경우 고유번호 오름차순
            else return b.play-a.play // 재생횟수 다르면 재생횟수 내림차순
        })
    }
    
    var bestMap = new Map();
    for (let [key, values] of sortedMap) {
        bestMap.set(key, [])
        if (values.length >= 2) { // value가 2개 이상일 때만 2개 잘라서 넣기
            for (let i=0; i<2; i++) {
                bestMap.get(key).push(values[i])
            }
        } else bestMap.get(key).push(values[0]) // 1개일 경우 하나만 넣기
    }
    
    console.log(bestMap)
    
    var answer = [];
    for (let [key, values] of bestMap) {
        for (let value of values) {
            answer.push(value.idx)
        }
    }
    return answer;
}