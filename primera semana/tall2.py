import cv2 
from ultralytics import YOLO 

model= YOLO('yolov8n.pt')
cap=cv2.VideoCapture('video4.mp4')
contador=0
linea_x=340
personas_previas=[]
velocidad_lenta= 50 
while True:
    ret, frame=cap.read()
    if not ret:
        break
    #---INICIO---
    frame=cv2.resize(frame,(640,480))
    resultados= model(frame,conf=0.5 , verbose=False)
    cv2.line(frame, (linea_x, 0),(linea_x,frame.shape[0]),(0,0,255), 2)
    #---FIN---
    cv2.imshow('Resultados', frame)
    tecla= cv2.waitKey(velocidad_lenta)
    if tecla==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()