from microbit import*
import music
import radio

radio.config(group = 13)

while True:
    message_in = radio.receive()
    if message_in == "Intrusion detected":
        display.scroll(message_in)
        music.pitch(2000, wait = False)
