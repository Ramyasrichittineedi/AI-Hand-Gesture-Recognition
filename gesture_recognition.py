import cv2
import mediapipe as mp
import os

# Model path
model_path = os.path.join(os.path.dirname(__file__), "gesture_recognizer.task")

# MediaPipe setup
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
RunningMode = mp.tasks.vision.RunningMode

# Create recognizer
options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=RunningMode.IMAGE,
    num_hands=1
)

recognizer = GestureRecognizer.create_from_options(options)

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot access webcam")
    exit()

print("Webcam started!")
print("Show your hand...")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Create MediaPipe image
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )

    # Recognize gesture
    result = recognizer.recognize(mp_image)

    gesture_name = "No Gesture"

    if result.gestures:
        gesture_name = result.gestures[0][0].category_name

        # Change names for our project
        if gesture_name == "Open_Palm":
            gesture_name = "Open Hand"
        elif gesture_name == "Closed_Fist":
            gesture_name = "Fist"
        elif gesture_name == "Thumb_Up":
            gesture_name = "Thumbs Up"
        elif gesture_name == "Victory":
            gesture_name = "Victory / Peace"

    # Display gesture
    cv2.putText(
    frame,
    gesture_name,
    (30, 60),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.2,
    (255, 0, 0),
    3
)

    cv2.imshow("AI Hand Gesture Recognition", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
recognizer.close()
cv2.destroyAllWindows()