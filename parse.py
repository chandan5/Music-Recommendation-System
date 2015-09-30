import numpy as np

metadata = {'users': 0,
            'items': 0,
            'ratings': 0,
            }
def load():
    # userid songid user-rating
    with open('ml-100k/u.data') as f:
        data = np.loadtxt(f)
    data = np.delete(data, len(data[0])-1, 1)
    with open('ml-100k/u.info') as f:
        metafile = np.genfromtxt(f)
    metafile = np.delete(metafile, len(metafile[0])-1, 1)
    metadata['users'] = metafile[0][0]
    metadata['items'] = metafile[1][0]
    metadata['ratings'] = metafile[2][0]
    #import pdb; pdb.set_trace()
    return data, metadata

#print load()


