import cv2
cap = cv2.VideoCapture("http://172.20.10.2:8080/video")

while True:
    ret, frame = cap.read()
    cv2.imshow('IP Cam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import cv2
import mediapipe as mp
import paho.mqtt.client as mqtt
mqttbroker = "mqtt-dashboard.com"
client = mqtt.Client()
client.connect(mqttbroker)
kirim = "tangan"

cap= cv2.VideoCapture(0)
mphand= mp.solutions.hands
hands= mphand.Hands()

while True:
    success, frame = cap.read()
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        print("ada tangan")
    else:
        client.publish(kirim, "ada tangan")
        print("tidak ada tangan")

    cv2.imshow("Kamera",frame)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()