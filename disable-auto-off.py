from playsound import playsound
from tendo import singleton

# disable multiple instances of the app
me = singleton.SingleInstance()
# disable multiple instances of the app

# loop 30 second silence endlessly
def sound():
    playsound('silent.mp3')
    sound()

sound()
# loop 30 second silence endlessly