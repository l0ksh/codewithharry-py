#!/usr/bin/python3

#text = 'This text  contains double spaces.'

#for i in text:
#    if text[i] == " " and text[i + 1] == " ":
#        print(f'The double spaces are at the following indexes:\n {i} \n {i+1}')
#        print('Helo')

def detect_double_spaces(text):
  """
  Detects double spaces in a string.

  Args:
    text: The string to be checked.

  Returns:
    A list of all the indexes of the double spaces in the string.
  """

  double_spaces = []
  for i in range(len(text) - 1):
    if text[i] == " " and text[i + 1] == " ":
      double_spaces.append(i)

  return double_spaces


if __name__ == "__main__":
  text = "This is a  string  with double spaces."
  double_spaces = detect_double_spaces(text)

  print("The double spaces in the string are at the following indexes:")
  for index in double_spaces:
    print(index)
