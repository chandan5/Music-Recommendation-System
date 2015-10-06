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

    for userid in xrange(np.shape(ratingMatrix)[0]):
        for item in xrange(np.shape(ratingMatrix)[1]):
            if prediction[userid][item]: continue

            # calculate average
            import pdb; pdb.set_trace();
            s = np.copy(similarity[item])
            s /= np.linalg.norm(s)
            prediction[userid][item] = np.dot(ratingMatrix[userid], s)

    return prediction