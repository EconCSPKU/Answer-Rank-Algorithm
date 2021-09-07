import numpy as np

def optimal_rank(guessmatrix):
    n, n = guessmatrix.shape
    F = np.zeros(2 ** n)
    Fr = np.zeros(2 ** n, dtype=np.int)
    Log = dict()
    for i in range(n):
        Log.update({2 ** i : i})
    for i in range(2 ** n):
        for j in range(n - 1, -1, -1):
            if (i >> j) & 1 == 1:
                k = i ^ (1 << j)
                tot = F[k] + guessmatrix[j][j]
                while k != 0:
                    tot += guessmatrix[j][Log[k & -k]]
                    k -= k & -k
                if (tot > F[i]) or (Fr[i] == 0) or ((tot == F[i]) and (guessmatrix[j][j] > guessmatrix[Fr[i] - 1][Fr[i] - 1])):
                    F[i] = tot
                    Fr[i] = j + 1
    k = 2 ** n - 1
    order = []
    while k != 0:
        order.append(Fr[k] - 1)
        k = k ^ (1 << Fr[k] - 1)
    return order
