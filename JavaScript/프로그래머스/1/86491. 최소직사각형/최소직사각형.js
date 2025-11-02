function solution(sizes) {
    var answer = 0;
    
    // 가로를 길게 하기
    let sortSize = sizes.map(([x,y]) => {
        if (x < y) return [y,x] 
        else return [x,y]
    })

    let xSize = 0, ySize = 0;
    for (let [x,y] of sortSize) {
        xSize = Math.max(xSize, x);
        ySize = Math.max(ySize, y);
    }
    
    return xSize*ySize;
}

// reduce로 푸는 방법
// function solution(sizes) {
//     const [hor, ver] = sizes.reduce(([h, v], [a, b]) => [Math.max(h, Math.max(a, b)), Math.max(v, Math.min(a, b))], [0, 0])
//     return hor * ver;
// }