from djitellopy import Tello
import cv2
tello = Tello()
tello.connect()
stream  = cv2.imread('./drone.jpg')
#move control with keyboard
cv2.imshow("tello image", stream)
while True:
    key = cv2.waitKey(1)
    if key == ord('u'):
        tello.move_up(50)
    elif key == ord('t'):
        tello.takeoff()
    elif key == ord('f'):
        tello.move_forward(60)
    elif key == ord('c'):
        tello.rotate_clockwise(90)
    elif key == ord('b'):
        tello.move_back(60)
    elif key == ord('l'):
        tello.land()
    elif key == ord('q'):
        break
        
    
    
            

