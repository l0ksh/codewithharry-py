#!/usr/bin/python3

def wipe_file(file_path):
    with open(file_path, 'w') as file:
        file.truncate(0)

    print(f"Contents of file '{file_path}' have been wiped.")

# Example usage
file_path = 'textfiles/wipe.txt'

wipe_file(file_path)

