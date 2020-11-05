#!/usr/bin/python3
 
# adapted from https://github.com/recantha/EduKit3-RC-Keyboard/blob/master/rc_keyboard.py
 
import sys, termios, tty, os, time
from pydub import AudioSegment
from pydub.playback import play
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
button_delay = 0.2


track1 = AudioSegment.from_mp3('AudioSamples/Track1.mp3')
track2 = AudioSegment.from_mp3('AudioSamples/Track2.mp3')
track3 = AudioSegment.from_mp3("AudioSamples/output.mp3")
 
while True:

    #some method to scan for which audio files currently connected

    char = getch()
 

    #file 1 activated
    if (char == "1"):
        print("File 1 Only")
        play(track1)
 
    #file 2 activated
    if (char == "2"):
        print("File 2 Only")
        play(track2)

    #file 1 & 2 both on
    elif (char == "3"):
        print("Both Files")
        play(track3)
        
    
    #nothing on
    elif (char == "0"):
        print("Nothing playing")
        time.sleep(2)
 
 
    elif (char == "4"):
        print("Exit!")
        time.sleep(button_delay)
        exit(0)