from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
import time

i = Image.open('res/testCube.png')  #all[rows[pixels(r g b alph)]]
iArr = np.asarray(i)
print(iArr)

plt.imshow(iArr)
plt.show()


def threshold(imageArray):
    balanceArr = []


#part 6 is where i diverge




