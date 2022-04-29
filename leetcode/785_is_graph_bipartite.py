class Solution:
    def isBipartite(self, adj):
        V = len(adj)
        col = [-1]*(V)
        q = []
        for i in range(V):
            if (col[i] == -1):
                q.append([i, 0])
                col[i] = 0
                while len(q) != 0:
                    p = q[0]
                    q.pop(0)
                    v = p[0]
                    c = p[1]
                    for j in adj[v]:
                        if (col[j] == c):
                            return False
                        if (col[j] == -1):
                            if c == 1:
                                col[j] = 0
                            else:
                                col[j] = 1
                            q.append([j, col[j]])
        return True
 
