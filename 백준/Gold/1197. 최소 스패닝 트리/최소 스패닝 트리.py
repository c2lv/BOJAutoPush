import sys

input = sys.stdin.readline

v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = list(range(v + 1)) # 초기 상태에서는 모든 노드가 자기 자신이 부모인 상태
rank = [0] * (v + 1) # rank는 트리의 높이를 나타내며, 초기에는 모든 트리가 높이 0인 상태

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
for c, a, b in edges: # 가중치 낮은 순서대로 간선 선택
    if union(a, b):
        mst_cost += c
        used += 1
        if used == v - 1:
            break

print(mst_cost)