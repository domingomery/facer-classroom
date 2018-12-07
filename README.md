# facer-classroom
`Student attendance system in classrooms'

`[facer] : ----------------------------------------------------------------`

`[facer] : fd = HOG, fr = FaceNet, sc = CosSim(uninorm=1), th = 0.45`

`[facer] : loading face recognition model FaceNet...`

`[facer] : loading descriptors from data/enroll/000297/FaceNet...`

`[facer] : loading descriptors from data/enroll/000300/FaceNet...`

`[facer] : loading descriptors from data/enroll/000302/FaceNet...`

`:`

`[facer] : loading descriptors from data/enroll/000326/FaceNet...`

`[facer] : >>`session 0/5...`

`[facer] : >>`session 1/5...`

`[facer] : >>`session 2/5...`

`[facer] : >>`session 3/5...`

`[facer] : >>`session 4/5...`

`[facer] : assistance report in sessions 1...5`

`297  -                    Name Last_Name_20  :   5/5 = 100.00%`

`300  -                    Name Last_Name_21  :   5/5 = 100.00%`

`302  -                    Name Last_Name_13  :   5/5 = 100.00%`

`305  -                    Name Last_Name_15  :   5/5 = 100.00%`

`308  -                    Name Last_Name_19  :   5/5 = 100.00%`

`310  -                    Name Last_Name_08  :   2/5 =  40.00%`

`312  -                    Name Last_Name_22  :   5/5 = 100.00%`

`314  -                    Name Last_Name_07  :   5/5 = 100.00%`

`317  -                    Name Last_Name_26  :   5/5 = 100.00%`

`319  -                    Name Last_Name_11  :   5/5 = 100.00%`

`321  -                    Name Last_Name_12  :   5/5 = 100.00%`

`323  -                    Name Last_Name_17  :   5/5 = 100.00%`

`325  -                    Name Last_Name_27  :   5/5 = 100.00%`

`327  -                    Name Last_Name_09  :   2/5 =  40.00%`

`299  -                    Name Last_Name_25  :   5/5 = 100.00%`

`301  -                    Name Last_Name_05  :   4/5 =  80.00%`

`304  -                    Name Last_Name_04  :   5/5 = 100.00%`

`306  -                    Name Last_Name_24  :   5/5 = 100.00%`

`309  -                    Name Last_Name_01  :   5/5 = 100.00%`

`311  -                    Name Last_Name_16  :   5/5 = 100.00%`

`313  -                    Name Last_Name_23  :   5/5 = 100.00%`

`316  -                    Name Last_Name_18  :   5/5 = 100.00%`

`318  -                    Name Last_Name_02  :   5/5 = 100.00%`

`320  -                    Name Last_Name_03  :   5/5 = 100.00%`

`322  -                    Name Last_Name_14  :   5/5 = 100.00%`

`324  -                    Name Last_Name_06  :   5/5 = 100.00%`

`326  -                    Name Last_Name_10  :   4/5 =  80.00%`



# facer_simple
Simple face recognition in a picture with many persons. The idea of this code is to verify is the subject present in the query image is present in the session image. In this simple example, the query image is Query_6.png and the session image is Session_3.png. The result is shown in detection.png.

# 1. What to install before
- Install Homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
- Re-install boost-python:
brew reinstall boost-python --with-python3 --without-python

# 2. Updates and other installing
- pip3 install --upgrade pip
- pip3 install cmake
- cd dlib
- python3 setup.py install
- pip3 install face_recognition
- pip3 install scikit-image
- pip3 install opencv-python
- pip3 install keras
- pip3 install tensorflow

# 3. Install Dlib & FaceNet in Python folder

- git clone https://github.com/davisking/dlib.git
- git clone https://github.com/ageitgey/face_recognition
- git clone https://github.com/nyoki-mtl/keras-facenet
- in folder keras-facenet/model create keras
- in folder keras-facenet/model/keras copy this model
https://www.dropbox.com/s/o65ow1cl3lcwd1o/facenet_keras.h5?dl=0

# 4. How to run facer_simple

In a folder called "facer" copy the following files:
- main.py
- utils.py
- Query_6.png
- Session_3.png

Run main.py (Expected output: query image is detected in session image).

# 5. Comments

- To understand main.py: edit the file and read the comments, all functions are defined in utils.py
- The demo uses dlib. If you want to run the demo using FaceNet:
1) edit main.py and uncomment line 17
from keras.models import load_model
2) in line 32 put the path of model facenet_keras.h5
3) edit main.py, in line 14 set fr_method   = 2
4) run main.py  


# 6. Inputs
- Query Image: Query_6.png

![Query Image: Query_6.png](https://github.com/domingomery/facer_simple/blob/master/Query_6.png)

- Session Image: Session_3.png
![Session Image: Session_3.png](https://github.com/domingomery/facer_simple/blob/master/Session_3.png)

# 7. Output
- Is the person in the Query Image present in the Session Image?

`[facer] : ----------------------------------------------------------------`

`[facer] : fd = HOG, fr = Dlib+, sc = CosSim(uninorm=1), th = 0.6`

`[facer] : loading face recognition model...`

`[facer] : reading query image Query_6.png...`

`[facer] : detecting faces in session image Session_3.png...`

`[facer] : 13 face(s) found in session image Session_3.png`

`[facer] : finding Query_6.png in session image ...`

`[facer] : scores `

`[0.84946395 0.90679934 0.87062143 0.86717102 0.87782153 0.87154528`

` 0.95557544 0.89859898 0.90368649 0.86654181 0.84295712 0.84654535`

` 0.8821119 ]`

`[facer] : face #6 was detected with score = 0.9555754407241641`

![Detection Image](https://github.com/domingomery/facer_simple/blob/master/detection.png)

References:
- Mery, D.; Mackenney, I.; and Villalobos, E. [Student Attendance System in Crowded Classrooms using a Smartphone Camera](http://dmery.sitios.ing.uc.cl/Prints/Conferences/International/2019-WACV.pdf). In 2019 IEEE Winter Conference on Applications of Computer Vision (WACV2017), 2019.

Note: 
The students of these pictures gave their permission to be part of this research. The pictures can be used free of charge, for research and educational purposes only. Redistribution and commercial use is prohibited.




