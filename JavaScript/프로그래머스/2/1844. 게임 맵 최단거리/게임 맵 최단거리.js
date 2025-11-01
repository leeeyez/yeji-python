function solution(maps) {
    var answer = 0;
    let R = maps.length;      // 행의 수
    let C = maps[0].length;   // 열의 수
    
    
    const dr = [1,-1,0,0];
    const dc = [0,0,1,-1];
    
    function bfs(r,c) {
        let visited = new Array(R).fill().map(() => Array(C).fill(0));
        let queue = [[r,c]];
        let queueIndex = 0;
        
        visited[r][c] = 1;
        
        while (queueIndex < queue.length) {
            let [r,c] = queue[queueIndex++];
            
            if (r === 0 && c === 0) return visited[r][c];
            
            for (let i=0; i<4; i++) {
                let nr = r + dr[i]
                let nc = c + dc[i]
                
                if (0 <= nr && nr < R && 0 <= nc && nc < C) {
                    if (maps[nr][nc] === 1 && visited[nr][nc] === 0) {
                        visited[nr][nc] = visited[r][c] + 1;
                        queue.push([nr, nc]);
                    }
                }
            }
        }
        
        return -1
    }
    
    return bfs(R-1,C-1);
}