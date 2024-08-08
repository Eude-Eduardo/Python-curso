def isPalindrome(str):
  if str == str[::-1]:
    return True
  else:
    return False

def main():
  userInput = input("Enter a WORD to be tested as a palindrome:").lower()

  if (isPalindrome(userInput)):
    print(userInput.capitalize() + " is a palindrome!")
  else:
    print(userInput.capitalize() + " is NOT a palindrome!")

if __name__ == "__main__":
    main()
