#!/usr/bin/env python
# coding=utf-8
import sys
import time

from lifxlan import LifxLAN, WHITE, BLUE, PINK, WARM_WHITE


PINK1 = [58275, 25535, 47142, 4500]
BLUE1 = [43634, 25535, 65535, 3500]

def main():
    num_lights = None
    if len(sys.argv) != 2:
        print("\nDiscovery will go much faster if you provide the number of lights on your LAN:")
        print("  python {} <number of lights on LAN>\n".format(sys.argv[0]))
    else:
        num_lights = int(sys.argv[1])

    print("Discovering lights...")
    lifx = LifxLAN(num_lights)

    devices = lifx.get_lights()

    bulb = devices[0]

    print("Making colors happen...")
    bulb.set_color(WARM_WHITE, 7000, False)

if __name__=="__main__":
	main()
