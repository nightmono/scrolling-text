#!/usr/bin/python3

import time

ERASE_LINE = "\033[2K\r"

def scrolling_text(text: str):
    raise NotImplementedError()

if __name__ == "__main__":
    scrolling_text(input("> "))