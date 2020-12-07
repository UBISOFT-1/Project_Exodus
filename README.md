# Project_Exodus
Face Detection Safety System for Windows, MacOS and Linux, by Muneeb Khurram.

## Project Intro (Working)

This Project uses the Python 3.6 **face_recognition** library and detects the face infront of the webcam of the computer, if the user is detected as allowed and is in,
the `./Faces` Folder and its name is the Name of the Face or Could be the ID, whatever you prefer it allows and if the added ID is Blocked in the `Banned_Faces.txt` file,
then it locks, the computer and if that person is still infront of the computer then, it says mean words to that person like, `"Out of all the Calculations my AI has done,
you have no chance of surviving in the universe"`. So it is really cool and is *Good for Memes* as well. Further working is being done, and if there is a nice feature or,
a meme u want to add be sure to tell me what it shoud be ;)


## Installation
Installing this is *Straightforward* on Linux and MacOS and Windows, as long as you follow my `instructions`.

### Requirements

- `Python 3.6` [This Version Only, unless u can somehow `install dlib`]
- `pip`
- `dlib`
- `numpy`
- `face_recognition`
- `opencv-python`
- `pyttsx3`
- `psutil`

These are the requirements of installing this on your Windows Machine. In Depth Procedure is given below.

### System Requiremets

*4GB-6GB RAM DDR4* ~ Less will also Do (Hopefully)
*Intel HD 620 Graphics* ~ If u have a GPU, then make sure to install face_recognition with GPU not CPU [PyPI Page](https://pypi.org/project/face-recognition/)
*7th - Infinte Gen*

### Procedure

1. Download and Install [Python 3.6](https://www.python.org/downloads/release/python-360/)
2. When Installing Python 3.6 Select `Add pip to PATH` option.
3. Open cmd or powershell Admin and type `pip install cmake`
4. After that type:

`pip install https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-win_amd64.whl#md5=b7330a5b2d46420343fbed5df69e6a3f`

[Dlib Install Steps See:](https://stackoverflow.com/questions/41912372/dlib-installation-on-windows-10)

This should do the trick and save you from of Install of Visual Studio SDK. No need to say thankyou!
If you are on MacOS and Linux, you will not have this Problem. But if you are bent upon not using Python 3.6
for whatever reason, here are the steps to install dlib on Windows 10, https://medium.com/analytics-vidhya/how-to-install-dlib-library-for-python-in-windows-10-57348ba1117f#:~:text=%20How%20to%20install%20dlib%20library%20for%20Python,environment.%20First%20of%20all%2C%20you%20need...%20More%20 
Again, no need to say that you :)!

5. After that Install [Git](https://git-scm.com/).

6. Type in the terminal `git clone https://github.com/UBISOFT-1/Project_Exodus.git`

7. Then type `cd Project_Exodus` or press open terminal here.

8. Type `pip install -r requirements.txt`

9. Thats all, I hope so ;)

## Usage

*After this you have done all that had to be done to make it run.*

Now, the **FUN** Part.

### Basic Usage
You will see the Faces Folder, open the Folder and add the Faces, you want to add, it will auto detect them when they come in front of the Webcam.
If there is a user that you do not know of, means there is no picture of him in the Faces Folder, it will add its photo onto the Unknown_Access folder, so u can see.

**Most Importantly**, It saves their Face Encodings, Features in the `./Unknown_Access/Face_Encoding.txt` for further refrence and for other tools to process.

### Ban a Person

To *Restrict/Ban* a man from using your device or being infront of the webcam, go to the Banned_People.txt file and add the name of the Picture you saved in the `./Faces` Folder.

**Note**: Name the Pictures with an ID like User_001.jpg or *.JPEG or *.PNG or *.png and make it easy like I added mine as Muneeb Khurram.jpg so it detects me as Muneeb Khurram.

Then just add the First Part of the Image name in the `Banned_People.txt` as Muneeb Khurram for `Muneeb Khurram.jpeg`, hope you get the point.

## Activate the Anti-Cover Feature in your Camera

This is a really big feature in this new version Update 1.0. What is does is that it locks the PC if you are covering your Camera Lens,
Previously, in Project Exodus, if the attacker knew about the Admin Password, he could cover the camera and evade this, but in this version
we have stopped, this, to some extent it can even stop some malware as it keeps on locking. 

### Procedure 

1) Open the Folder of Project Exodus by `cd Project_Exodus`
2) Then, type `python3 camera_adjustment.py`
3) This will now open a Voice Driven Tutorial,
4) First it will ask you which camera are u using, if you have more than one connected camera's

**Note** If you want to use the default camera then press 0 or else select from the numbers provided above.
 
 Then, take a photo in normal condition with your camera, after that take a photo with your lens
 covered. And this should do the trick. :)
 
 **Note** See the Demo Below, Trust me it is easy AF.
   

# DEMO:
https://youtu.be/g5TGesFdI_4
[![Watch the video](https://img.youtube.com/vi/g5TGesFdI_4/maxresdefault.jpg)](https://youtu.be/g5TGesFdI_4)

:)

When you are in the Folder, type `python Face_Detection.py` and thats it ;)

Happy Secure Safe Computer :)
# Connect a IP Webcam

This features works, even over the internet, and if the user enter the room it locks the PC, tested it on a Camera 1000 Km
away from my Home :), Works like a charm. Used HikVision Camera's.

*Note*
Still Working on that Feature :)

# New Features (Upcoming)
- Detect if Camera is being Covered ;) (Almost Complete/Possible)
- Connect IP Webcam (Under Dev/Possible)
- Option to process the image in personal Google Colab of user for seamless experience (Trying/Possible)

https://youtu.be/IzgP8fH1QzY
[Old Video] - [Check the Above Video]
[![Watch the video](https://img.youtube.com/vi/IzgP8fH1QzY/maxresdefault.jpg)](https://youtu.be/IzgP8fH1QzY)

# License
MIT - (C) 2020 Muneeb Ahmad



