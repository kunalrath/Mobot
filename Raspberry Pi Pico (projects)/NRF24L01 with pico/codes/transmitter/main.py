#........project by Kunal Rathod..............#
# tx...........................

from machine import Pin, SPI, ADC, I2C


# from sh1106 import SH1106_I2C

import struct
import utime
from nrf24l01 import NRF24L01

sys_led = Pin(16, Pin.OUT)     
sysinput_led = Pin(17, Pin.OUT)                
csn = Pin(15, mode=Pin.OUT, value=1)  
ce  = Pin(14, mode=Pin.OUT, value=0)  


# i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
# oled = SH1106_I2C(128,64, i2c)



x0Axis = ADC(Pin(27))
x1Axis = ADC(Pin(28))
y0Axis = ADC(Pin(26))

# oled.fill(0)
# oled.show()

pipeline = (b"\xe1\xf0\xf0\xf0\xf0")
nrf = NRF24L01(SPI(0), csn, ce, payload_size=4)
nrf.open_tx_pipe(pipeline)
nrf.reg_write(0x01, 0b11111000)
sys_led.value(1)
state = 0
while True:
    state = 0
    x0Value = x0Axis.read_u16()
    y0Value = y0Axis.read_u16()
    x1Value = x1Axis.read_u16()
    if x0Value >= 40000:
        state = 1
        sysinput_led.value(1)
        
#         oled.text("v", 64, 32)
#         oled.show()
        
    elif x0Value <= 20000:
        state = 2
        sysinput_led.value(1)
        
    elif x1Value >= 40000:
        state = 5
        sysinput_led.value(1)
        
    elif x1Value <= 20000:
        state = 6
        sysinput_led.value(1)
        
    elif y0Value >= 40000:
        state = 3
        sysinput_led.value(1)
        
    elif y0Value <= 20000:
        state = 4
        sysinput_led.value(1)
        
    else:
        state = 0
        sysinput_led.value(0)
#         oled.fill(0)
#         oled.show()
    try:
        nrf.send(struct.pack("i", state))
    except OSError:
        print('message lost')
        sysinput_led.value(1)
        utime.sleep(1)
        
    print(state)
    utime.sleep(0.01)
