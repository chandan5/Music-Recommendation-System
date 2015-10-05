import numpy as np

def cosine(a, b):
    return np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))

def cosineMatrix(ratingMatrix, noitems):
    sim = np.zeros((noitems, noitems))
    for i in xrange(noitems):
        for j in xrange(i,noitems):
            sim[i][j] = cosine(ratingMatrix[:,i],ratingMatrix[:,j])
            sim[j][i] = sim[i][j]
    return sim

