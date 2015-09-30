import numpy as np
import parse


def constructRatingMatrix(data, metadata):
    ratingMatrix = np.zeros((metadata['users'], metadata['items']))
    for i in data:
    	ratingMatrix[int(i[0])-1][int(i[1])-1] = i[2] 
    return ratingMatrix

