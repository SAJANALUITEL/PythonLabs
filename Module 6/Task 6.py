import math
def pizza_value(diameter, price):
    return price / (math.pi * (diameter/2) ** 2)
pizza_1_price = float(input("Enter the price of pizza1: "))
pizza_1_diameter = float(input("Enter the diameter of pizza1 in centimeters: "))
pizza_2_diameter = float(input("Enter the price of pizza2: "))
pizza_2_diameter = float(input("Enter the diameter of pizza2 in centimeters: "))
if pizza_value(pizza_1_diameter, pizza_1_price) > pizza_value(pizza_2_diameter, pizza_2_price):
    print ("The pizza2 is better value")
else:
    print("pizza1 is better value")
