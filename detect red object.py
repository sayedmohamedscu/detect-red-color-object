import cv2
import numpy as np

cap = cv2.VideoCapture(1)


while(1):

    _, frame = cap.read()
    
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 50, 70])
    
    upper_red = np.array([10, 255, 255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    cv2.imshow('Original',mask)
    
    ret,thresh = cv2.threshold(mask,127,255,0)
        
    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #print(len(contours))
    
    for cnt in contours :
       
        area = cv2.contourArea(cnt)

        if area >3000:
            
                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                
                    
                d2=str(cx)
                d1=str(cy)
                img= cv2.drawContours(frame, [cnt], 0, (0,0,255), 2)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img,(d2),(cx,cy-30), font,1,(255,255,255),1,cv2.LINE_AA)
                cv2.putText(img,(d1),(cx,cy), font,1,(255,255,255),1,cv2.LINE_AA)

                cv2.circle(frame,(cx,cy), 6, (0,255,0), -1)
                
                #print (cx,cy)
                rimg=cv2.flip(img,1)


                cv2.imshow('Orignal',rimg)
                
                print ('xxx', area)




    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
