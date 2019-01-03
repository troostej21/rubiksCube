from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
import time
from functools import reduce

i = Image.open('res/testCube.png')  #all[rows[pixels(r g b alph)]]
iArr = np.array(i)
i2 = Image.open('res/testCube2.png')
iArr2 = np.array(i2)
#print(iArr)

plt.imshow(iArr) #comment out after really plotting
plt.show()


def threshold(imageArray):
    balanceArr = []
    newArr = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum  = reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3])
            balanceArr.append(avgNum)
    balance = reduce(lambda x, y: x + y, balanceArr / balanceArr)

    for eachRow in newArr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newArr



'''ax1 = plt.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8, 6), (4, 0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8, 6), (0, 3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8, 6), (4, 3), rowspan=4, colspan=3)
ax5 = plt.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
ax6 = plt.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)



ax1.imshow(iArr)
ax2.imshow(iArr2)
'''




threshold(iArr)

#part 6 is where i diverge




