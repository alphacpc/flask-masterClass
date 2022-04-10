import cv2
import face_recognition

img_sadio = cv2.imread('sadio.jpeg')
rgb_img_sadio = cv2.cvtColor(img_sadio, cv2.COLOR_BGR2RGB)
img_encoding_sadio = face_recognition.face_encodings(rgb_img_sadio)[0]

img_wade = cv2.imread('wade.jpg')
rgb_img_wade = cv2.cvtColor(img_wade, cv2.COLOR_BGR2RGB)
img_encoding_wade = face_recognition.face_encodings(rgb_img_wade)[0]

img_thomas = cv2.imread('thomas.jpg')
rgb_img_thomas = cv2.cvtColor(img_thomas, cv2.COLOR_BGR2RGB)
img_encoding_thomas = face_recognition.face_encodings(rgb_img_thomas)[0]

cv2.imshow("Image", img_sadio)
cv2.waitKey(0)