import matplotlib.pyplot as plt
import matplotlib
import algorithm
import numpy as np

if __name__=="__main__":
    mymat = np.array([[ 3.,  0.,  1.,  0.],[ 1.,  3.,  2.,  0.],[ 2.,  6., 10.,  3.],[ 2.,  7., 24., 27.]])
    print(algorithm.optimal_rank_with_type(mymat, ansnum=[ 4.,  6., 20., 44.]))
