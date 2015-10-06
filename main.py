import numpy
import parse
import utils
import similarity_functions as sf

def main():
    training, test, metadata = parse.load(1)
    ratingMatrix = utils.constructRatingMatrix(training, metadata)
    similarity = sf.cosineMatrix(ratingMatrix, int(metadata['items']))
    return utils.predictRating(similarity, ratingMatrix)

if __name__ == '__main__':
    print main()
