import sys

def decimal_to_hex(decimal_value):
    hex_chars = '0123456789ABCDEF'
    hexadecimal = ""
    num = decimal_value
    if num == 0:
        return "0"
    while num != 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16
    return hexadecimal

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            decimal_value = int(sys.argv[1])
            print(f"Converting {decimal_value} to Hex: {decimal_to_hex(decimal_value)}")
        except ValueError:
            print("Error: Input is not a valid integer.")
    else:
        print("Error: No input argument provided.")
