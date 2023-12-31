def prim(G, r):
    Q = list(range(len(G)))
    key = [float('inf')] * len(G)
    pi = [None] * len(G)
    key[r] = 0
    total = 0



    while Q:
        u = min(Q, key=lambda u: key[u])
        Q.remove(u)

        if pi[u] is not None:
            print(f"Simpul {pi[u]} terhubung ke simpul {u} dengan bobot {key[u]}")
            total += key[u]

        for v in range(len(G)): 
            if G[u][v] != 0 and v in Q and G[u][v] < key[v]:
                pi[v] = u
                key[v] = G[u][v]
        
        print()

    print("Total bobot minimum:", total)
    print(key)
    print(pi)

# Graph 1
graph1 = [
    [0, 2, 0, 6, 0, 0, 0, 0, 0, 0],
    [2, 0, 3, 8, 5, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 7, 0, 0, 0, 0, 0],
    [6, 8, 0, 0, 9, 4, 0, 0, 0, 0],
    [0, 5, 7, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 4, 3],
    [0, 0, 0, 0, 0, 0, 6, 4, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 3, 5, 0]
]

# Graph 2
graph2 = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2, 0],
    [0, 0, 7, 0, 9, 14, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6, 0],
    [8, 11, 0, 0, 0, 0, 1, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 6, 7, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Graph 3
graph3 = [
    [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 9, 0, 10, 0],
    [0, 0, 0, 0, 0, 0, 0, 10, 0, 11],
    [0, 0, 0, 0, 0, 0, 0, 0, 11, 0]
]

print("Graph 1")
prim(graph1, 0)