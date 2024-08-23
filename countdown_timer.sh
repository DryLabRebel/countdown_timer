#!/usr/bin/env bash

time="${1:-5}"
scale="${2:-m}"

echo $time
echo $scale

echo $seconds

if [[ "$scale" == "s" ]]
then
    seconds="$time"
elif [[ "$scale" == "m" ]]
then
    seconds=$(($time*60))
elif [[ "$scale" == "h" ]]
then
    seconds=$(($time*60*60))
else printf "\nInvalid time units, please enter 's' for seconds, 'm' for minutes or 'h' for hours.\n"
fi

# TODO: Add option to input hours or minutes

printf "\nWelcome to the countdown timer.\n"
printf "The countdown will run for 5 minutes if no argument is supplied.\n"
printf "\nCountdown timer set for $time$scale.\n\n"
sleep "$seconds" && say "times up"
printf "\n\nCountdown complete.\n"
