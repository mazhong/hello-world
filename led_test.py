from Adafruit_BBIO import GPIO
import time
    
for i in range(4):
    GPIO.setup("USR%d" % i, GPIO.OUT)

while True:
    try:
        for i in range(4):
            GPIO.output("USR%d" % i, GPIO.HIGH)
            time.sleep(0.3)
        for i in range(4):
            GPIO.output("USR%d" % i, GPIO.LOW)
            time.sleep(0.3)
    except KeyboardInterrupt:
        for i in range(4):
            GPIO.output("USR%d" % i, GPIO.LOW)
        GPIO.cleanup()