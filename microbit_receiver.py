from microbit import*
import music
import radio

radio.config(group = 13)
radio.on()

receive = 1
while True:
    message_in = radio.receive()

    if message_in == "Intrusion detected" and receive==1:
        display.scroll(message_in, wait=False)
        music.pitch(2000, wait = False)
        while not button_a.get_presses():
            sleep(50)
        music.stop()
        receive = 0
        message_in = "no"
        display.clear()

    if button_b.get_presses():
        radio.send("Reset")
        receive = 1
