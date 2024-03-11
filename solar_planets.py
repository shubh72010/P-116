import cv2

img = cv2.imread("solar-system.jpg")


cv2.putText(img,
        "sun",
        (90,100),
        cv2.FONT_HERSHEY_COMPLEX,
        1,
        (255,255,255)
        )

cv2.putText(img,"Mercury",(100,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Venus",(190,255),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Earth",(290,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Mars",(380,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Jupiter",(580,50),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Saturn",(780,90),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Uranus",(957,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Neptune",(1100,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imshow("output",img)

cv2.waitKey(0)
