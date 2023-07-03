#!/usr/bin/python3

def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            for line in source:
                destination.write(line)

    print(f"File '{source_file}' copied to '{destination_file}'.")

# Example usage
source_file = 'textfiles/original.txt'
destination_file = 'textfiles/copy.txt'

copy_file(source_file, destination_file)
