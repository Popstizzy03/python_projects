def binary_to_decimal(binary_str):
    """
    Convert a binary string to a decimal number.
    
    :param binary_str: Binary number in string format (e.g., '1011')
    :return: Decimal representation of the binary number
    """
    try:
        decimal_number = int(binary_str, 2)
        return decimal_number
    except ValueError:
        return "Invalid binary number. Please enter a binary number using only 0s and 1s."

def decimal_to_binary(decimal_num):
    """
    Convert a decimal number to a binary string.
    
    :param decimal_num: Decimal number (e.g., 11)
    :return: Binary representation of the decimal number as a string
    """
    try:
        decimal_num = int(decimal_num)
        if decimal_num < 0:
            return "Invalid decimal number. Please enter a non-negative integer."
        binary_str = bin(decimal_num)[2:]
        return binary_str
    except ValueError:
        return "Invalid decimal number. Please enter a valid integer."

def main():
    print("Conversion Menu:")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        binary_str = input("Enter a binary number: ")
        result = binary_to_decimal(binary_str)
        print(f"Binary to Decimal: {binary_str} -> {result}")
    elif choice == '2':
        decimal_num = input("Enter a decimal number: ")
        result = decimal_to_binary(decimal_num)
        print(f"Decimal to Binary: {decimal_num} -> {result}")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
