#!/usr/bin/python3

import time

ERASE_LINE = "\033[2K\r"

def scrolling_text(text: str):
    frame = 0
    max_frame = len(text)
    while 1:
        if frame <= max_frame:
            output = f"{text[0:frame]:>{max_frame}}"
        else:
            output = f"{text[frame-max_frame:max_frame]:<{max_frame}}"

        print(f"{ERASE_LINE}{output}", end="")
        
        frame += 1
        if frame > max_frame * 2:
            frame = 0
        time.sleep(0.1)

if __name__ == "__main__":
    scrolling_text(input("> "))