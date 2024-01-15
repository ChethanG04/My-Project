import cv2
cap = cv2.VideoCapture(0)
if not(cap.isOpened()):
 print("yes")
while(True):
 ret,frame=cap.read()
 cv2.rectangle(frame, (10,15), (50,60),(0,255,0), 1)
 cv2.putText(frame, "hi",(8,18),
 cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1)
 cv2.imshow('preview',frame)
                     
 if cv2.waitKey(1) & 0xFF == ord('q'):
  break
cap.release()
cv2.destroyAllWindows()
                         
