gender = str(input("Enter your gender (male/female): "))
hm = float(input("Enter the haemoglobin value (g/l): "))

if gender == "male":
    if 134 <= hm <= 167:
        print("haemoglobin is normal")
    elif hm < 134 :
        print("haemoglobin is low")
    else :
        print("haemoglobin is high")
if gender == "female":
    if 117 <= hm <=155:
        print("haemoglobin is normal")
    elif hm < 117 :
        print("haemoglobin is low")
    else :
        print("haemoglobin is high")
        