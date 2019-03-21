# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:03:40 2019

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:56:08 2019

@author: User
"""

"""code for colour filter """
import cv2 
import numpy as np 
cap=cv2.VideoCapture(0)
test=cap
while True :
    a=[]
    c=0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    _, frame = cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#filter
#red color  
    lower_red=np.array([161,130,80])#(161,155,84)
    upper_red=np.array([200,255,255])
    #in the output console the red color is outputed as white and background becomes black 
    red_mask=cv2.inRange(hsv_frame,lower_red,upper_red)#
    #to make the output cosole have a red patch 
    red=cv2.bitwise_and(frame,frame,mask=red_mask)
    blur_median=cv2.medianBlur(red,15)
    kernel=np.ones((5,5),np.uint8)
    # REMOVES FALSE POSITIVE   
    opening = cv2.morphologyEx(blur_median, cv2.MORPH_OPEN, kernel)
   #removes false negative 
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    #convert to grayscale for hough 
    frame_color=cv2.cvtColor(closing,cv2.COLOR_HSV2BGR)
    frame_gray=cv2.cvtColor(frame_color,cv2.COLOR_BGR2GRAY)
         
    _, contours, _ = cv2.findContours(frame_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 
    font = cv2.FONT_HERSHEY_COMPLEX
    
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        cv2.drawContours(frame, [approx], 0, (0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        
        if len(approx) == 3:
            cv2.putText(frame, "Triangle", (x, y), font, 1, (0))
       
        elif 6 < len(approx) < 15:
            c=c+1
            cv2.putText(frame, "SLot_"+str(c), (x, y), font, 1, (0))
            a.append(c)
        else:
            c=c+1
            cv2.putText(frame, "Slot_"+str(c), (x, y), font, 1, (0))
            a.append(c)
        '''cv2.putText(frame,"number of empty slots are"+str(c),(100,100),font,1,(0))'''
    cv2.imshow("frame",frame)
    cv2.imshow("gray scale converted",frame_gray)
    print("number of empty slots are "+str(c))
    b=c
print("NUMBER OF EMPTY SLOTS ARE "+str(b))
while True:
    _,hi=test.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.putText(hi,"THE NUMBER OF EMPTY SLOTS ARE "+str(b),(10,100),font,1,(0))       
    cv2.imshow("final",hi)
    
    print("test")
cv2.destroyAllWindows()
