# AI Hand Gesture Recognition

An AI-based hand gesture recognition system that uses a webcam to recognize basic hand gestures in real time.
## Project Overview

This project uses a webcam to capture hand movements and recognize different hand gestures using MediaPipe Gesture Recognizer and OpenCV.

The system recognizes the following gestures:

- Open Hand
- Fist
- Thumbs Up
- Victory / Peace

The detected gesture is displayed on the screen in real time.

## Technologies Used

- Python
- OpenCV
- MediaPipe
- MediaPipe Gesture Recognizer

## How It Works

The system follows these steps:

1. The webcam captures the video.
2. OpenCV reads each frame from the webcam.
3. The frame is converted into an appropriate format.
4. MediaPipe Gesture Recognizer detects and recognizes the hand gesture.
5. The recognized gesture name is displayed on the screen.

### Flow

Webcam → Video Frame → MediaPipe Gesture Recognizer → Gesture Detection → Display Result

## Project Features

- Real-time hand gesture recognition
- Webcam-based detection
- Recognizes four basic gestures
- Simple and easy-to-use interface
- Gesture name displayed on the screen
- No custom dataset required
