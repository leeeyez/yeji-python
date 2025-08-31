from collections import deque

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    qimp = deque((imp[i], i) for i in range(n)) # 중요도와 그 인덱스(순서) 쌍을 qimp에 저장

    count = 0
    while True:
        qmax = max(x[0] for x in qimp) # 남은 원소 (중요도, 인덱스) 중 가장 큰 중요도 찾기
        if qimp[0][0] == qmax:   # 중요도가 가장 클 때
            count += 1           # 중요도가 가장 크면 무조건 인쇄하므로 인쇄count + 1
            if qimp[0][1] == m:  # 만약 인덱스가 m일때 (인쇄순서를 찾고자하는 문서일떄ㄴ)
                print(count)     # 지금까지 인쇄 count 출력 후 break
                break
            qimp.popleft()       # 찾고자하는 인덱스가 아니라면 pop
        else:
            qimp.rotate(-1) # 왼쪽이동 (제일 앞 원소를 가장 뒤로)