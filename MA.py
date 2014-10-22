import numpy as np

dataset = [1,5,7,2,6,7,8,2,2,7,8,3,7,3,7,3,15,6]

def movingaverage(values,window):
    weigths = np.repeat(1.0, window)/window
    #including valid will REQUIRE there to be enough datapoints.
    #for example, if you take out valid, it will start @ point one,
    #not having any prior points, so itll be 1+0+0 = 1 /3 = .3333
    smas = np.convolve(values, weigths, 'valid')
    return smas # as a numpy array

#Will print out a 3MA for our dataset
print movingaverage(dataset,3)
