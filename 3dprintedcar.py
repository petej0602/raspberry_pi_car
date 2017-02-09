import explorerhat
from time import sleep

#functions to control movements and lights

def drive_forwards(channel,event):
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.backward(100)
    explorerhat.light.off()
    explorerhat.light.green.pulse(0.2,0.2,0.5,0.2)


def reverse(channel,event):
    explorerhat.motor.one.backward(100)
    explorerhat.motor.two.forward(100)
    explorerhat.light.off()
    explorerhat.light.blue.pulse(0.2,0.2,0.5,0.2)


def turn(channel,event):
    explorerhat.motor.one.forward(70)
    explorerhat.motor.two.forward(70)
    explorerhat.light.off()
    explorerhat.light.yellow.pulse(0.2,0.2,0.5,0.2)


def stop(channel,event):
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    explorerhat.light.off()
    explorerhat.light.red.pulse(0.2,0.2,0.5,0.2)
    sleep(1)
    explorerhat.light.off()
    
#events to call functions when touch capacitors pressed
explorerhat.touch.one.pressed(drive_forwards)
explorerhat.touch.two.pressed(reverse)
explorerhat.touch.three.pressed(turn)
explorerhat.touch.four.pressed(stop)
    
