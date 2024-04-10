# Simple BASIC like text editor

import sys

# Where Data Store
global data
data = {}

# Save
def save(path):
    string = ""
    for i in data:
        string = string + data[i] + "\n"

    with open(path, "w") as f:
        f.write(string)

# Load
def load(path):
    line_counter = 0

    with open(path, "r") as f:
        for i in f.readlines():
            data[line_counter] = i.strip()
            line_counter += 10

def run():
    global data
    print("BED - BASIC Editor")

    while True:
        try:
            words = input("> ") # Input
            args = words.split() # Split
            if not words:
                pass
            elif args[0].isdigit():
                data[int(args[0])] = " ".join(args[1:]) # Storing text with line number
                data = {key: data[key] for key in sorted(data)} # Order it
            # List command
            elif args[0].upper() == "LIST":
                # Example: list [LINE NUMBER]
                if len(args) > 1:
                    print(data[int(args[1])])
                # Example: list
                else:
                    for i in data:
                        print(str(i) + " " + data[i])
            # Save
            elif args[0].upper() == "SAVE":
                save(args[1])
            # Load
            elif args[0].upper() == "LOAD":
                load(args[1])
            # New
            elif args[0].upper() == "NEW":
                data = {}
            elif args[0].upper() == "EXIT":
                sys.exit()
            else:
                if not data:
                    data[0] = words
                else:
                    data[list(data.keys())[-1] + 1] = words
        except KeyboardInterrupt:
            break
        except Exception as e: print(e)
