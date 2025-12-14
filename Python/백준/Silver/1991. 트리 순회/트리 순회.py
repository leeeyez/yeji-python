# 트리 순회
# 전위 순회, 중위 순회, 후위 순회 결과 출력

import sys
input = sys.stdin.readline

n = int(input())
tree = {} 

# 트리 정보 입력받기
for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = [left, right]  # 딕셔너리에 저장


# 전위 순회 함수
def preorder(node):
    # '.'은 자식이 없다는 뜻이므로 그냥 돌아가기
    if node == '.':
        return
    
    # 전위 순회: 나 → 왼쪽 → 오른쪽
    print(node, end='')           # 1. 나를 출력
    preorder(tree[node][0])        # 2. 왼쪽 자식으로 가기
    preorder(tree[node][1])        # 3. 오른쪽 자식으로 가기


# 중위 순회 함수  
def inorder(node):
    if node == '.':
        return
    
    # 중위 순회: 왼쪽 → 나 → 오른쪽
    inorder(tree[node][0])         # 1. 왼쪽 자식으로 가기
    print(node, end='')            # 2. 나를 출력
    inorder(tree[node][1])         # 3. 오른쪽 자식으로 가기


# 후위 순회 함수
def postorder(node):
    if node == '.':
        return
    
    # 후위 순회: 왼쪽 → 오른쪽 → 나
    postorder(tree[node][0])       # 1. 왼쪽 자식으로 가기
    postorder(tree[node][1])       # 2. 오른쪽 자식으로 가기
    print(node, end='')            # 3. 나를 출력



# 실행 (A부터 시작)
preorder('A')
print()  # 줄바꿈
inorder('A')
print()  # 줄바꿈
postorder('A')