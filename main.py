import cv2
import os

# Read the video from specified path
vid = cv2.VideoCapture("E:/Github/Framerizacao_de_Videos/Videos/4.mp4")
interval = 50
i = 0
try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while (True):

    # reading from frame
    success, frame = vid.read()

    if success:
        if i == 0:
            # continue creating images until video remains
            name = './data/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
    else:
        break

    i += 1
    if i == interval:
        i = 0

# Release all space and windows once done
vid.release()
cv2.destroyAllWindows()