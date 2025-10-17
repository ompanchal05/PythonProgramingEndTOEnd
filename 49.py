#WAP2 To understand the basic use of OpenCV by capturing and displaying video using a webcam.

# Import OpenCV library
import cv2

# Open the default camera (0 means the first webcam)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Loop to continuously capture frames
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame read is not successful, break
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting ...")
        break

    # Display the resulting frame
    cv2.imshow('Live Video - Press Q to Quit', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
