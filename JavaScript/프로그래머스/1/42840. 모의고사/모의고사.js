function solution(answers) {
    let score = [0,0,0];
    
    const patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    
    for (let i=0; i<answers.length; i++) {
        const correct = answers[i];
        
        for (let j=0; j<3; j++) {
            const curP = patterns[j];
            const curPlen = patterns[j].length;
            
            if (correct === curP[i % curPlen]) score[j]++; 
        }
    }
    
    const maxScore = Math.max(...score);
    
    let answer = [];
    score.forEach((score, idx) => {
        if (maxScore === score) answer.push(idx+1);
    })
    return answer;
}