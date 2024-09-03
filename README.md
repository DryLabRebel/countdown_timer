Countdown Timer
===============

A *very* simple countdown timer.

Welcome to the countdown timer.

This program will take a single integer, and one of either 's' (seconds), 'm' (minutes) or 'h' (hours) to denote the time scale. The defaults are 5 and 'm'.

Example:

    $ python 3 countdown-timer --value 5 --scale 's'

Will set a countdown timer for 5 seconds, and depending on your OS and implementation of bash, should end with a pleasant response "times up".

The countdown will run for 5 minutes if no argument is supplied.

The maximum value is 60, and therefore the upper limit to the countdown is 60 hours.

The program will warn you, and prompt for confirmation if you set a time of 5 hours or more.

Dependencies:

- `python 3`
- `sys`
- `time`
- `pyttsx3`
- `argparse`

> TODO: Create an alarm clock!

