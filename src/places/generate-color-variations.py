#!/usr/bin/python3
import os

# This script uses src.svg and generates the following files from it:
#
# green.svg
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

SRC = {"folder":"eeca8f","backfolder":"c89e6b","paper":"e4e4e4","line":"92b372","emblem":"575757"}
GREEN = {"name":"green","folder":"f9ca70","backfolder":"e19d00","paper":"e4e4e4","line":"35a854","emblem":"1f1f1f"}
AQUA = {"name":"aqua","folder":"f9ca70","backfolder":"e19d00","paper":"e4e4e4","line":"1f9ede","emblem":"1f1f1f"}
BLUE = {"name":"blue","folder":"f9ca70","backfolder":"e19d00","paper":"e4e4e4","line":"0c75de","emblem":"1f1f1f"}
BROWN = {"name":"brown","folder":"f9ca70","backfolder":"e19d00","paper":"e4e4e4","line":"aa876a","emblem":"1f1f1f"}
GREY = {"name":"grey","folder":"f9ca70","backfolder":"e19d00","paper":"e4e4e4","line":"70737a","emblem":"1f1f1f"}
ORANGE = {"name":"orange","folder":"f9ca70","backfolder":"e19d00","paper":"e4e4e4","line":"ff7139","emblem":"1f1f1f"}
PINK = {"name":"pink","folder":"f9ca70","backfolder":"e19d00","paper":"e4e4e4","line":"e54980","emblem":"1f1f1f"}
PURPLE = {"name":"purple","folder":"f9ca70","backfolder":"e19d00","paper":"e4e4e4","line":"8c5dd9","emblem":"1f1f1f"}
RED = {"name":"red","folder":"f9ca70","backfolder":"e19d00","paper":"e4e4e4","line":"e82127","emblem":"1f1f1f"}
SAND = {"name":"sand","folder":"f9ca70","backfolder":"e19d00","paper":"e4e4e4","line":"c5a07c","emblem":"1f1f1f"}
TEAL = {"name":"teal","folder":"f9ca70","backfolder":"e19d00","paper":"e4e4e4","line":"199ca8","emblem":"1f1f1f"}

VARIANTS = [GREEN, AQUA, BLUE, BROWN, GREY, ORANGE, PINK, PURPLE, RED, SAND, TEAL]

for variant in VARIANTS:
    name = variant["name"]
    os.system(f"cp src.svg {name}.svg")
    for key in SRC.keys():
        src_color = SRC[key]
        color = variant[key]
        if src_color != color:
            os.system("sed -i 's/%s/%s/g' %s.svg" % (src_color, color, name))
