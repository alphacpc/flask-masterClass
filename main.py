import cv2
import face_recognition

# Encode faces


# Load camera
cap = cv2.VideoCapture(0)

while True:
    status_frame, frame = cap.read()

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)

    if key == 4:
        break

cap.release()
cv2.destroyAllWindows()