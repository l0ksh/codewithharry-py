#!/usr/bin/python3

def detect_and_remove_double_spaces(text):
  """
  Detects and removes double spaces in a string.

  Args:
    text: The string to be checked.

  Returns:
    The string with the double spaces removed.
  """

  new_text = ""
  for i in range(len(text)):
    if text[i] != " ":
      new_text += text[i]
    elif i + 1 < len(text) and text[i + 1] == " ":
      continue

  return new_text


if __name__ == "__main__":
  text = "This is  a string with double spaces."
  new_text = detect_and_remove_double_spaces(text)

  print("The original string:")
  print(text)

  print("The new string without double spaces:")
  print(new_text)
