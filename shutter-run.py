#!/usr/bin/env python
from __future__ import print_function, division, unicode_literals, absolute
import argparse
import time
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script to operate the VeloceCal shutter')
    parser.add_argument('--nopen', '-n',
                        help='Number of times to open the shutter, default 2',
                        type=int,
                        default=2)
    parser.add_argument('--delay', '-d',
                        help='Delay, in seconds, before starting the shutter sequence, default 0',
                        type=float,
                        default=0)
    parser.add_argument('--host',
                        help='Hostname or IP address of the Raspberry Pi controlling the shutter',
                        default='10.88.21.151')
    parser.add_argument('opentime',
                        help='Total time to keep the shutter open for, in seconds',
                        type=float)
    parser.add_argument('totaltime',
                        help='Total elapsed time for the shutter opening sequence, in seconds',
                        type=float)
    args = parser.parse_args()

    # Need to set these environment variables otherwise the imports fail
    os.environ['GPIOZERO_PIN_FACTORY'] = 'pigpio'
    os.environ['PIGPIO_ADDR'] = args.host

    # Need to import down here because they fail if done before setting the environment variables
    from gpiozero import DigitalOutputDevice
    from gpiozero.pins.pigpio import PiGPIOFactory

    # Connect to GPIO 27 on the Raspberry Pi
    remote_pin_factory = PiGPIOFactory(host=args.host)
    shutter = DigitalOutputDevice(pin=27, pin_factory=remote_pin_factory)

    exposure = args.opentime / args.nopen
    wait_time = (args.totaltime - args.opentime) / (args.nopen - 1)

    time.sleep(args.delay)
    shutter.blink(on_time=exposure, off_time=0, n=1, background=False)
    for i in range(args.nopen - 1):
        time.sleep(wait_time)
        shutter.blink(on_time=exposure, off_time=0, n=1, background=False)

    shutter.close()
