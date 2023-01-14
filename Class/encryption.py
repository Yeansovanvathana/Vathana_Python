ciper_text = input('Enter the text: ')
shift = int(input('Enter the shift: '))

Text = ''
for i in ciper_text:
    if(i.islower()):
        Text += chr((ord(i) + shift - ord('a')) % 26 + ord('a'))
    elif (i.isupper()):
        Text += chr((ord(i) + shift - ord('A')) % 26 + ord('A'))
    elif (i.isdigit()):
        # x = int(i)
        # x = (x + shift) % 10
        # Text += str(x)
        Text += chr((ord(i) + shift - ord('0')) % 10 + ord('0'))
    else:
        Text += chr((ord(i) + shift - ord(' ')) % 15 + ord(' '))


print("Plain text is: " + ciper_text)
print("ciper_text is: " + Text)