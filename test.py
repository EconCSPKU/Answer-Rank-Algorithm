import matplotlib.pyplot as plt
import matplotlib
import algorithm
import numpy as np

if __name__=="__main__":
    mymat = np.array([[3, 3, 3, 3], [3, 3, 3, 3], [0, 0, 2, 2], [0, 0, 2, 2]])
    print(algorithm.optimal_rank_with_type(mymat))
