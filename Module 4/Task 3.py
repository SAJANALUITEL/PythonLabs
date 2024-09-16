smallest = None
largest = None

while True:
    str1 = input("enter the num:")

    if str1 == "":
        break
    try:
        str2 = int(str1)
        print(str2)
        if smallest is None or str2 < smallest:
            smallest = str2
        if largest is None or str2 > largest:
            largest = str2
    except ValueError:
        print("invalid input")
if smallest is not None and largest is not None:
    print("Smallest number:", samllest)
    print("Largest number:", largest)
else
    print("program end")
    