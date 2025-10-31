function solution(nums) {
    var answer = 0;
    var arr = [...new Set(nums)] // 집합 자료형을 통한 중복 제거
    var len = nums.length / 2
    
    answer = Math.min(arr.length, len) // 중복 제거한 원소 수와 총 원소의 절반 중 작은 수
    return answer;
}