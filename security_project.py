from microbit import *
import utime
import machine
import music

def get_distance():
    # Distanz messen
    pin1.write_digital(1)   # Pin 1 (Trigger) HIGH für...
    utime.sleep_us(10)      # ...10 µs...
    pin1.write_digital(0)   # ...und wieder LOW
    echo_pulse = machine.time_pulse_us(pin2, 1) # Messe, wie lange der Echo-Impuls an Pin 2 dauert.
    distance = echo_pulse * 0.017 # Rechne Zeit in Distanz um.
    return distance

start_distance = get_distance()
print("Starting up, initial dist: ", start_distance)
while True:
    current_distance = get_distance()
    if abs(start_distance - current_distance) > 10:
        sleep(3000)
        print(current_distance)
        second_distance = get_distance()
        if abs(start_distance - second_distance) > 10:
            print("Intrusion detected:", second_distance)
            music.pitch(2000, wait=False)
            while not button_a.get_presses():
                sleep(59)
            music.stop()
            sleep(1000)
    

