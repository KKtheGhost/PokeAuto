from NXController import Controller

ctr = Controller()
## Or use your serial port if you have many
# ctr = Controller('/dev/tty.usbserial-AO0099VT');
#for i in range(10):
#    ctr.ls_r(1)
#    ctr.pause(0.2)
#    ctr.ls_l(1)
#    ctr.pause(0.2)
ctr.A()
