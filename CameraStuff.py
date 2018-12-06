from SimpleCV import Image, Display, Color, Camera


var = []

# Initialize the camera
cam = Camera()
# Loop to continuously get images
while True:
    # Get Image from camera
    img = cam.getImage()
    img.show()


    #find blobs
    blobs = img.findBlobs()
    blobs.draw()
    img.show()
    # areaAvg = np.mean(blobs.area)
    # areaStd = np.std(blobs.area)

    #find color





