from collections import deque

def get_path_bfs(edges, visited, V1, V2):
    if V1 == V2:
        ans = [V1]
        visited[V1] = True
        return ans

    q = deque()
    h = {}
    ans = []
    q.append(V1)
    visited[V1] = True

    while q:
        first = q.popleft()
        for i in range(len(edges)):
            if edges[first][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)
                h[i] = first
                if i == V2:
                    ans.append(i)
                    while V1 not in ans:
                        b = h[i]
                        ans.append(b)
                        i = b
                    return ans
    return None


def main():
    V, E = map(int, input().split())
    edges = [[0] * V for _ in range(V)]

    for _ in range(E):
        sv, ev = map(int, input().split())
        edges[sv][ev] = 1        
        edges[ev][sv] = 1

    V1, V2 = map(int, input().split())
    visited = [False] * V
    ans = get_path_bfs(edges, visited, V1, V2)
    
    if ans is not None:
        print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()