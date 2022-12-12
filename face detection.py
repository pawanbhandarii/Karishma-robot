# Import the necessary packages
import cv2

# Initialize the Pi camera and grab a reference to the raw camera capture
#camera = PiCamera()
camera = cv2.VideoCapture(0)
rawCapture = PiRGBArray(camera)

# Allow the camera to warmup
time.sleep(0.1)

# Capture a frame from the camera
camera.capture(rawCapture, format="bgr")
frame = rawCapture.array

# Convert the frame to grayscale and detect faces in the frame
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = cv2.CascadeClassifier("haarcascade_frontalface_default.xml").detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Loop over the faces and check if the eyes are looking directly at the camera
for (x, y, w, h) in faces:
    # Extract the face ROI and convert it to grayscale
    face_gray = gray[y:y+h, x:x+w]

    # Detect the eyes in the face ROI
    eyes = cv2.CascadeClassifier("haarcascade_eye.xml").detectMultiScale(face_gray)

    # Loop over the eyes and check if they are looking directly at the camera
    for (ex, ey, ew, eh) in eyes:
        # Calculate the eye aspect ratio to determine if the eyes are open
        ear = calculate_ear(ex, ey, ew, eh)

        # Check if the ear is below a certain threshold, indicating the eyes are open and looking directly at the camera
        if ear < EYE_AR_THRESHOLD:
            print("Looking into the camera!")

# Release the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
