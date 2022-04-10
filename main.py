import cv2
from simple_face import SimpleFacerec 

# Encode faces
sfr = SimpleFacerec()
sfr.load_encoding_images('images/')


# Load camera
cap = cv2.VideoCapture(0)
# cap.set(10, 200);
frameParSeconde = cap.get(cv2.CAP_PROP_FPS);
print(frameParSeconde)

while True:
    success, frame = cap.read()

    #Detec Faces
    face_locations, face_names = sfr.detect_known_faces(frame)

    for face_loc, name in zip(face_locations,face_names):
        y1, x1, y2, x2= face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x2, y2 + 40), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255,0), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255,0), 4)  

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(int(1000/frameParSeconde))

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()