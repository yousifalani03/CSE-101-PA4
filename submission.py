import heapq
import math
import copy
from copy import deepcopy
import numpy as np

## Name:Yousif Alani
## PID: 18562674

#######################################################
##############       QUESTION 1 HERE   ################
#######################################################

def myFloyd(M):
    # make a working copy (don’t mutate caller’s matrix)
    n = len(M)

    dist_now = [[M[i][j] for j in range(n)] for i in range(n)]

    for z in range(n):
        dist_now[z][z] = 0  # just to be safe if caller didn’t

    snapshots = []

    # classic triple loop; take a snapshot after each k-phase
    for k in range(n):
        for i in range(n):
            # small local alias saves a couple lookups; "human-ish" micro-opt
            dik = dist_now[i][k]
            if dik is math.inf:  # small guard, avoids pointless inner loop when unreachable
                continue
            
            for j in range(n):
                alt = dik + dist_now[k][j]
                if alt < dist_now[i][j]:
                    dist_now[i][j] = alt
        # store a deep-ish copy (row slices are fine here)
        snapshots.append([row[:] for row in dist_now])


    return snapshots


#########################################################
##############       QUESTION 2 HERE   ##################
#########################################################
def myDijkstra(vertices, edges):
    n = len(vertices)
    # build tiny adjacency list

    neighbor_sack = [[] for _ in range(n)]

    for i, j, w in edges:
        neighbor_sack[i].append((j, w))

    # init

    long_dist = [math.inf] * n
    long_dist[0] = 0
    came_from = [-1] * n
    stamped = [False] * n  # visited-ish

    # simple O(n^2) pick-min loop (readable, no heap)
    for _ in range(n):
        u = -1
        best_so_far = math.inf

        for v in range(n):
            if not stamped[v] and long_dist[v] < best_so_far:
                best_so_far = long_dist[v]
                u = v
        if u == -1:
            break  # nothing left that’s reachable

        stamped[u] = True
        # relax out-edges

        for nxt, wt in neighbor_sack[u]:
            if stamped[nxt]:
                continue
            trial = long_dist[u] + wt
            if trial < long_dist[nxt]:
                long_dist[nxt] = trial
                came_from[nxt] = u

    # rebuild paths from parents
    all_paths = []
    for t in range(n):
        if long_dist[t] is math.inf:
            all_paths.append([])  # shouldn’t happen per spec, but fine
            continue
        
        track = []
        cur = t
        while cur != -1:
            track.append(cur)
            cur = came_from[cur]
        track.reverse()
        # ensure source-alone path is [0], not empty
        all_paths.append(track)


    return (all_paths, long_dist)

#########################################################
##############       QUESTION 3 HERE   ##################
#########################################################
def myMSTTSP(distance_matrix):
    # Prim’s MST, then preorder walk (DFS) to get a 2-approx tour

    N = len(distance_matrix)
    in_tree = [False] * N
    keyish = [math.inf] * N
    parent = [-1] * N
    keyish[0] = 0

    for _ in range(N):
        # pick the lightest fringe node
        grab = -1
        best = math.inf

        for v in range(N):
            if not in_tree[v] and keyish[v] < best:
                best = keyish[v]
                grab = v
        if grab == -1:
            break
        in_tree[grab] = True

        # update neighbors (complete graph implied by distance_matrix)
        for w in range(N):
            wt = distance_matrix[grab][w]
            if not in_tree[w] and wt < keyish[w]:
                keyish[w] = wt
                parent[w] = grab

    # build MST adjacency (undirected)
    twigs = [[] for _ in range(N)]
    for v in range(1, N):
        p = parent[v]
        if p != -1:
            twigs[p].append(v)
            twigs[v].append(p)


    # preorder walk from 0
    visit_mark = [False] * N
    order = []

    def wander(u):
        visit_mark[u] = True
        order.append(u)
        # small deterministic flavor: visit children in ascending order
        for w in sorted(twigs[u]):
            if not visit_mark[w]:
                wander(w)


    wander(0)

    # complete the cycle by returning to 0 (matches the example)
    tour = order + [0]

    # compute total distance
    total = 0

    for i in range(len(tour) - 1):
        a, b = tour[i], tour[i + 1]
        total += distance_matrix[a][b]


    return (tour, total)