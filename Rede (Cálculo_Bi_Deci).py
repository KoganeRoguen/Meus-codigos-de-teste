def binary_to_decimal(binary_value):
    binary_parts = binary_value.split(".")
    
    decimal_parts = []
    for part in binary_parts:
        decimal_parts.append(str(int(part, 2)))
        
    decimal_result = ".".join(decimal_parts)
    return decimal_result

while True:
    try:
        binary_input = input("Enter a binary number: ")
        decimal_result = binary_to_decimal(binary_input)
    except ValueError:
        print("Your input is not a binary number! Please try again")
    else:
        break

print(f"{decimal_result}")