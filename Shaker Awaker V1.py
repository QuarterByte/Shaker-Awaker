from datetime import datetime, date, time, timezone
import time
import RPi.GPIO as GPIO

GPIO. setmode (GPIO. BOARD)
GPIO. setup(7, GPIO.OUT)

now = datetime.now()
hour = now.strftime ("%H:%M:%S")

print (hour)

for i in range(3):
    GPIO.output(7, True)
    time. sleep(2)
    print ("done!")
    GPIO. output(7, False)
    time. sleep(2)
GPIO. cleanup()