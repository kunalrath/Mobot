#...........project by Kunal Rathod........#

from machine import Pin, SPI
import struct
import utime
from nrf24l01 import NRF24L01
import motor_module as motor 

csn = Pin(15, mode=Pin.OUT, value=1) 
ce  = Pin(14, mode=Pin.OUT, value=0)


pipeline = (b"\xe1\xf0\xf0\xf0\xf0")
nrf = NRF24L01(SPI(0), csn, ce, payload_size=4)
nrf.open_rx_pipe(1, pipeline)
nrf.reg_write(0x01, 0b11111000)
nrf.start_listening()
while True:
    buf=nrf.recv()
    got=struct.unpack("i", buf)[0]
    if got == 1:
        motor.fwd()
    elif got == 2:
        motor.bwd()
    elif got == 3:
        motor.rht()
    elif got == 4:
        motor.lft()
    elif got==0:
        motor.stop()
        
    print("rx",got)
    utime.sleep(0.02)

#     utime.sleep(0.1)
