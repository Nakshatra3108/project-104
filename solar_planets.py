import cv2
img=cv2.imread('solar-system.jpg')

cv2.putText(img,'Sun',(20,300),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,0,0),2)
cv2.putText(img,'Mercury',(110,190),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
cv2.putText(img,'Venus',(190,260),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
cv2.putText(img,'Earth',(285,175),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
cv2.putText(img,'Mars',(380,255),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
cv2.putText(img,'Jupiter',(480,255),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
cv2.putText(img,'Saturn',(750,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
cv2.putText(img,'Uranus',(940,145),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
cv2.putText(img,'Neptune',(1080,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
cv2.imshow('Image',img)
cv2.waitKey(0)

cv2.imwrite('Solar-system-named.jpg',img)