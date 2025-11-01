function solution(bridge_length, weight, truck_weights) {
    let time = 0;
    let bridge = []; // 다리 위의 트럭들
    let totalWeight = 0; // 다리 위 총 무게
    
    // 대기 트럭을 큐로 변환 (원본 보존)
    let waiting = [...truck_weights];
    
    while (waiting.length > 0 || bridge.length > 0) { // 대기 트럭이 존재하거나 다리 위에 트럭이 존재할떄
        time++;
        
        // 1. 다리 위 트럭들 이동
        bridge = bridge.map(truck => ({
            weight: truck.weight,
            time: truck.time + 1
        }));
        
        // 2. 다리를 다 건넌 트럭 제거
        // 다리 위에 트럭이 있고, 가장 앞의 트럭의 time(시간)이 다리 길이 이상일 떄 (1초에 1씩 전진)
        // 총 무게에서 가장 앞의 트럭 무게 빼줌
        if (bridge.length > 0 && bridge[0].time > bridge_length) {
            totalWeight -= bridge.shift().weight;
        }
        
        // 3. 새 트럭 진입 가능한지 확인
        // 대기하는 트럭이 있고, 지금 다리의 무게 + 진입하려는 트럭 무게 <= 가능 무게
        // 다리 위의 트럭 수가 다리 길이보다 작을 때 진입 가능
        if (waiting.length > 0 && 
            totalWeight + waiting[0] <= weight && 
            bridge.length < bridge_length) {
            
            let newTruck = waiting.shift(); // 대기 중인 트럭 중 맨 앞
            bridge.push({ weight: newTruck, time: 1 });
            totalWeight += newTruck;
        }
    }
    
    return time;
}

// 다리를 깊이 고정 배열로 정의하면 더 깔끔
// time을 같이 관리해줄 필요X
function solution(bridge_length, weight, truck_weights) {
    let time = 0;
    let bridge = Array(bridge_length).fill(0);
    let bridgeWeight = 0;
    
    while (truck_weights.length > 0 || bridgeWeight > 0) {
        time++;
        
        // 맨 앞 트럭 나감
        bridgeWeight -= bridge.shift();
        
        // 새 트럭 들어올 수 있나?
        if (truck_weights[0] && bridgeWeight + truck_weights[0] <= weight) {
            let truck = truck_weights.shift();
            bridge.push(truck);
            bridgeWeight += truck;
        } else {
            bridge.push(0); // 빈 공간
        }
    }
    
    return time;
}