def timeConversion(s):
    hour = int(s[:2])
    period = s[-2:]

    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour = hour + 12

    return f"{hour:02d}" + s[2:8]


s = input("Enter time in 12-hour format: ")

result = timeConversion(s)

print("24-hour format:", result)