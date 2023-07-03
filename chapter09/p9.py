#!/usr/bin/python3

def compare_files(file1, file2):
    with open(file1, 'r') as f1:
        content1 = f1.read()

    with open(file2, 'r') as f2:
        content2 = f2.read()

    if content1 == content2:
        print("The files are identical.")
    else:
        print("The files are not identical.")

# Example usage
file1 = 'textfiles/file1.txt'
file2 = 'textfiles/file2.txt'

compare_files(file1, file2)

