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
GREEN = {"name":"green","folder":"f9bd30","backfolder":"e19d00","paper":"e4e4e4","line":"92b372","emblem":"575757"}
AQUA = {"name":"aqua","folder":"f9bd30","backfolder":"e19d00","paper":"e4e4e4","line":"1f9ede","emblem":"575757"}
BLUE = {"name":"blue","folder":"f9bd30","backfolder":"e19d00","paper":"e4e4e4","line":"5b73c4","emblem":"575757"}
BROWN = {"name":"brown","folder":"f9bd30","backfolder":"e19d00","paper":"e4e4e4","line":"aa876a","emblem":"575757"}
GREY = {"name":"grey","folder":"f9bd30","backfolder":"e19d00","paper":"e4e4e4","line":"9d9d9d","emblem":"575757"}
ORANGE = {"name":"orange","folder":"f9bd30","backfolder":"e19d00","paper":"e4e4e4","line":"ff7139","emblem":"575757"}
PINK = {"name":"pink","folder":"f9bd30","backfolder":"e19d00","paper":"e4e4e4","line":"e54980","emblem":"575757"}
PURPLE = {"name":"purple","folder":"f9bd30","backfolder":"e19d00","paper":"e4e4e4","line":"8c5dd9","emblem":"575757"}
RED = {"name":"red","folder":"f9bd30","backfolder":"e19d00","paper":"e4e4e4","line":"e82127","emblem":"575757"}
SAND = {"name":"sand","folder":"f9bd30","backfolder":"e19d00","paper":"e4e4e4","line":"c5a07c","emblem":"575757"}
TEAL = {"name":"teal","folder":"f9bd30","backfolder":"e19d00","paper":"e4e4e4","line":"199ca8","emblem":"575757"}

VARIANTS = [GREEN, AQUA, BLUE, BROWN, GREY, ORANGE, PINK, PURPLE, RED, SAND, TEAL]

for variant in VARIANTS:
    name = variant["name"]
    os.system(f"cp src.svg {name}.svg")
    for key in SRC.keys():
        src_color = SRC[key]
        color = variant[key]
        if src_color != color:
            os.system("sed -i 's/%s/%s/g' %s.svg" % (src_color, color, name))
