def gallons_to_liters(gallons):
    return gallons * 3.78541 # 1 gallon = 3.78541 liters

def main():
    while True:
        gallons = float(input("Enter the quantity of gasoline in gallons: "))
        if gallons < 0:
            print("Negative value entered.")
            break
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is {liters:,2f} liters.")
if __name__ == "__main__":
    main()
    