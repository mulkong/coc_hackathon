#-*- coding: utf-8 -*- # gilit_jy^^

import cv2
 
vidcap = cv2.VideoCapture('/Users/kk/Downloads/SewerPipe.mp4')
 
count = 0
 
while(vidcap.isOpened()):
    ret, image = vidcap.read()
 
    if(int(vidcap.get(1)) % 100 == 0): # 전체 영상의 1/100 프레임 추출
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite("/Users/kk/Desktop/SewerPipe/frame%d.jpg" % count, image)
        print('Saved frame%d.jpg' % count)
        count += 1


vidcap.release()
