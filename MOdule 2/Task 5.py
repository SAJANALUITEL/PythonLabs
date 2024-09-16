pounds_per_talent = 20
lots_per_pound = 32
grams_per_lot = 13.3
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
grams_from_talents = talents * pounds_per_talent * lots_per_pound * grams_per_lot
grams_from_pounds = pounds * lots_per_pound * grams_per_lot
grams_from_lot = lots * grams_per_lot
total_grams = grams_from_talents + grams_from_pounds + grams_from_lot
kilograms = int(total_grams / 1000)
remaining_grams = total_grams % 1000
print(f"\nThe weight in modern units:\n{kilograms} kilograms and {remaining_grams:.2f} grams.")
