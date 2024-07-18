#!/usr/bin/python3

import time

ERASE_LINE = "\033[2K\r"

def scrolling_text(text: str, width: int = 16):
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

    start_i = 0
    end_i = 0
    # Finite state machine time
    # 0:left, 1:mid, 2:right, 3:reset
    # States: left, mid, mid-short, right, reset
    state = "left"

    while 1:
        if state == "left":
            output_line = f"|{text[start_i:end_i]:>{width}}|"
            end_i += 1
            
            if end_i == width:
                state = "mid" 
            
        elif state == "mid":
            output_line = f"|{text[start_i:end_i]}|"
            start_i += 1
            end_i += 1
            
            if end_i > len(text):
                state = "right"
            
        elif state == "right":
            output_line = f"|{text[start_i:end_i]:<{width}}|"
            start_i += 1
            
            if start_i > len(text):
                state = "reset"
            
        elif state == "reset":
            start_i = 0
            end_i = 1
            state = "left"

        print(f"{ERASE_LINE}{output_line}", end="")
        time.sleep(0.1)

if __name__ == "__main__":
    scrolling_text("This is an example")