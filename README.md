# Project Title: Fitness Tracker Application

## Description:

This project is a fitness-tracking application that leverages computer vision technologies to monitor and count physical exercises, such as push-ups, sit-ups, and squats. Utilizing Python, OpenCV, and MediaPipe, the application processes video input from the user's webcam to detect and analyze movements, ensuring exercises are performed correctly and counts are accurate. It features a graphical user interface built with Pygame, allowing users to select different exercises and view real-time feedback.

## Features:

1. **Real-Time Exercise Detection:** Uses the webcam to detect and track user movements for various exercises.
2. **Multiple Exercise Support:** Capable of recognizing and counting push-ups, sit-ups, and squats.
3. **Graphical User Interface:** Offers a user-friendly GUI for easy interaction, making it simple to select exercises and start tracking.
4. **Live Feedback:** Provides instant visual feedback on the number of repetitions and exercise form directly through the webcam feed.

## Installation

Ensure you have Python 3.8 or later installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies

- OpenCV for computer vision tasks
- MediaPipe for pose estimation
- Pygame for the graphical user interface
- NumPy for numerical operations

Install the required Python packages using the following command:
```bash
pip install opencv-python mediapipe pygame numpy
```

## Setup

Clone this repository or download the source code.

Navigate to the project directory.

(Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```


## Usage

To run the application, execute the `main.py` script from the terminal or command prompt:

```bash
python main.py
```

Use the GUI to select the exercise you wish to track. Position yourself in view of the webcam and start exercising. The application will provide real-time feedback and count your repetitions.


