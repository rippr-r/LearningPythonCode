def verify_card_number(card_number):
    # This function checks if a card number is valid using the Luhn algorithm
    sum_of_odd_digits = 0
    # Reverse the card number so we can process digits from right to left
    card_number_reversed = card_number[::-1]
    # Take every other digit starting from the rightmost (now index 0 after reversing)
    odd_digits = card_number_reversed[::2]
    # Add up all odd-positioned digits (in the reversed number)
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    sum_of_even_digits = 0
    # Take every other digit starting from index 1 (second digit from the right originally)
    even_digits = card_number_reversed[1::2]
    # Process each even-positioned digit
    for digit in even_digits:
        number = int(digit) * 2  # Double the digit
        if number >= 10:
            # If doubling made it two digits, add the digits together (e.g., 12 → 1 + 2 = 3)
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
  
    # If total modulo 10 is 0, the card number is valid
    return total % 10 == 0
  
def main():
    card_number = '4111-1111-4555-1142'
    # Create a translation table to remove '-' and ' ' from the card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    # Apply the translation table to get only digits
    translated_card_number = card_number.translate(card_translation)
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')
      
main()
