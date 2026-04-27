import sys

input = sys.stdin.readline

n,m = map(int, input().split())

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = list(range(n + 1)) # 초기 상태에서는 모든 노드가 자기 자신이 부모인 상태
rank = [0] * (n + 1) # rank는 트리의 높이를 나타내며, 초기에는 모든 트리가 높이 0인 상태

def find(x): # root 찾기
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b): #  두 노드 부모 같으면 False, 다르면 연결하고 True
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return False
    # 더 높은 쪽을 부모로 설정, 같으면 a
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True

mst_cost = 0
used = 0
max_included = 0
for weight, a, b in edges:
    if union(a, b):
        mst_cost += weight
        used += 1
        if weight > max_included:
            max_included = weight
        if used == n - 1:  # full MST built
            break

# 그래프가 연결되어 있지 않으면 MST 불가능하나,
# 문제에서 항상 임의 두 집 사이 경로 존재하는 입력만 주어진다고 했으므로 고려하지 않음
# 두 개의 트리로 만들기 위해 가장 유지비 큰 간선을 제거
print(mst_cost - max_included)