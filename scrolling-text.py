#!/usr/bin/python3

import time
from shutil import get_terminal_size

ERASE_LINE = "\033[2K\r"

def scrolling_text(text: str, width: int = 32, center=False, delay=0.1):
    start_i = 0
    end_i = 0
    # Finite state machine time
    # States: left, mid, mid-short, right, reset
    state = "left"

    while 1:
        if state == "left":
            output_line = f"|{text[start_i:end_i]:>{width}}|"
            end_i += 1
            
            if end_i == width:
                state = "mid"  
            elif end_i == len(text):
                state = "mid-short"
                padding = width - len(text)
            
        elif state == "mid":
            output_line = f"|{text[start_i:end_i]}|"
            start_i += 1
            end_i += 1
            
            if end_i > len(text):
                state = "right"
            
        elif state == "mid-short":
            output_line = f"|{' '*padding}{text[start_i:end_i]:<{width-padding}}|" 
            padding -= 1
            
            if padding == 0:
                state = "right"
            
        elif state == "right":
            output_line = f"|{text[start_i:end_i]:<{width}}|"
            start_i += 1
            
            if start_i > len(text):
                state = "reset"
            
        if state == "reset":
            start_i = 0
            end_i = 0
            state = "left"

        if center:
            terminal_width = get_terminal_size().columns
            # `rstrip` to avoid issues when making the terminal width smaller.
            output_line = output_line.center(terminal_width).rstrip()  
        print(f"{ERASE_LINE}{output_line}", end="")
        time.sleep(delay)

def main():
    import argparse
    import sys
    
    parser = argparse.ArgumentParser("Scrolling text display")
    parser.add_argument("text", nargs="*", help="text that will be scrolled")
    parser.add_argument("-w", "--width", help="width of the display", type=int)
    parser.add_argument("-c", "--center", help="center the display", action="store_true") 
    parser.add_argument("-d", "--delay", help="delay between each screen update in seconds (default: 0.1)", type=float) 
    
    args = parser.parse_args()

    text = " ".join(args.text)    
    if not text:
        parser.print_help()
        sys.exit()

    width = args.width or 32
    delay = args.delay or 0.1
    
    try:
        scrolling_text(text, width=width, center=args.center, delay=delay)
    except KeyboardInterrupt:
        print("\nScrolling text killed.")

if __name__ == "__main__":
    main()