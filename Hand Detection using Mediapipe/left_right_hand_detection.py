import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

#cap = cv2.VideoCapture("C:/Users/crazyguy/Downloads/Video/test_video1.mp4")
cap = cv2.VideoCapture(0)
detector =HandDetector(detectionCon=0.8, maxHands=2)

#save output file
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)
result = cv2.VideoWriter('C:/Users/crazyguy/Downloads/Video/filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 40, size)

while True:
    _, img = cap.read()
    hands, img = detector.findHands(img)
    result.write(img)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
result.release()
cv2.destroyAllWindows()