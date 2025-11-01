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

// 장르별 총재생횟수 객체 / {장르, 재생수, 고유번호} 갖는 객체 배열 두가지로 나누어 비교
function solution(genres, plays) {
    var dic = {};
    genres.forEach((t,i)=> {
        dic[t] = dic[t] ?  dic[t] + plays[i] :plays[i];        
    }); // 장르별 총 재생수를 담는 객체 {genre: 총재생횟수}

    var dupDic = {};
    return genres          
          .map((t,i)=> ({genre : t, count:plays[i] , index:i})) // 객체 배열로 전환
          .sort((a,b)=>{  // 정렬             
               if(a.genre !== b.genre) return dic[b.genre] - dic[a.genre]; // 장르 총합 기준 (내림차순)
               if(a.count !== b.count) return b.count - a.count; // 장르 내 재생횟수 기준 (내림차순)
               return a.index - b.index; // 고유번호 기준 (오름차순)
           })
           .filter(t=>  {
               if(dupDic[t.genre] >= 2) return false; // 장르의 노래가 2개 이상이면 false -> 필터로 제거
               dupDic[t.genre] = dupDic[t.genre] ? dupDic[t.genre]+ 1 : 1; // 아니면 dupPic에 추가
               return true;
            })
           .map(t=> t.index);  // index만 뽑기
}