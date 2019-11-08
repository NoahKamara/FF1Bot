import os
import pickle



def save(obj):
    with open("team" + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load():
    with open("team" + '.pkl', 'rb') as f:
        return pickle.load(f)