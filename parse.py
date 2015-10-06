import numpy as np

def load(fileno, training=True):
    """
    takes the training file no and return training and test data
    Ex. fileno = 1 for u1.base and u1.test
        fileno = 5 for u5.base and u5.test
    """
    # userid songid user-rating
    basedir = "ml-100k/u%s." % (fileno)
    with open(basedir + 'base') as f:
        training = np.loadtxt(f)
    with open(basedir + 'test') as f:
        test = np.loadtxt(f)    
    with open('ml-100k/u.info') as f:
        metafile = np.genfromtxt(f)
    metafile = np.delete(metafile, len(metafile[0])-1, 1)
    metadata = {}
    metadata['users'] = metafile[0][0]
    metadata['items'] = metafile[1][0]
    metadata['ratings'] = metafile[2][0]
    return training[:, :-1], test[:, :-1], metadata
