def is_palindrome(word):
  if word == word[::-1]:
    print("It's a palindrome!")
  else:
    print("It's not a palindrome.")

if __name__ == "__main__":
  is_palindrome("racecar")