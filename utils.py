import numpy as np
import parse
data, metadata = parse.load()
def constructRatingMatrix():
    ratingMatrix = np.empty((metadata['users'], metadata['items']))
    ratingMatrix.fill(-1)
    for i in data:
    	ratingMatrix[int(i[0])-1][int(i[1])-1] = i[2] 
    print ratingMatrix
    import pdb
    pdb.set_trace()

constructRatingMatrix()