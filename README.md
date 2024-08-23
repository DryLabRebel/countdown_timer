Countdown Timer
===============

A *very* simple countdown timer.

> TODO: Add flags to used as named arguments

Welcome to the countdown timer.

This program will take a single integer, and one of either 's' (seconds), 'm' (minutes) or 'h' (hours) to denote the time scale. The defaults are 5 and 'm'.

Example:

    $ countdown-timer 5 s

Will set a countdown timer for 5 seconds, and depending on your OS and implementation of bash, should end with a pleasant response "times up".

The countdown will run for 5 minutes if no argument is supplied.

Dependencies:

- `bash`
- `sleep`
- `printf`
- `say`

