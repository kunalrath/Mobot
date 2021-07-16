#....project by Kunal Rathod..........#
from machine import Pin
M1a = Pin(0, Pin.OUT)
M1b = Pin(1, Pin.OUT)

M2a = Pin(2, Pin.OUT)
M2b = Pin(3, Pin.OUT)

M3a = Pin(18, Pin.OUT)
M3b = Pin(19, Pin.OUT)

M4a = Pin(20, Pin.OUT)
M4b = Pin(21, Pin.OUT)

def fwd():
    M1a.value(1)
    M1b.value(0)

    M2a.value(0)
    M2b.value(1)


    M3a.value(1)
    M3b.value(0)

    M4a.value(0)
    M4b.value(1)
    
def bwd():
    M1a.value(0)
    M1b.value(1)

    M2a.value(1)
    M2b.value(0)


    M3a.value(0)
    M3b.value(1)

    M4a.value(1)
    M4b.value(0)
    
def lft():
    M1a.value(0)
    M1b.value(1)

    M2a.value(1)
    M2b.value(0)


    M3a.value(1)
    M3b.value(0)

    M4a.value(1)
    M4b.value(0)
    
def rht():
    M1a.value(1)
    M1b.value(0)

    M2a.value(0)
    M2b.value(1)


    M3a.value(0)
    M3b.value(1)

    M4a.value(0)
    M4b.value(1)

def stop():
    M1a.value(0)
    M1b.value(0)

    M2a.value(0)
    M2b.value(0)


    M3a.value(0)
    M3b.value(0)

    M4a.value(0)
    M4b.value(0)
