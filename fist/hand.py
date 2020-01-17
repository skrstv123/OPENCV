# detects a fist/punch
import cv2 

hc = cv2.CascadeClassifier('fist.xml')

def draw_rect(bw,col):
    hnd_rects = hc.detectMultiScale(bw, 1.3, 5)
    for x,y,w,h in hnd_rects:
        cv2.rectangle(col, (x,y),(x+w,y+h),(0,0,255),4)
        
    return col 

internal_web_cam = cv2.VideoCapture(0)
while 1:
    _unused,clframe = internal_web_cam.read()
    # xx= type(clframe)
    # clframe= clframe[:,::-1]
    bw = cv2.cvtColor(clframe,cv2.COLOR_BGR2GRAY)
    with_rect = draw_rect(bw,clframe)
    cv2.imshow('Video',with_rect)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        # print(xx)
        break
internal_web_cam.release()
cv2.destroyAllWindows()