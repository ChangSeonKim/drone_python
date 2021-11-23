from djitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff()
tello.move_up(50)
tello.move_forward(60)
tello.move_back(60)
tello.land()
pass