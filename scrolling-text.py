#!/usr/bin/python3

import time

ERASE_LINE = "\033[2K\r"

def scrolling_text(text: str):
    # The text will have 3 states that will need to be handled differently.
    
    # Left-end:
    # Only a portion of the left side of the text is shown
    # |     This is|
    
    # Middle-scroll:
    # When the entire width is taken up by a portion of the text
    # |is an exampl|
    
    # Right-end:
    # The end (right) portion scrolling off
    # |an example  |

    raise NotImplementedError()

if __name__ == "__main__":
    text = input("> ")
    print(f"\033[1A", end="")
    scrolling_text(text)