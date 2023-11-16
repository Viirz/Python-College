from queue import PriorityQueue

def prim_priority_queue(G, r):
    Q = PriorityQueue()
    key = [float('inf')] * len(G)
    pi = [None] * len(G)
    visited = [False] * len(G)
    key[r] = 0
    Q.put((0, r))
    total = 0

    while not Q.empty():
        _, u = Q.get()

        if visited[u]:
            continue

        visited[u] = True
        total += key[u]

        if pi[u] is not None:
            print(f"Simpul {pi[u]} terhubung ke simpul {u} dengan bobot {key[u]}")

        for v in range(len(G)):
            if G[u][v] != 0 and not visited[v] and G[u][v] < key[v]:
                key[v] = G[u][v]
                pi[v] = u
                Q.put((key[v], v))

    print("Total bobot minimum:", total)
    print(key)
    print(pi)

# Graph 1: 4x4
graph1 = [
    [0, 2, 3, 0],
    [2, 0, 1, 0],
    [3, 1, 0, 4],
    [0, 0, 4, 0]
]

# Graph 2: 5x5
graph2 = [
    [0, 2, 3, 0, 0],
    [2, 0, 1, 4, 0],
    [3, 1, 0, 2, 5],
    [0, 4, 2, 0, 3],
    [0, 0, 5, 3, 0]
]

# Graph 3: 6x6
graph3 = [
    [0, 2, 3, 0, 0, 0],
    [2, 0, 1, 4, 0, 0],
    [3, 1, 0, 2, 5, 0],
    [0, 4, 2, 0, 3, 1],
    [0, 0, 5, 3, 0, 2],
    [0, 0, 0, 1, 2, 0]
]

print("Graph 1")
prim_priority_queue(graph1, int(input("Masukkan simpul awal Graph 1: ")))
print()

prim_priority_queue(graph2, int(input("Masukkan simpul awal Graph 2: ")))
print()

prim_priority_queue(graph3, int(input("Masukkan simpul awal Graph 3: ")))

