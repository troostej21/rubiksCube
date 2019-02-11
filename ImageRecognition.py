from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
import time
from functools import reduce
from statistics import mean


def threshold(imgArray):
    balanceArr = []
    newArr = imgArray

    for eachRow in imgArray:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:3])
            balanceArr.append(avgNum)
    balance = mean(eachPix[:3])

    for eachRow in newArr:
        for eachPix in eachRow:
            if mean(eachPix[:3]) > balance:
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


# i = Image.open("res/images/numbers/0.1.png")
i = Image.open("res/1TestSide.png")
iar = np.array(i)

i2 = Image.open("res/images/numbers/y0.4.png")
iar2 = np.array(i2)

# i3 = Image.open("res/images/numbers/y0.5.png")
i3 = Image.open("res/1TestSide.png")
iar3 = np.array(i3)

i4 = Image.open("res/images/sentdex.png")
iar4 = np.array(i4)

threshold(iar3)

fig = plt.figure()
ax1 = plt.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8, 6), (4, 0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8, 6), (0, 3), rowspan=4, colspan=3)
# ax4 = plt.subplot2grid((8, 6), (4, 3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
# ax4.imshow(iar4)

plt.show()
