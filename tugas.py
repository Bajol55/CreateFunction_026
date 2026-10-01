    ### 1

def convert_temperature(value: float, unit: str):
    """
    Converts temperature between Celsius and Fahrenheit.
    
    Parameters:
        value (float): The temperature value to convert.
        unit (str): 'C' for Celsius, 'F' for Fahrenheit.
        
    Returns:
        tuple: (converted_value, target_unit)
    """
    unit = unit.upper().strip()
    
    if unit == 'C':
        # Celsius to Fahrenheit: (C * 9/5) + 32
        converted = (value * 9/5) + 32
        return converted, 'F'
    elif unit == 'F':
        # Fahrenheit to Celsius: (F - 32) * 5/9
        converted = (value - 32) * 5/9
        return converted, 'C'
    else:
        raise ValueError("Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit.")


# --- Examples ---
print(convert_temperature(0, 'C'))    # (32.0, 'F')
print(convert_temperature(100, 'C'))  # (212.0, 'F')
print(convert_temperature(32, 'F'))   # (0.0, 'C')
print(convert_temperature(98.6, 'F')) # (37.0, 'C')

    ### 2

luas_lingkaran = lambda r: 3.14 * r * r
r = int(input("Masukkan jari-jari lingkaran: "))
hasil = luas_lingkaran(r)
print("Luas lingkaran:", hasil)