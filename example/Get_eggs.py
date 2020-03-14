from NXController import Controller

ctr = Controller()
## Or use your serial port if you have many
# ctr = Controller('/dev/tty.usbserial-AO0099VT');

for x in range(300):
    for i in range(2):
        # Hold two stick in the oppsite direction
        ctr.ls_l(-1)
        ctr.rs_r(-1)
        ctr.pause(1.8)
        ctr.release()
        # Backwards
        ctr.ls_r(-1)
        ctr.rs_l(-1)
        ctr.pause(1.76)
        ctr.release()
    ctr.pause(0.5)
    ctr.A()
    ctr.pause(0.5)
    ctr.A()
    ctr.pause(4)
    ctr.B()
    ctr.pause(2)
    ctr.B()
    ctr.pause(1.4)
    ctr.B()
    ctr.pause(0.1)
    ctr.release()

ctr.close()
