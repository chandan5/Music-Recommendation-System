import numpy as np
import parse
np.set_printoptions(threshold='nan')


def constructRatingMatrix(data, metadata):
    ratingMatrix = np.zeros((metadata['users'], metadata['items']))
    for i in data:
    	ratingMatrix[int(i[0])-1][int(i[1])-1] = i[2] 
    return ratingMatrix

def predictRating(similarity, ratingMatrix):
    prediction = np.copy(ratingMatrix)
    nousers = np.shape(ratingMatrix)[0]
    noitems = np.shape(ratingMatrix)[1]
    for item in xrange(noitems):
        s = np.copy(similarity[item])
        for userid in xrange(nousers):
            if prediction[userid][item]: continue
            p = s*ratingMatrix[userid]
            c = p/ratingMatrix[userid]
            c[np.isnan(c)] = 0
            SUM = np.sum(c)
            prediction[userid][item] = np.dot(ratingMatrix[userid], c)
            prediction[userid][item] = 0 if SUM == 0 else prediction[userid][item]/SUM
        print item
    return prediction