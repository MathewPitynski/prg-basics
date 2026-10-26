time_24 = input("Enter time (24-hour format): ")
hours_str, minutes_str = time_24.split(":")
hours = int(hours_str)

if hours == 0:
    print(f"Time in 12-hour format: 12:{minutes_str}am")
elif hours < 12:
    print(f"Time in 12-hour format: {hours}:{minutes_str}am")
elif hours == 12:
    print(f"Time in 12-hour format: 12:{minutes_str}pm")
else:
    print(f"Time in 12-hour format: {hours - 12}:{minutes_str}pm")