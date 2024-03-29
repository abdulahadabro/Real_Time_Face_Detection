#   I have discussed about Face detection, Cascade classifier, and Haar features.
#   Finally how to use pre-trained model to detect human face in real-time.

#1. Imports:
import cv2
import os

#2. Initialize the classifier:

cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)


#3. Apply faceCascade on webcam frames:

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frames = video_capture.read()

    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frames)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#4. Release the capture frames:

        video_capture.release()
        cv2.destroyAllWindows()

# Run the Code

# You will observe the bounding boxes in webcam frames. To stop the webcam capture press “q”.

