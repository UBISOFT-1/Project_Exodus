import os
import face_recognition
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


