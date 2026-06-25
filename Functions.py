#  Calculate the area of a circle
def calculate_circle_area(radius):
    pi_value = 3.14159
    area = pi_value * (radius ** 2)
    return round(area, 2)

#  Calculate total due with tax
def calculate_total_due(money, tax_rate):
    if tax_rate > 1:
        tax_rate = tax_rate / 100
    total = money + (money * tax_rate)
    return round(total, 2)

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return round(celsius, 2)

# Area of a Circle
radius_input = float(input("Enter circle radius: "))
area_result = calculate_circle_area(radius_input)
print(f"Output Area: {area_result}\n")

# Taxes
money_input = float(input("Enter money amount: "))
tax_input = float(input("Enter tax rate (Enter number for that percentage like 6 for 6%): "))
tax_result = calculate_total_due(money_input, tax_input)
print(f"Output Total Due: {tax_result}\n")

# Temperature Conversion
f_input = float(input("Enter temperature in Fahrenheit: "))
c_result = convert_to_celsius(f_input)
print(f"Output Celsius: {c_result}\n")
