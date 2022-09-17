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
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)


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
position = "None"

with md_pose.Pose(min_detection_confidence=0.5,
                  min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        image1 = cv2.flip(frame, 1)
        image = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

        result = pose.process(image)

        image1.flags.writeable = True

        try:
            landmarks = result.pose_landmarks.landmark

            for i in range(0, len(landmarks)):
                if 11 <= i <= 16:
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

            r_shoulder = [landmarks[12].x,
                          landmarks[12].y]

            r_hip = [landmarks[24].x, landmarks[24].y]
            r_knee = [landmarks[26].x, landmarks[26].y]
            r_ankle = [landmarks[28].x, landmarks[28].y]

            l_hip = [landmarks[23].x, landmarks[23].y]
            l_knee = [landmarks[25].x, landmarks[25].y]
            l_ankle = [landmarks[27].x, landmarks[27].y]

            l_back_angle = detect_angle_3(l_shoulder, l_hip, l_ankle)
            r_back_angle = detect_angle_3(r_shoulder, r_hip, r_ankle)

            left_angle = detect_angle_3(l_shoulder, l_elbow, l_wrist)
            right_angle = detect_angle_3(r_shoulder, r_elbow, r_wrist)

            # show angle on image and make animation for angle detection

            right = "{:.2f}".format(right_angle)
            left = "{:.2f}".format(left_angle)

            cv2.putText(image1, str(left),
                        tuple(np.multiply(l_elbow, [width, height]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2,
                        cv2.LINE_AA)
            cv2.putText(image1, str(right),
                        tuple(np.multiply(r_elbow, [width + 10, height + 10]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2,
                        cv2.LINE_AA)


            left_angle2 = 0
            if left_angle > 90:
                left_angle2 = left_angle - 90
            else:
                left_angle2 = left_angle
            if right_angle > 90:
                right_angle2 = right_angle - 90
            else:
                right_angle2 = right_angle

            cv2.circle(image1,
                       tuple(np.multiply(l_elbow, [width, height]).astype(int)),
                       20, (255, 255, 255), 1)
            cv2.circle(image1,
                       tuple(np.multiply(r_elbow, [width, height]).astype(int)),
                       20, (255, 255, 255), 1)

            cv2.putText(image1, "CHECK HERE",
                        tuple(np.multiply(l_elbow, [width + 10, height + 10]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2,
                        cv2.LINE_AA)


            # cv2.circle(image1,
            #            tuple(np.multiply(l_elbow, [width, height]).astype(int)),
            #            int(20 * (90 - left_angle2) / 90), (255, 255, 255), -1)
            # cv2.circle(image1,
            #            tuple(np.multiply(r_elbow, [width, height]).astype(int)),
            #            int(20 * (90 - right_angle2) / 90), (255, 255, 255), -1)
            cv2.circle(image1,
                       tuple(np.multiply(l_shoulder, [width, height]).astype(int)),
                       20, (255, 255, 255), 1)
            cv2.circle(image1,
                       tuple(np.multiply(r_shoulder, [width, height]).astype(int)),
                       20, (255, 255, 255), 1)
            cv2.circle(image1,
                       tuple(np.multiply(l_wrist, [width, height]).astype(int)),
                       20, (255, 255, 255), 1)
            cv2.circle(image1,
                       tuple(np.multiply(r_wrist, [width, height]).astype(int)),
                       20, (255, 255, 255), 1)

            # Check if back is straight
            # if l_back_angle >= 130:
        # print(left_angle)

            angle = 0
            back = 0
            # if landmarks[14].z > landmarks[13].z:
            #     angle = right_angle
            #     back = r_back_angle
            # else:
            #     angle = left_angle
            #     back = l_back_angle

            if right_angle <= 85 and left_angle <= 85 and position == "Up":
                position = 'Down'

            elif right_angle <= 85 and left_angle <= 85:
                position = "Down"

            elif (right_angle > 130 and left_angle > 130) and position == 'Down':
                position = 'Up'
                counter += 1
                # if l_back_angle < 150 or r_back_angle < 150:
                #     # put text to say that back is not straight
                #     cv2.putText(image, "Back is not straight",
                #                 (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2,
                #                 cv2.LINE_AA)
                print(counter)
            print(f"right: {landmarks[14].z}, left: {landmarks[13].z}, back: {r_back_angle} angle: {right_angle}")


        except:
            pass

        md_drawing.draw_landmarks(image1, result.pose_landmarks,
                                  md_pose.POSE_CONNECTIONS,
                                  md_drawing.DrawingSpec(
                                      color=(245, 117, 66), thickness=2,
                                      circle_radius=2),
                                  md_drawing.DrawingSpec(
                                      color=(245, 66, 230), thickness=2,
                                      circle_radius=2)
                                  )
        if counter >= 0:
            cv2.putText(image1, "Push ups: " + str(counter), (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(image1, "Position: " + position, (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Video", image1)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
