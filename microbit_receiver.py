from microbit import*
import music
import radio

radio.config(group = 13)

while True:
    message_in = radio.receive()
    if message_in == "Intrusion detected":
        display.scroll(message_in)
        music.pitch(2000, wait = False)
        while not button_a.get_presses():
            sleep(60)
            music.stop()
            sleep(1000)
    if button_b.get_presses():
        radio.send("Reset")
