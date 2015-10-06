import numpy as np

def cosine(a, b):
    norm = np.linalg.norm(a)*np.linalg.norm(b)
    if not norm:
        return 0
    return np.dot(a, b)/norm

def cosineMatrix(ratingMatrix, noitems):
    sim = np.zeros((noitems, noitems))
    for i in xrange(noitems):
        for j in xrange(i,noitems):
            sim[i][j] = cosine(ratingMatrix[:, i],ratingMatrix[:, j])
            sim[j][i] = sim[i][j]
    return sim

def pearsonCosineMatrix(ratingMatrix, noitems):
    sim = np.zeros((noitems, noitems))
    for i in xrange(noitems):
        for j in xrange(i,noitems):
            sim[i][j] = cosine(ratingMatrix[:, i] - np.mean(ratingMatrix[:, i]),
                ratingMatrix[:, j] - np.mean(ratingMatrix[:, j]))
            sim[j][i] = sim[i][j]
    return sim
