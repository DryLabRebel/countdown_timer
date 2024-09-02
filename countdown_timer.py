#!/usr/bin/env python3

import argparse
import os
import time
import pyttsx3 as tts

parser = argparse.ArgumentParser()
parser.add_argument("--value")
parser.add_argument("--scale")
args = parser.parse_args()

count = args.value
# count = 5
scale = args.scale
# scale = 's'

if scale == 's':
  seconds = count
  units = 'seconds'
if scale == 'm':
  seconds = count*60
  units = 'minutes'
if scale == 'h':
  seconds = count*(60**2)
  units = 'hours'

print("Welcome to the countdown timer.")
print("The countdown will run for 5 minutes if no argument is supplied.")
print(f"Countdown timer set for {count} {units}.")

try:
  time.sleep(seconds)
except Exception:
  pass
else:
  tts.speak("times up!")

print("Countdown complete.")
