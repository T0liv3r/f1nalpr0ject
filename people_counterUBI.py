from ubidots import ApiClient
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN)

try:
    api = ApiClient("BBUS-810e5c801c34375eb2d8fbadd68bef48121")
    people = api.get_variable("65711f5c453dd1164ddd8054")
except:
    print("Couldn't connect to the API, check your Internet connection")

counter = 0
peoplecount = 0

while(1):
    presence = GPIO.input(7)
    if(presence):
        peoplecount += 1
        presence = 0
        time.sleep(1.5)
    time.sleep(1)
    counter += 1
    if(counter==10):
        print(peoplecount)
        people.save_value({'value':peoplecount})
        counter = 0
        peoplecount = 0
