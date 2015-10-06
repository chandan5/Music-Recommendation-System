import numpy as np

def cosine(a, b):
    dp = np.dot(a, b)
    p = a*b
    norm = np.linalg.norm(p/b)*np.linalg.norm(p/a)
    if not norm:
        return 0
    return dp/norm

def cosineMatrix(ratingMatrix, noitems):
    sim = np.zeros((noitems, noitems))
    for i in xrange(noitems):
        for j in xrange(i,noitems):
            sim[i][j] = cosine(ratingMatrix[:, i],ratingMatrix[:, j])
            sim[j][i] = sim[i][j]
    return sim

# need to modify below 2 functions IMPORTANT
def pearsonCosineMatrix(ratingMatrix, noitems):
    sim = np.zeros((noitems, noitems))
    for i in xrange(noitems):
        for j in xrange(i,noitems):
            sim[i][j] = cosine(ratingMatrix[:, i] - np.mean(ratingMatrix[:, i]),
                ratingMatrix[:, j] - np.mean(ratingMatrix[:, j]))
            sim[j][i] = sim[i][j]
    return sim

def adjustedCosineMatrix(ratingMatrix, noitems):
    sim = np.zeros((noitems, noitems))
    for i in xrange(noitems):
        for j in xrange(i,noitems):
            sim[i][j] = cosine(ratingMatrix[:, i] - np.mean(ratingMatrix[:, i]),
                ratingMatrix[:, j] - np.mean(ratingMatrix[:, j]))
            sim[j][i] = sim[i][j]
    return sim
