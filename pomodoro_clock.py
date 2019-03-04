#!/usr/bin/env python3
"""
Countdown timer using 25 minute increments
 - After first session start a 5 minute timer for break
 - Repeat this three more times, then create a 30 minute break
"""
import time
import winsound


def main():
    work, short_break = (int(1500), int(300))
    frequency = 2500
    duration = 1000

    while True:
        for i in range(3):
            winsound.Beep(frequency, duration)
            print('Time to work!')
            winsound.Beep(frequency, duration)
            time.sleep(work)
            print('Take a five minute break!')
            winsound.Beep(frequency, duration)
            time.sleep(short_break)

        print('Time to work!')
        winsound.Beep(frequency, duration)
        time.sleep(work)
        print('Time for a 25 minute break!')
        winsound.Beep(frequency, duration)
        time.sleep(work)


if __name__ == '__main__':
    main()
