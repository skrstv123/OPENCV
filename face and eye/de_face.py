import cv2 
facc=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyec = cv2.CascadeClassifier('haarcascade_eye.xml')

def draw_rect(bw,col):
    face_rects = facc.detectMultiScale(bw, 1.3, 5)
    for x,y,w,h in face_rects:
        cv2.rectangle(col, (x,y),(x+w,y+h),(0,0,255),4)
        bw_face = bw[y:y+h,x:x+h]
        col_face = col[y:y+h,x:x+h]
        eye_rects = eyec.detectMultiScale(bw_face,1.1,3)
        for a,b,br,le in eye_rects:
            cv2.rectangle(col_face,(a,b),(a+br,b+le),(0,255,0),2)
    return col 

internal_web_cam = cv2.VideoCapture(0)
while 1:
    _unused,clframe = internal_web_cam.read()
    xx= type(clframe)
    bw = cv2.cvtColor(clframe,cv2.COLOR_BGR2GRAY)
    with_rect = draw_rect(bw,clframe)
    cv2.imshow('Video',with_rect)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        print(xx)
        break
internal_web_cam.release()
cv2.destroyAllWindows()