import numpy as np
import math

def cosine(a, b):
    cosine_ret = 0
    a_norm_special = 0
    b_norm_special = 0
    length = (a.shape)[0]
    for i in xrange(length):
        if(a[i] != 0 and b[i] !=0):
            cosine_ret += a[i]*b[i]
            a_norm_special += a[i]*a[i]
            b_norm_special += b[i]*b[i]
    if(a_norm_special != 0 and b_norm_special != 0):
        a_norm_special = math.sqrt(a_norm_special)
        b_norm_special = math.sqrt(b_norm_special)
        cosine_ret /= a_norm_special
        cosine_ret /= b_norm_special
    return cosine_ret
    #import pdb; pdb.set_trace()        
    #return np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))

def cosineMatrix(ratingMatrix, noitems):
    sim = np.zeros((noitems, noitems))
    for i in xrange(noitems):
        for j in xrange(i,noitems):
            sim[i][j] = cosine(ratingMatrix[:, i],ratingMatrix[:, j])
            sim[j][i] = sim[i][j]
        print i
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