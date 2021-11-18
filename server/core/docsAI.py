"""
This AI help your for your write
"""
from torchtext.legacy import data, datasets
import numpy as np 

# calculate similarity
def cos_sim(v1, v2):
    dot_prod = np.dot(v1, v2)
    norm = (np.sqrt(sum(np.square(v1)))*np.sqrt(sum(np.square(v2))))
    sim = dot_prod / norm
    return sim

