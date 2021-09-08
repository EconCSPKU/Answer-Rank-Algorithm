import numpy as np

def optimal_rank(M):
    # input answer-guess matrix M
    n, n = M.shape
    opt_uppersum = np.zeros(2 ** n)
    opt_last = np.zeros(2 ** n, dtype=np.int)
    Log = dict()
    for i in range(n):
        Log.update({2 ** i : i})
    # main algorithm
    for i in range(2 ** n):
        # enumerate all subsets in a predetermined order
        opt_uppersum[i] = -1
        for j in range(n - 1, -1, -1):
            # enumerate the first answer in the ranking
            if (i >> j) & 1 == 1:
                k = i ^ (1 << j)
                uppersum = opt_uppersum[k] + M[j][j]
                while k != 0:
                    uppersum += M[j][Log[k & -k]]
                    k -= k & -k
                if (uppersum > opt_uppersum[i]) or ((uppersum == opt_uppersum[i]) and (M[j][j] > M[opt_last[i]][opt_last[i]])):
                    opt_uppersum[i] = uppersum
                    opt_last[i] = j
    k = 2 ** n - 1
    order = []
    while k != 0:
        order.append(opt_last[k])
        k = k ^ (1 << opt_last[k])
    return order
