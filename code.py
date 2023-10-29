import face_recognition
import cv2
import numpy as np
from datetime import datetime
import pyttsx3 as text
import smtplib

engine = text.init()


# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)


video_capture = cv2.VideoCapture(0)

# # Load a sample picture and learn how to recognize it.
#img008 = face_recognition.load_image_file("Images/1KS19EC008_AMULYA_R.jpg")
#mg_008_encoding = face_recognition.face_encodings(img008)[0]
# print(22)
# # Load a second sample picture and learn how to recognize it.
#img050 = face_recognition.load_image_file("Images/1KS19EC050_Monisha_B_K.jpg")
#img_050_encoding = face_recognition.face_encodings(img050)[0]
# #
# # # Load a third sample picture and learn how to recognize it.
#img051 = face_recognition.load_image_file("Images/1KS19EC051_Anila_D.jpg")
#img_051_encoding = face_recognition.face_encodings(img051)[0]
# #
# # # Load a fourth sample picture and learn how to recognize it.
#img053 = face_recognition.load_image_file("Images/1KS19EC053_Nisarga_K.jpg")
#img_053_encoding = face_recognition.face_encodings(img053)[0]
# #
# # # Load a fifth sample picture and learn how to recognize it.
#img054 = face_recognition.load_image_file("Images/1KS19EC054_Nithin_D.jpg")
#img_054_encoding = face_recognition.face_encodings(img054)[0]
# # print(33)
# # # Load a sixth sample picture and learn how to recognize it.
#img055 = face_recognition.load_image_file("Images/1KS19EC055_Pavan_Kumar_G_R.jpg")
#img_055_encoding = face_recognition.face_encodings(img055)[0]
# #
#Load a seventh sample picture and learn how to recognize it.
#img061 = face_recognition.load_image_file("Images/1KS19EC061_Prashanth_S_K.jpg")
#img_061_encoding = face_recognition.face_encodings(img061)[0]
#
# # # Load a eigth sample picture and learn how to recognize it.
#img064 = face_recognition.load_image_file("Images/1KS19EC064_Priyanka_K.jpg")
#img_064_encoding = face_recognition.face_encodings(img064)[0]

# # # Load a ninth sample picture and learn how to recognize it.
img065 = face_recognition.load_image_file("Images/1KS19EC065_Radhakrishna_L.jpg")
img_065_encoding = face_recognition.face_encodings(img065)[0]
# #
# # # Load a tenth sample picture and learn how to recognize it.
#img066 = face_recognition.load_image_file("Images/1KS19EC066_Rajalakshmi.S.jpg")
#img_066_encoding = face_recognition.face_encodings(img066)[0]
# #
# #
# # # Load a 11th sample picture and learn how to recognize it.
#img069 = face_recognition.load_image_file("Images/1KS19EC069_Rohan_K_R.jpg")
#img_069_encoding = face_recognition.face_encodings(img069)[0]
# #
# # # Load a 12th sample picture and learn how to recognize it.
#img070 = face_recognition.load_image_file("Images/1KS19EC070_Bharatesh.jpg")
#img_070_encoding = face_recognition.face_encodings(img070)[0]
# #
# # # Load a 13th sample picture and learn how to recognize it.
#img078 = face_recognition.load_image_file("Images/1KS19EC078_SHAMITHA.jpg")
#img_078_encoding = face_recognition.face_encodings(img078)[0]
# #
# # # Load a 14th sample picture and learn how to recognize it.
img079 = face_recognition.load_image_file("Images/1KS19EC079_Shashank_Kashyap_H_R.jpg")
img_079_encoding = face_recognition.face_encodings(img079)[0]
# #
# # # Load a 15th sample picture and learn how to recognize it.
img081 = face_recognition.load_image_file("Images/1KS19EC081_Shreyams_D_K.jpg")
img_081_encoding = face_recognition.face_encodings(img081)[0]
# #
# # # Load a 16th sample picture and learn how to recognize it.
#img082 = face_recognition.load_image_file("Images/1KS19EC082_Shreyas_B_Aradhya.jpg")
#img_082_encoding = face_recognition.face_encodings(img082)[0]
# #
# #Load a 17th sample picture and learn how to recognize it.
img083 = face_recognition.load_image_file("Images/1KS19EC083_Shreyas_Gowda.jpg")
img_083_encoding = face_recognition.face_encodings(img083)[0]
# #
# #
# # #Load a 18th sample picture and learn how to recognize it.
#img084 = face_recognition.load_image_file("Images/1KS19EC084_Shreyas_V_Bharadwaj.jpg")
#img_084_encoding = face_recognition.face_encodings(img084)[0]
#
#Load a 19th sample picture and learn how to recognize it.
img085 = face_recognition.load_image_file("Images/1KS19EC085_SHUBHAM.jpg")
img_085_encoding = face_recognition.face_encodings(img085)[0]

