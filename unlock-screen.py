import cv2

cap = cv2.VideoCapture()
cap.open("rtsp://admin:12345678a@192.168.10.13:554/Streaming/channels/202/picture")

while(True):
     # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here

    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
