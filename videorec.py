import cv2

for i in dir (cv2):
    if 'video' in i or 'Video' in i:
                 print (i)

#starting cam
x=cv2.VideoCapture(0)

width=int(x.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(x.get(cv2.CAP_PROP_FRAME_HEIGHT))

#XVID for .avi,,,deciding format
video_format=cv2.VideoWriter_fourcc(*'XVID')
#saving data
video_output=cv2.VideoWriter('ad.avi',video_format,20.0,(width,height))

for i in dir (cv2):
    if 'width' in i or 'HEIGHT' in i:
                 print (i)

while x.isOpened():
    status,frame=x.read()
    cv2.imshow("hello",frame)
    video_output.write(frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
x.release()
    