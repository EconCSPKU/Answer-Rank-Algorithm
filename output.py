import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import heatmap
import algorithm


def init(allans, guessmatrix, order):
    """
    Rearrange the answer-guess matrix
    """
    n = len(allans)
    newmatrix = np.zeros([n, n])
    newans = []
    for i in range(n):
        newans.append(allans[order[i]])
        for j in range(n):
            newmatrix[i][j] = guessmatrix[order[i]][order[j]]
    return newans, newmatrix

def print_heatmap(filename, id, allans, guessmatrix, ansnum=[], order = None, minmax = None, figsize = (3.5, 3), specialname = None):
    """
    Input the answer-guess matrix, output the figure.

    filename:       the path to save the figure
    id:             the question id
    allans:         the answer list of the question
    guessmatrix:    the answer-guess matrix M
    order:          the rank of the answers. If order == None, use our algorithm to calculate the optimal rank
    """
    if order == None:
        order, ordernorm = algorithm.optimal_rank(guessmatrix, ansnum=ansnum)
        res, resnorm = algorithm.optimal_rank_with_type(guessmatrix, ansnum=ansnum)
        order2 = algorithm.calc_order(res, ansnum)
        # print(resnorm, ordernorm)
        # if order == order2:
        #     return
        order = order2
        ordernorm = resnorm
        specialname = "Question_" + str(id + 1) + "_new"
    newans, newmatrix = init(allans, guessmatrix, order)
    if len(allans) > 10:
        figsize = (9, 8)
    fig, ax = plt.subplots(figsize = figsize)
    if minmax == None:
        minmax = [newmatrix.min(), newmatrix.max()]
    norm = matplotlib.colors.Normalize(minmax[0] + 1, minmax[1] + 1)
    im, cbar = heatmap.heatmap(newmatrix + 1, newans, newans, norm = norm, ax=ax, cmap="Blues", usecbar = False)
    fmt = matplotlib.ticker.FuncFormatter(lambda x, pos: "{:.0f}".format(x - 1))
    texts = heatmap.annotate_heatmap(im, valfmt = fmt, threshold = (sum(minmax) + 1) // 2)
    ax.set_xlabel("Norm = %.6f" % ordernorm)
    fig.tight_layout()
    if specialname == None:
        fig.savefig('output/' + filename + "/Question_" + str(id + 1) + ".png", bbox_inches='tight', dpi = 400)
        fig.savefig('output/' + filename + "/Question_" + str(id + 1) + ".pdf", bbox_inches='tight')
    else:
        fig.savefig('output/' + filename + "/" + specialname + ".png", bbox_inches='tight', dpi = 400)
        fig.savefig('output/' + filename + "/" + specialname + ".pdf", bbox_inches='tight')

def print_csv(filename, id, allans, guessmatrix, ansnum=[]):
    # print([filename, id, allans])
    types, typesnorm = algorithm.optimal_rank_with_type(guessmatrix, normalize="all", ansnum=ansnum)
    order, ordernorm = algorithm.optimal_rank(guessmatrix, ansnum=ansnum)
    # res, normall = algorithm.optimal_rank_with_type(guessmatrix, normalize="all", ansnum=ansnum)
    # print([filename, id, res, normtr, normall])
    return [filename, id, allans, types, algorithm.calc_order(types, ansnum), typesnorm, order, ordernorm]