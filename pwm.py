import machine
import time
p12 = machine.Pin(12)
pwm12 = machine.PWM(p12)
pwm12.freq(500)
pwm12.duty(512)
time.sleep(1)
pwm12.deinit()
