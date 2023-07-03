#!/usr/bin/python3

import os

def rename_file(old_file_name, new_file_name):
  """Renames a file.

  Args:
    old_file_name: The old file name.
    new_file_name: The new file name.

  Returns:
    True if the file was renamed successfully, False otherwise.
  """

  if os.path.exists(old_file_name):
    os.rename(old_file_name, new_file_name)
    return True
  else:
    return False

if __name__ == "__main__":
  old_file_name = "textfiles/python3.py"
  new_file_name = "textfiles/renamed_by_python.py"

  if rename_file(old_file_name, new_file_name):
    print("File renamed successfully.")
  else:
    print("File could not be renamed.")

