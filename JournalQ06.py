import sys

if len(sys.argv) == 2:
    text = sys.argv[1]
else:
    text = "waw"

if text == text[::-1]:
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")
