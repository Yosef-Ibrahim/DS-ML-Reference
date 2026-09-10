# =============================================================================
# 🐍 Python Fundamentals for Data Engineering — Runnable Python Script
# Author: Youssef Ibrahim Mohamed Soliman
# GitHub: https://github.com/Yosef-Ibrahim
# Email:  youssefibrahimelisely@gmail.com
# =============================================================================

import sys

# Ensure UTF-8 output encoding for Windows terminals
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def demonstrate_strings():
    print("--- 1. String Operations & Formatting ---")
    first_name = "Youssef"
    last_name = "Ibrahim"
    full_name = f"{first_name} {last_name}"
    
    print(f"Full Name: {full_name}")
    print(f"Uppercase: {full_name.upper()}")
    print(f"Lowercase: {full_name.lower()}")
    print("Escaped Tab & Newline:\n\tData Engineering\n\tPython Reference\n")

def demonstrate_numbers():
    print("--- 2. Numbers & Numerical Operators ---")
    print(f"Addition (2 + 3): {2 + 3}")
    print(f"Exponentiation (2 ** 3): {2 ** 3}")
    print(f"Float Division (7 / 2): {7 / 2}")
    print(f"Floor Division (7 // 2): {7 // 2}")
    print(f"Modulo (7 % 2): {7 % 2}\n")

def demonstrate_lists():
    print("--- 3. List Manipulations ---")
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(f"Initial List: {motorcycles}")
    
    motorcycles.append('ducati')
    print(f"After Append: {motorcycles}")
    
    motorcycles.insert(0, 'bmw')
    print(f"After Insert at Index 0: {motorcycles}")
    
    popped_item = motorcycles.pop()
    print(f"Popped Item: {popped_item}")
    print(f"List After Pop: {motorcycles}")
    
    motorcycles.sort()
    print(f"Sorted List: {motorcycles}\n")

def demonstrate_numerical_lists():
    print("--- 4. Numerical Lists & List Comprehensions ---")
    numbers = list(range(1, 11))
    print(f"Range 1-10: {numbers}")
    print(f"Min: {min(numbers)}, Max: {max(numbers)}, Sum: {sum(numbers)}")
    
    squares = [val**2 for val in range(1, 11)]
    print(f"Squares (List Comprehension): {squares}")
    
    even_squares = [val**2 for val in range(1, 11) if val % 2 == 0]
    print(f"Even Squares (Filtered Comprehension): {even_squares}\n")

def main():
    print("[+] Executing Python Fundamentals Reference Script...\n")
    demonstrate_strings()
    demonstrate_numbers()
    demonstrate_lists()
    demonstrate_numerical_lists()
    print("[SUCCESS] Python Fundamentals Script Completed Successfully!")

if __name__ == "__main__":
    main()
