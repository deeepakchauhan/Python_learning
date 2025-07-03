# temperature conversion

unit = input("temperature is in Celsius or Kelvin (C/K):")
temp = float(input("enter the temperature:"))


if unit == "C":
    temp = temp + 273
    print(temp)
elif unit == "K":
    temp = temp - 273
    print(temp)
else:
    print(f"{unit} is an invalid unit of measurement")