##Load a 20th sample picture and learn how to recognize it.
img092 = face_recognition.load_image_file("Images/1KS19EC092_Sumukha_Vasishta_M_R.jpg")
img_092_encoding = face_recognition.face_encodings(img092)[0]


#Load a 22nd sample picture and learn how to recognize it.
#img098 = face_recognition.load_image_file("Images/1KS19EC098_Theerthana_SR.jpg")
#img_098_encoding = face_recognition.face_encodings(img098)[0]
#
#
#



# Create arrays of known face encodings and their names
#known_face_encodings = [img_008_encoding,img_050_encoding,img_051_encoding,img_053_encoding,img_054_encoding,
 #                       img_055_encoding,img_061_encoding,img_064_encoding, img_065_encoding,img_066_encoding,
  #                      img_069_encoding,img_070_encoding,img_078_encoding,img_079_encoding,img_081_encoding,
   #                    img_082_encoding,img_083_encoding,img_084_encoding,img_085_encoding,img_092_encoding,img_098_encoding]
known_face_encodings = [img_065_encoding,img_079_encoding,img_081_encoding,img_083_encoding,img_085_encoding,img_092_encoding]

#known_face_names = [
 #   "AMULYA","MONISHA BK","ANILA","NISARGA K","NITHIN","PAVAN KUMAR","PRASHANTH SK","PRIYANKA K","RADHAKRISHNA L",
  #   "RAJALAKSHMI S","ROHAN KR","BHARATESH SK","SHAMITHA BIJOOR","SHASHANK KASHYAP HR","SHREYAMS DK","SHREAYS B ARADHYA",
   #  "SHREAYS GOWDA","SHREYAS V BHARADWAJ","SHUBHAM KUMAR","SUMUKHA VASISHTA","THEERTHANA SR"]

known_face_names = ["RADHAKRISHNA L","SHASHANK KASHYAP","SHREYAMS DK","SHREYAS GOWDA","SHUBHAM","SUMUKHA VASISHTA"]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

#video_capture = cv2.VideoCapture("http://100.102.57.130:8080/video")

def intruder():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('miniproject101w@gmail.com', 'wdeqibddrbedxzxv')
    server.sendmail('miniproject101w@gmail.com', 'miniproject101w@gmail.com', 'Intruder detected')

    print("mail sent")

def markattendance(name):
    with open('attendance.cs','r+') as f:
        mydatalist = f.readlines()
        namelist = []
        for line in mydatalist:
            entry = line.split(',')
            namelist.append(entry[0])

        if name not in namelist:
            now = datetime.now()
            timestr = now.strftime('%H:%M')
            f.writelines(f'\n{name},{timestr}')
            engine.say("Welcome to Class" + name)
            engine.runAndWait()



while True:
    print(111)
    # Grab a single frame of video
    ret, frame = video_capture.read()

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
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                markattendance(name)
                print("Face recognized as",name)
            else:
                intruder()

            # Or instead, use the known face with the smallest distance to the new face
            #face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
           # best_match_index = np.argmin(face_distances)
           # if matches[best_match_index]:
               # name = known_face_names[best_match_index]
               # markattendance(name)
                #print("Face recognized as",name)
           # else:
               # intruder()

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
