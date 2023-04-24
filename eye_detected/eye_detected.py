import numpy as np
import cv2
import os

video_capture = cv2.VideoCapture(0)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') # 載入人臉模型

# faces = face_cascade.detectMultiScale(gray)  # 偵測人臉

if not video_capture.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Cannot receive frame")
        break
        
    frame = cv2.resize(frame,(640,480))              # 縮小尺寸，避免尺寸過大導致效能不好
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # 將鏡頭影像轉換成灰階
    faces = eye_cascade.detectMultiScale(gray)      # 偵測人臉

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)   # 標記人臉
    cv2.imshow('detected', frame)
    if cv2.waitKey(1) == 27 or cv2.getWindowProperty('detected', cv2.WND_PROP_VISIBLE) < 1:
        break

video_capture.release()
cv2.destroyAllWindows()
