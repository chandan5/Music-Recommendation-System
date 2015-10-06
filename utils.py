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
    for userid in xrange(nousers):
        for item in xrange(noitems):
            if prediction[userid][item]: continue

            # calculate average
            #import pdb; pdb.set_trace();
            s = np.copy(similarity[item])
            # condition when all elements are zero
            s = s/np.sum(s) if np.sum(s) else s
            prediction[userid][item] = np.dot(ratingMatrix[userid], s)
        print userid
    return prediction