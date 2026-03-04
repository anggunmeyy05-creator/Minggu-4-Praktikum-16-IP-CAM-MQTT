import paho.mqtt.client as mqtt
subscribe = "masukkan-kata"
def on_message(client, userdata, msg):
    data= str(msg.payload.decode())
    print(data)
    return
client = mqtt.Client()
client.on_message = on_message
server = "mqtt-dashboard.com"
client.connect(server, 1883)
client.subscribe(subscribe)
client.loop_forever()

while True:
    client.loop_start()
    client.loop_stop()

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
