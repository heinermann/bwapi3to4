#!/usr/bin/python3
import os
from changes import *


BOT_DIR = "bot_sources"
DEFAULT_BOT = "ualberta"


def get_source_files(bot_name):
    source_files = []

    for root, dirs, files in os.walk("./{}/{}".format(BOT_DIR, bot_name)):
        for f in files:
            if f.endswith(".cpp"):
                source_files.append(os.path.join(root, f))

    return source_files


def convert(source):
    modified = simple_replace(source)
    return modified


if __name__ == "__main__":
    bot = DEFAULT_BOT
    bot = input("Bot to convert: ")

    files = get_source_files(bot)

    for filename in files[:2]:
        old = None
        with open(filename, 'r') as fp:
            old = fp.read()
        new = convert(old)
        print(new)
        outputFile = filename.replace("./{}".format(BOT_DIR), "./converted")
        print(outputFile)
        # Find out how to save to file
