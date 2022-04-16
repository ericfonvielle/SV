from microbit import *
import utime
import machine
distance = 0.4
def duree():
    # On envoie une salve sonore
    pin0.write_digital(0)
    utime.sleep_us(2)
    pin0.write_digital(1)
    utime.sleep_us(10)
    pin0.write_digital(0)
    pin0.read_digital()

    #On attend que le son revienne
    duree = machine.time_pulse_us(pin0, 1, 1000000)
    return duree

while True:
    print("Vitesse du son = ", ##############FORMULE&&&&&&)
    sleep(500)