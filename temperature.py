"""
Module Name: temperature
Author: Uday Sharma
"""

def celsius_to_kelvin(c):
    return c + 273.15

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32

def show_menu():
    print("\n" + "=" * 55)
    print("           🌡️   TEMPERATURE CALCULATOR  ⁠🌡️")
    print("=" * 55)
    print("1. Celsius ➜ Fahrenheit")
    print("2. Celsius ➜ Kelvin")
    print("3. Fahrenheit ➜ Celsius")
    print("4. Fahrenheit ➜ Kelvin")
    print("5. Kelvin ➜ Celsius")
    print("6. Kelvin ➜ Fahrenheit")
    print("7. Exit")
    print("=" * 55)

def num():
    return float(input("Enter Temperature: "))