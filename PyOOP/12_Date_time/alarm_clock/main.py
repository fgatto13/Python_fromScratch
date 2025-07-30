# alarm clock in Python!

import time
import datetime
# the pygame module helps us in using music effects
import pygame

# the alarm_time parameter is a string representing a time in military format
def set_alarm(alarm_time):
    print(f"alarm set for {alarm_time}")

def main():
    # we now need to create an alarm song
    # to do so, we first need to set the path to the sound file
    sound_file = "computing-sound-2-94849.mp3"
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
    is_running = True
    while is_running:
        # we retrieve the current time, and format it to only get the hours, minutes and seconds
        current = datetime.datetime.now().strftime("%H:%M:%S")
        print(current)
        time.sleep(1)
        if current == alarm_time:
            print("Wake up!")
            # to play the mp3 file, we access the mixer module from the pygame module:
            pygame.mixer.init() # when we create a mixer, we need to initialize it (we can also pass a bunch of parameters)
            # to load the file, we use the load method:
            pygame.mixer.music.load(sound_file)
            # and to play it, we use the play method:
            pygame.mixer.music.play()
            # to keep playing the music file while the mixer is busy,
            # we can create a while loop:
            while pygame.mixer.music.get_busy(): # it returns a boolean
                time.sleep(1)
            is_running = False

if __name__ == "__main__":
    main()
