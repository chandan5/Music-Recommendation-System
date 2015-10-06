import numpy
import parse
import utils
import similarity_functions as sf

def main():
    training, test, metadata = parse.load(1)
    ratingMatrix = utils.constructRatingMatrix(training, metadata)
    similarity = sf.cosineMatrix(ratingMatrix)
    print "similarity done"
    prediction = utils.predictRating(similarity, ratingMatrix)
    predictionOnTest = prediction[test[:, 0]-1, test[:, 1]-1]
    error = predictionOnTest - test[:, 2]
    print np.abs(error).mean()

if __name__ == '__main__':
    print main()
