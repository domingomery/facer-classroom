# facer-classroom
Student attendance system in classrooms: The idea of this code is to verify is the subjects that are enrolled are present in the session images. In this simple example, there are 27 students in 5 sessions. The result is shown in [result.png](https://github.com/domingomery/facer-classroom/blob/master/result.png).

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

# 4. How to run facer-classroom

In a folder called "facer-classroom" copy the following files:
- main.py
- utils.py
- data/enroll
- data/sessions

Run main.py (Expected output: attendance report and face images of each student in every session).

# 5. Comments

- To understand main.py: edit the file and read the comments, all functions are defined in utils.py
- The demo uses FaceNet. If you want to run the demo using dlib see inputs in next section.
- In line 80 of utils.py please include your path for facenet_keras.h5

# 6. Inputs
Check definitions in lines 12-29 of main.py:
- for definition of face detection method see variable fd_method
- for definition of face recognition method see variable fr_method
- for extraction of descriptors of enrolled face images set first element of variable extract_desc
- for extraction of descriptors of session face images set second element of variable extract_desc
- for display result image set variable show_img
- id of subjects are given in student_list.csv
- enrolled images are in data/enroll
- session images are in data/sessions

# 7. Output

`[facer] : ----------------------------------------------------------------`

`[facer] : fd = HOG, fr = FaceNet, sc = CosSim(uninorm=1), th = 0.45`

`[facer] : loading face recognition model FaceNet...`

`[facer] : loading descriptors from data/enroll/000297/FaceNet...`

`:`

`[facer] : >>`session 0/5...`

`:`

`[facer] : assistance report in sessions 1...5`

`297  -                    Name Last_Name_20  :   5/5 = 100.00%`

`:`

`326  -                    Name Last_Name_10  :   4/5 =  80.00%`


![Detection Image](https://github.com/domingomery/facer-classroom/blob/master/result.png)

References:
- Mery, D.; Mackenney, I.; and Villalobos, E. [Student Attendance System in Crowded Classrooms using a Smartphone Camera](http://dmery.sitios.ing.uc.cl/Prints/Conferences/International/2019-WACV.pdf). In 2019 IEEE Winter Conference on Applications of Computer Vision (WACV2017), 2019.

Note: 
The students of these pictures gave their permission to be part of this research. The pictures can be used free of charge, for research and educational purposes only. Redistribution and commercial use is prohibited.




