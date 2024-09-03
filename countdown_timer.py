#!/usr/bin/env python3

import argparse
import os
import sys
import time
import pyttsx3 as tts
from functions_countdown_timer import (
    the_long_wait,
    scaler,
    countdown_timer
    )

parser = argparse.ArgumentParser()

# Designate the scale of the supplied units
parser.add_argument(
    "--scale",
    default = 'm'
    )
# Designate the length of time (in scale)
parser.add_argument(
    "--value",
    type = int,
    default = 5,
    choices = range(60)
    )

args = parser.parse_args()

scale = args.scale
count = args.value
# scale = 's'
# count = 5

the_long_wait(scale, count)

seconds, units = scaler(scale, count)

print("Welcome to the countdown timer.")
print("The countdown will run for 5 minutes if no argument is supplied.")
print(f"Countdown timer set for {count} {units}.")

countdown_timer(seconds)

print("Countdown complete.")
