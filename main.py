import cv2
from simple_face import SimpleFacerec 

# Encode faces
sfr = SimpleFacerec()
sfr.load_encoding_images('images/')


# Load camera
cap = cv2.VideoCapture(0)
cap.set(10, 400);
frameParSeconde = cap.get(cv2.CAP_PROP_FPS);

while True:
    success, frame = cap.read()

    #Detec Faces
    face_locations, face_names = sfr.detect_known_faces(frame)

    for face_loc, name in zip(face_locations,face_names):

        x1, y1, x2, y2= face_loc[3], face_loc[0], face_loc[1], face_loc[2]


        if name == "alpha":
            name = "kawou " + name
        elif name == "mariama":
            name = name + " diolat"
        elif name == "hawa":
            name = name + " lapin"
        elif name == "Diamila":
            name = name + " ndare"
        elif name == "mouhamed":
            name = name + " mbourou"

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255,0), 1)
        

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255,0), 2)  

    cv2.imshow("Capture video", frame)

    key = cv2.waitKey(int(1000/frameParSeconde))

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()