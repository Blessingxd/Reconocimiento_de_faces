import cv2 

cap=cv2.VideoCapture('video5.mp4')
contador=0
linea1_x=100
linea2_x=500
linea3_x=80
linea4_x=500
personas_previas=[]
velocidad_lenta= 50 
while True:
    ret, frame=cap.read()
    if not ret:
        break
    #---INICIO---
    frame=cv2.resize(frame,(640,480))
    cv2.line(frame, (linea1_x, 200),(linea1_x,20), (0,0,255), 2)
    cv2.line(frame, (linea2_x, 300),(linea2_x,450),(0,0,255), 2)
    cv2.line(frame, (linea3_x, 200),(linea3_x,450),(0,0,255), 2)
    cv2.line(frame, (linea4_x, 190),(linea4_x,10),(0,0,255), 2)
    #---FIN---
    cv2.imshow('Resultados', frame)
    tecla= cv2.waitKey(velocidad_lenta)
    if tecla==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()