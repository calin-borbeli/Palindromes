text = input("Enter text: ")
text = text.replace(" ", "")

if text:
    text = text.lower()
    l = len(text) - 1
    ispalindrome = True
    for i in range(0, int(l / 2)):
        if text[i] != text[l - i]:
            ispalindrome = False
            break

    if ispalindrome:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

else:
    print("It's not a palindrome")
