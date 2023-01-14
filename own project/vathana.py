def min_keystrokes(S):
    # Initialize the displayed number and the keystroke count to 0
    num = 0
    count = 0
    # Iterate through the digits of S
    while S > 0:
        # Get the most significant digit
        digit = S // 10
        # Check if the digit is 0 or 00
        if digit == 0:
            # Check if the displayed number is divisible by 100
            if num % 100 == 0:
                # Increment the keystroke count and update the displayed number
                count += 1
                num *= 100
            else:
                # Increment the keystroke count and update the displayed number
                count += 2
                num = num * 10 + digit
        else:
            # Increment the keystroke count and update the displayed number
            count += 1
            num = num * 10 + digit
        # Update S to remove the most significant digit
        S = S % 10
    return count

# Test the function
S = int(input())
print(min_keystrokes(S))  # Output: 4
