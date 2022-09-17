import cv2
import mediapipe as md
import numpy as np

md_drawing = md.solutions.drawing_utils
md_drawing_style = md.solutions.drawing_styles
md_pose = md.solutions.pose

count = 0

position = None

cap = cv2.VideoCapture(0)
# find camera frame dimensions
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


def detect_angle_3(p1: list, p2: list, p3: list):
    # return angle between p1[x, y] p2 and p3 in degrees within 180 degrees
    radians = np.arctan2(p3[1] - p2[1], p3[0] - p2[0]) - np.arctan2(
        p1[1] - p2[1],
        p1[0] - p2[0])

    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle


counter = 0
position = "Up"

with md_pose.Pose(min_detection_confidence=0.5,
                  min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        result = pose.process(image)
        image.flags.writeable = True

        try:
            landmarks = result.pose_landmarks.landmark

            for i in range(0, len(landmarks)):
                if 11 <= i <= 16 or 23 <= i <= 30:
                    if landmarks[i].visibility <= 0.01:
                        for j in range(0, len(landmarks)):
                            landmarks[j].x = 0
                            landmarks[j].y = 0
                            landmarks[j].visibility = 0


                    pass

                else:
                    landmarks[i].visibility = 0




            l_shoulder = [landmarks[11].x,
                          landmarks[11].y]
            l_elbow = [landmarks[13].x,
                       landmarks[13].y]
            l_wrist = [landmarks[15].x,
                       landmarks[15].y]

            r_shoulder = [landmarks[12].x,
                          landmarks[12].y]
            r_elbow = [landmarks[14].x,
                       landmarks[14].y]
            r_wrist = [landmarks[16].x,
                       landmarks[16].y]



            r_hip = [landmarks[24].x, landmarks[24].y]
            r_knee = [landmarks[26].x, landmarks[26].y]
            r_ankle = [landmarks[28].x, landmarks[28].y]

            l_hip = [landmarks[23].x, landmarks[23].y]
            l_knee = [landmarks[25].x, landmarks[25].y]
            l_ankle = [landmarks[27].x, landmarks[27].y]

            l_back_angle = detect_angle_3(l_shoulder, l_hip, l_ankle)
            r_back_angle = detect_angle_3(r_shoulder, r_hip, r_ankle)

            # show angle on image and make animation for angle detection

            right = "{:.2f}".format(r_back_angle)
            left = "{:.2f}".format(l_back_angle)

            cv2.putText(image, str(left),
                        tuple(np.multiply(l_elbow, [1280, 750]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2,
                        cv2.LINE_AA)
            cv2.putText(image, str(right),
                        tuple(np.multiply(r_elbow, [1280, 690]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2,
                        cv2.LINE_AA)




        except:
            pass

        md_drawing.draw_landmarks(image, result.pose_landmarks,
                                  md_pose.POSE_CONNECTIONS,
                                  md_drawing.DrawingSpec(
                                      color=(245, 117, 66), thickness=2,
                                      circle_radius=2),
                                  md_drawing.DrawingSpec(
                                      color=(245, 66, 230), thickness=2,
                                      circle_radius=2)
                                  )
        # count number of push ups and position
        if counter >= 0:
            cv2.putText(image, "Push ups: " + str(counter), (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(image, "Position: " + position, (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Video", image)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

        if key == ord("s"):
            import main
            main.main()
            cap.release()
            cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()
