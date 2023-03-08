from microbit import *
import utime
import machine
import music
import radio

radio.config(group = 13)

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
    message_in = radio.receive()
    current_distance = get_distance()

    if abs(start_distance - current_distance) > 10:
        sleep(3000)
        print(current_distance)
        second_distance = get_distance()

        if abs(start_distance - second_distance) > 10:
            radio.send("Intrusion detected")
            print("Intrusion detected:", second_distance)

    if message_in == "Reset" ():
        start_distance = get_distance()






