import cv2

cap = cv2.VideoCapture("Video")  # URL pf RTSP stream, or *.mp4* file
cv2.namedWindow("test")
img_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(7)
    if k % 256 == 26:
        break

    elif k % 256 == 32:
        img_name = "frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        img_counter += 1

cap.release()
cv2.destroyAllWindows()
