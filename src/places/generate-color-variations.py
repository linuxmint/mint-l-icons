#!/usr/bin/python3
import os

# This script uses green.svg and generates the following files from it:
#
# aqua.svg
# blue.svg
# brown.svg
# grey.svg
# orange.svg
# pink.svg
# purple.svg
# red.svg
# sand.svg
# teal.svg

# It uses the following color table to do so:
COLORS = {}
COLORS["aqua"] = "0b8ac9"
COLORS["blue"] = "356cd2"
COLORS["brown"] = "997052"
COLORS["grey"] = "999999"
COLORS["orange"] = "cc823f"
COLORS["pink"] = "db457c"
COLORS["purple"] = "8463c5"
COLORS["red"] = "ce2639"
COLORS["sand"] = "c5a07c"
COLORS["teal"] = "199ca8"
COLORS["yellow"] = "e7bc0d"

GREEN_COLOR = "8bb158"

for color in COLORS:
    value = COLORS[color]
    os.system("sed 's/%s/%s/g' green.svg > %s.svg" % (GREEN_COLOR, value, color))
