import cv2
import cvzone
from cvzone.FaceDetectionModule import FaceDetector

#cap = cv2.VideoCapture("C:/Users/crazyguy/Downloads/Video/test_video1.mp4")
cap = cv2.VideoCapture(0)
detector =FaceDetector()
fpsReader = cvzone.FPS()
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)
result = cv2.VideoWriter('C:/Users/crazyguy/Downloads/filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 40, size)

while True:
    _, img = cap.read()
    img, bboxs = detector.findFaces(img)
    fps, img = fpsReader.update(img, pos=(50, 80), color=(0, 255, 0), scale=2, thickness=2)

    if bboxs:
        center = bboxs[0]["center"]
        cv2.circle(img, center, 5, (255,0,255), cv2.FILLED)
    result.write(img)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
result.release()
cv2.destroyAllWindows()