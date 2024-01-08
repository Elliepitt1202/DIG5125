# Video Coursework = Object/Face Tracking

#Importing python cv2
import cv2

# First function for face tracking
def initialize_face_tracker():
    # Loads the model for the face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    # Loads the video from the file path in my folder
    cap = cv2.VideoCapture("videos/dance.mp4")
    # Initalising the tracker to track faces
    tracker = cv2.TrackerMIL_create()
    # Read the first frame from the video
    ret, frame = cap.read()
    # Converts the frame to grayscale (not shown)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detects the faces on the frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Selects the first detected face
    if len(faces) > 0:
        x, y, w, h = faces[0]
        face_roi = (x, y, w, h)
        # Tracker then put in the region of the face
        tracker.init(frame, face_roi)
    return cap, tracker


# Second function for face tracking
def process_video(cap, tracker):
    # Enters Infinite loop reading frames
    while True:
        ret, frame = cap.read()
        # If no more frames left it breaks
        if not ret:
            break
        # Updates the tracker with each current frame
        success, face_roi = tracker.update(frame)
        if success:
            x, y, w, h = [int(i) for i in face_roi]
            # If successful draws the tracked face with a red rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Applys Gaussian blur effect over the tracked face
            face = frame[y:y + h, x:x + w]
            face = cv2.GaussianBlur(face, (99, 99), 30)
            frame[y:y + h, x:x + w] = face

        # Displays the processed frame and name of window
        cv2.imshow("OBJECT TRACKING AND BLUR", frame)

        # Closing the video using the letter "q"
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Closing the video
    cap.release()
    cv2.destroyAllWindows()

# Checks Python is run as main program
if __name__ == "__main__":
    video_cap, face_tracker = initialize_face_tracker()
    
    # Main loop processing video
    process_video(video_cap, face_tracker)
