import numpy
import parse
import utils
import similarity_functions as sf

def main():
    data, metadata = parse.load()
    ratingMatrix = utils.constructRatingMatrix(data, metadata)
    return sf.cosineMatrix(ratingMatrix, int(metadata['items']))

if __name__ == '__main__':
    print main()
