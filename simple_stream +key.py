def fun():
    

    from djitellopy import Tello
    import cv2 

    # tello 생성자 생성
    tello = Tello()

    # tello 연결
    tello.connect()

    # tello video 연결
    tello.streamon()

    # 비디오 연결
    while True:
        fr_read = tello.get_frame_read()
        cv2.imshow('tello stream', fr_read.frame)
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
            
#simply_stream.py + move contorl with key fun화q
    return

if __name__ == "__main__":
    fun()