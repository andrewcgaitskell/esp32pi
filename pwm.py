import machine
import time
p15 = machine.Pin(15)
pwm15 = machine.PWM(p15)
pwm15.freq(500)
pwm15.duty(512)
time.sleep(1)
pwm15.deinit()
