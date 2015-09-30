import numpy as np

def load():
    # userid songid user-rating
    with open('ml-100k/u.data') as f:
        data = np.loadtxt(f)
    data = np.delete(data, len(data[0])-1, 1)
    return data

print load()
