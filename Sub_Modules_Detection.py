import os
import face_recognition
import pyttsx3
import psutil
import random
def Get_Files(path_to_folder):
    extensions = ['.jpg', '.JPG', '.jpeg', '.JPEG','.png', '.PNG']
    good_images = []
    files = os.listdir(path_to_folder)
    for element in files:
        for extension in extensions:
            if extension in element:
                good_images.append(element)
    names = []
    for element in good_images:
        for stuff in extensions:
            if stuff not in element:
                continue
            else:
                meth = element.replace(f'{stuff}', '')
                names.append(meth)
    return names, good_images

def Encoding(image_path):
    image = face_recognition.load_image_file(f"{image_path}")
    encoding = face_recognition.face_encodings(image)[0]
    print(encoding)
    return encoding
def say(text_to_say):
    engine = pyttsx3.init()
    engine.say(f"{text_to_say}")
    engine.runAndWait()
    print("....")
def is_locked():
    for proc in psutil.process_iter():
        if(proc.name() == "LogonUI.exe"):
            return True
mean_stuff = ['Get your face off fool, makes me wanna throw up!', 'Out of all the possibilties my AI has calculated, there is no chance in the universe for you to survive', 'You are a dissappointment, a disgrace.', 'Why am I even doing this', 'Look, whose here blithering Idiot, get ur nasty asian face off']
def mean_stuff_2_say():
    stuff_2_say = random.choice(mean_stuff)
    stuff_2_say = random.choice(mean_stuff)
    return stuff_2_say
