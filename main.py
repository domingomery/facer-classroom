# the idea of this code is to verify is the subject present in the query image is
# present in the session image.
#
# D. Mery, UC, November, 2018
# http://dmery.ing.puc.cl

import numpy as np
from facer import Facer
from facer import fr_str, num2fixstr, dirfiles, extract_rows, vector_distances, im_crop
from facer import im_concatenate, imshow

# definitions
#IMG-2018 - Course: Image Proccesing at UC, 2018
# img_path_sessions = '/Users/domingomery/Dropbox/Mingo/Matlab/facer/test/img2018/'
img_path_sessions = 'data/sessions/'
id_subjects       = [297, 300, 302, 305, 308, 310, 312, 314, 317, 319, 321, 323, 325, 327, 299, 301, 304, 306, 309, 311, 313, 316, 318, 320, 322, 324, 326]  # id of the query persons for img2018
id_sessions       = range( 1,6)     # id of the sessions
csv_list          = 'student_list.csv'  # ID and names of the students

# img_path_enroll   = '/Users/domingomery/Dropbox/Mingo/Matlab/facer/images/'
img_path_enroll   = 'data/enroll/'
fd_method         = 0               # face detection (0:HOG, 1: CNN)
fr_method         = 2               # face recognition (0: Dlib, 1: Dlib+, 2: FaceNet)
sc_method         = 0               # 0 cosine similarity, 1 euclidean distance
uninorm           = 1               # 1 means descriptor has norm = 1
theta             = 0.45            # threshold for the recognition
print_scr         = 0               # print scores
show_img          = 1               # show images
extract_desc      = [0, 0]          # enrollment, session
img_size          = [80, 60]        # output
echo              = 1               # print out progress comments
session_prefix    = 'LN'            # prefix of the folder that contains the session images
show_fd           = 0               # show face detection


# init
F = Facer()
F.echo           = echo
F.printComment("----------------------------------------------------------------")
F.fd_method      = fd_method
F.fr_method      = fr_method
F.sc_method      = sc_method
F.uninorm        = uninorm
F.theta          = theta
F.show_fd        = show_fd
F.printDefinitions()

# load deep learning model (if any) and define parameters
F.printComment("loading face recognition model " + fr_str[fr_method] + "...")
F.loadModel()
n                  = len(id_subjects) # number of subjects
m                  = len(id_sessions) # number of sessions
image_final        = []
image_session      = []
img_size_f         = [img_size[0]*len(id_subjects),img_size[1]]
F.scores           = np.zeros((n,m))
F.session_prefix   = session_prefix
F.id_subjects      = id_subjects
F.id_sessions      = id_sessions
F.csv_list         = csv_list

# in case the descriptors have not already extracted and saved
# --- extract and save descriptors for enrolled subjects
if extract_desc[0] == 1:
    F.img_path       = img_path_enroll
    F.extractDescriptorsEnrollment()
# --- extract and save descriptors for faces in session images
if extract_desc[1] == 1:
    F.img_path       = img_path_sessions
    F.fd_method      = fd_method
    F.extractDescriptorsSession()

# store in D all descriptors of enrolled subjects
F.extract_desc = 0
F.save_desc    = 0
F.img_path     = img_path_enroll
F.getDescriptorsEnrollment()
D              = F.descriptorsE
ix             = F.ixE # indices

# for all sessions
F.full            = 1
F.fd_method       = fd_method
for j in range(m):
    F.printComment(">>> session "+str(j)+"/"+str(m)+"...")
    img_path_session  = img_path_sessions + F.session_prefix + num2fixstr(id_sessions[j],2) + '/'
    img_names_session = dirfiles(img_path_session,'*.png')
    F.img_path        = img_path_session
    F.img_names       = img_names_session
    F.getDescriptorsImageList()
    Y                 = F.descriptors
    iy                = F.ix
    facesy            = F.bbox

    # for all enrolled images
    for i in range(n):
        X = extract_rows(D,ix,i) # descriptors of subject i
        # computation of scores between enrolled faces and session images
        scr,scr_best,ind_best,face_detected = vector_distances(Y,X.T,sc_method,theta,print_scr)
        F.scores[i][j] = scr_best

        # construction of output image with the recognized faces per subject in each session
        if show_img == 1:
            if face_detected == 1:
                ii     = ind_best[0]
                jj     = iy[ind_best[0]].item()
                image  = im_crop(img_path_session+img_names_session[jj],facesy[ii],0)
            else:
                image  = []
            image_session = im_concatenate(image_session,image,img_size,0)

    if show_img == 1:
        image_final   = im_concatenate(image_final,image_session,img_size_f,1)
        image_session = []

# assistance report
if show_img == 1:
    imshow(image_final)
F.reportAssistance()
