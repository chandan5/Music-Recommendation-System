import numpy as np

def cosine(a, b):
    dp = np.dot(a, b)
    p = a*b
    norm = np.linalg.norm(p/b)*np.linalg.norm(p/a)
    if not norm:
        return 0
    return dp/norm

def cosineMatrix(ratingMatrix):
    noitems = np.shape(ratingMatrix)[1]
    sim = np.zeros((noitems, noitems))
    for i in xrange(noitems):
        for j in xrange(i,noitems):
            sim[i][j] = cosine(ratingMatrix[:, i],ratingMatrix[:, j])
            sim[j][i] = sim[i][j]
        print i
    return sim

# need to modify below 2 functions IMPORTANT
def pearsonCosineMatrix(ratingMatrix):
    noitems = np.shape(ratingMatrix)[1]
    sim = np.zeros((noitems, noitems))
    for i in xrange(noitems):
        for j in xrange(i,noitems):
            sim[i][j] = cosine(ratingMatrix[:, i] - np.mean(ratingMatrix[:, i]),
                ratingMatrix[:, j] - np.mean(ratingMatrix[:, j]))
            sim[j][i] = sim[i][j]
    return sim

def adjustedCosineMatrix(ratingMatrix):
    nousers = np.shape(ratingMatrix)[0]
    noitems = np.shape(ratingMatrix)[1]
    sim = np.zeros((noitems, noitems))
    user_avg_rating = np.zeros(nousers)
    import pdb; pdb.set_trace();  
    for u in xrange(nousers):
        for i in xrange(noitems):
            user_avg_rating[u] += ratingMatrix[u, i]
        user_avg_rating[u] /= noitems                
    for i in xrange(noitems):
        for j in xrange(i,noitems):
            sim[i][j] = cosine(ratingMatrix[:, i] - user_avg_rating,
                ratingMatrix[:, j] - user_avg_rating)
            sim[j][i] = sim[i][j]
    return sim
