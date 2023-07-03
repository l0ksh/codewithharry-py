#!/usr/bin/python3

def find_python_in_log(log_file):
    with open(log_file, 'r') as f:
        lines = f.readlines()
    python_lines = []
    for line_num, line in enumerate(lines, start=1):
        if 'ubuntu' in line.lower():
            python_lines.append(line_num)

    return python_lines

# Example usage
log_file = 'textfiles/auth.log'
python_lines = find_python_in_log(log_file)

if python_lines:
    print("The log file contains 'ubuntu' at line(s):", python_lines)
else:
    print("The log file does not contain 'python'.")
