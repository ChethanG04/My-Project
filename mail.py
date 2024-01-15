import cv2
import imghdr
from email.message import EmailMessage
import smtplib
from imutils.video import VideoStream

def cap_send():
 vs = VideoStream(src=0).start()
 frame = vs.read()
 print("Captured")
 cv2.imwrite("captured.jpg",frame)
 
 # Captured images will be sent from this Email
 Sender_Email = "lgroup788@gmail.com"

 # set the Email ID recieve the captured images
 Reciever_Email = "chethan.g.8431@gmail.com"
 Password = "xxwmysjkhpceaykn"
 newMessage = EmailMessage()
 newMessage['Subject'] = "Unknown person"
 newMessage['From'] = Sender_Email
 newMessage['To'] = Reciever_Email
 newMessage.set_content('unknown person deteced')
 with open('captured.jpg','rb') as f:
  image_data = f.read( )
  image_type = imghdr.what(f.name)
  image_name = f.name
 newMessage.add_attachment(image_data,maintype='image',subtype=image_type,filename=image_name)
 with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
  smtp.login(Sender_Email,Password)
  smtp.send_message(newMessage)
 print("mail Sent")
 vs.stop()

cap_send()
