import cv2
import mediapipe as mp

 # 建立偵測方法 # 建立繪圖方法
mp_face_detection = mp.solutions.face_detection 
mp_drawing = mp.solutions.drawing_utils 



# For webcam input:
Video_Capture = cv2.VideoCapture(0)

# start detected
with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
    
    if not Video_Capture.isOpened():
        print("Cannot open camera")
        exit()

    while Video_Capture.isOpened():
        ret, image = Video_Capture.read()

        if not ret:
          print("Ignoring empty camera frame.")
          # If loading a video, use 'break' instead of 'continue'.
          continue

        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image)

        if results.detections:
          for detection in results.detections:
            mp_drawing.draw_detection(image, detection)

        # Flip the image horizontally for a selfie-view display. 水平翻轉
        # cv2.imshow('detected', cv2.flip(image, 1))
        cv2.imshow('detected', image)

        if cv2.waitKey(1) & 0xFF == 27  or cv2.getWindowProperty('detected', cv2.WND_PROP_VISIBLE) < 1:
          break
Video_Capture.release()
cv2.destroyAllWindows()
