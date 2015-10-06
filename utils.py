import numpy as np
import parse


def constructRatingMatrix(data, metadata):
    ratingMatrix = np.zeros((metadata['users'], metadata['items']))
    for i in data:
    	ratingMatrix[int(i[0])-1][int(i[1])-1] = i[2] 
    return ratingMatrix

def predictRating(similarity, ratingMatrix):
    prediction = np.copy(ratingMatrix)

    for userid in xrange(np.shape(ratingMatrix)[0]):
        for item in xrange(np.shape(ratingMatrix)[1]):
            if prediction[userid][item]: continue

            # calculate average
            s = np.copy(similarity[item])
            # condition when all elements are zero
            s = s/np.sum(s) if np.sum(s) else s
            prediction[userid][item] = np.dot(ratingMatrix[userid], s)
    return prediction
