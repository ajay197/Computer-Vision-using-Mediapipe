from cvzone.PoseModule import PoseDetector
import cv2

cap = cv2.VideoCapture("C:/Users/crazyguy/Downloads/Video/workout.mp4")
#cap = cv2.VideoCapture(1)
detector = PoseDetector()

#save output file
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)
result = cv2.VideoWriter('C:/Users/crazyguy/Downloads/Video/filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 40, size)

while True:
    _, img = cap.read()
    img = detector.findPose(img)
    lmList, bbox = detector.findPosition(img, bboxWithHands=False)
    if bbox:
        center = bbox["center"]
        cv2.circle(img, center, 5, (255, 255, 0), cv2.FILLED)

    cv2.imshow("Output", img)
    result.write(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
result.release()
cv2.destroyAllWindows()