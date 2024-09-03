import os
import sys
import time
import pyttsx3 as tts

def the_long_wait(scale, count):
  if (scale == 'h') and (count >= 5):
    long_wait = input("Wow, 5 hours is a lot, are you sure (y or n)? ")
    if long_wait == 'y':
      print("OK, if you're sure!")
      pass
    elif long_wait == 'n':
      sys.exit("Probably wise. Exiting the countdown timer now...")
    else:
      sys.exit("Invalid input. Exiting the coundown timer now...")
  else:
    print("Yes, everything looks in order...")

def scaler(scale, count):
  if scale == 's':
    seconds = count
    units = 'seconds'
  if scale == 'm':
    seconds = count*60
    units = 'minutes'
  if scale == 'h':
    seconds = count*(60**2)
    units = 'hours'
  return seconds, units

def countdown_timer(seconds):
  try:
    time.sleep(seconds)
  except Exception:
    pass
  else:
    tts.speak("times up!")
