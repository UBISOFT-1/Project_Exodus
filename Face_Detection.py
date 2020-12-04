import face_recognition
import cv2
import numpy as np
from Sub_Modules_Detection import *
import secrets
import datetime
import os
import ctypes
import pyttsx3
import random
import pickle
# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.
# Mean Stuff 2 Say
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Create arrays of known face encodings and their names
# Encodings go here
known_face_encodings = []
# Face Names go Here

names, path = Get_Files('./Faces')
known_face_names = names
for element in path:
    try:
        encoding = Encoding(f'./Faces/{element}')
        known_face_encodings.append(encoding)
    except:
        continue
print(known_face_names)
print(known_face_encodings)
def sharpness(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(img, cv2.CV_16S)
    mean, stddev = cv2.meanStdDev(lap)
    return stddev[0,0]
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
all_unknown_encodings = []
while True:
    # Grab a single frame of video
    # Just Ignore this Line :) rtsp://admin:12345678a@192.168.10.13:554/Streaming/channels/101/
    #video_capture.open('')

    ret, frame = video_capture.read()
    with open('./Camera_Covered_Values.txt', 'r+') as corrupt:
        data = corrupt.read()
        correct_data = data.split(',')
        covered = correct_data[1]
    if int(sharpness(frame)) <= float(covered):
        ctypes.windll.user32.LockWorkStation()
        say('Locked u Bitch, Try Covering ur screen now')

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        if 'Unknown' in face_names:
            print('Unknown User Detected')
            password = secrets.token_urlsafe(32)
            cv2.imwrite(f'./Unknown_Access/Faces/unknown_person{password}.jpg', frame)
            try:
                # Making a face_encoding of the unknown_person in view of the camera
                encoding_unknown = Encoding(f'./Unknown_Access/Faces/unknown_person{password}.jpg')
                all_unknown_encodings.append(encoding_unknown)
                # Adding Encodings to the Simple .txt File
                f = open('./Unknown_Access/Face_Encodings.txt', 'a')
                f.write(f'{encoding_unknown} sep {password} sep [Type Name Here] \n')
                f.close()
            except:
                print("Failed to Encode - ;)")
            f = open('./Unknown_Access/Face_Encodings.txt', 'r')
            data = f.read().split('\n')
            f.close()

            # Adding Encoding() to the pickle file for further re-processing. Make sure this Folder is not Tampered with Especially this File
            # Could be Tampered with to exec() malicious code in the memory. See: https://intoli.com/blog/dangerous-pickles/
            f = open('dataset_faces.dat', 'a+')
            f.close()
            with open('dataset_faces.dat', 'ab') as f:
                pickle.dump(all_unknown_encodings, f)
        else:
            f = open('User_Access_Log_Name.txt', 'a+')
            for element in face_names:
                f.write(f'{element} - {datetime.datetime.now()}\n')
            f.close()
            f = open('User_Access_Log_Time.txt', 'a+')
            f.write(f'{datetime.datetime.now()}\n')
            f.close()
        f = open('Banned_People.txt', 'r+')
        data = f.read()
        data = data.split('\n')
        print(data)
        f.close()
        for element_banned in data:
            for element_names in face_names:
                if element_names in element_banned:
                    user32 = ctypes.windll.User32
                    if is_locked() == True:
                        print(face_names)
                        if face_names == []:
                            print("No Faces in the image ;)")
                        else:
                            stuff = mean_stuff_2_say()
                            say(stuff)
                    else:
                        say(f"Computer is gonna be locked, You are not Verified, You are Banned {element_names} .....")
                        ctypes.windll.user32.LockWorkStation()

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Face Detection Algorithm (C) 2020 Muneeb Ahmad - {PK-TR}', frame)

    # Hit 'q' on the keyboard to quit! -- Remove this Line 2 make it impossible to quit ;)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
