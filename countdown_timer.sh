#!/usr/bin/env bash

minutes="${1:-5}"
seconds=$(($minutes*60))

# TODO: Add option to input hours or minutes

printf "\nWelcome to the countdown timer.\n"
printf "The countdown will run for 5 minutes if no argument is supplied.\n"
printf "\nCountdown timer set for $minutes minutes.\n\n"
sleep $seconds && say "times up"
printf "\n\nCountdown complete.\n"

