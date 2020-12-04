#/usr/bin/python3.6.x
#encoding:'utf-8'
#License: All Rights Reserved (C) Muneeb Ahmad
import os
import cv2
import pyttsx3
samples = []
to_do = ['Take a Photo in a Normal Condition', 'Put a Finger or Hand covering the Camera Pixel Now']
os.system('pyfiglet ANTI-COVERED')
#Calculates the Sharpness of the Image
def sharpness(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(img, cv2.CV_16S)
    mean, stddev = cv2.meanStdDev(lap)
    return stddev[0,0]
# Get Camera Indexes
def returnCameraIndexes(camera_indexes_to_check=10):
    # checks the first 10 indexes.
    index = 0
    arr = []
    i = camera_indexes_to_check
    while i > 0:
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    return arr
camera_index = returnCameraIndexes(50)
print(camera_index)
print('[+] Select a Value from the Active Cameras in your PC, Select 0 for Default and other number if you want to use an attached usb or other camera')
camerz_inex = input('** Enter the Camera Index >> ')
# Getting the Blurry/Non-Blurry Image Ratings
for element in to_do:

    data = pyttsx3.init()
    data.say(f"{element}")
    data.runAndWait()
    vid = cv2.VideoCapture(int(camerz_inex), cv2.CAP_DSHOW)
    return_value, image = vid.read()
    cv2.imwrite('Open.png', image)
    samples.append(sharpness(image))
    print(f'Sharpness is: {sharpness(image)}')
    vid.release()
# Now Starting the Routine for Processing the Results

sharp_reading = samples[0]
blurry_reading = samples[1]

with open('Camera_Covered_Values.txt', 'w+') as f:
    f.write(f'{sharp_reading},{blurry_reading}')
