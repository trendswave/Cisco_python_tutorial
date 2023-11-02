# Create a list to store temperatures for 5 days, each with 24 hours
temps = [[0.0 for h in range(24)] for d in range(5)]

# Loop through each day to get temperature data from the user
for day in range(5):
    print(f"Day {day + 1}:")
    for hour in range(24):
        while True:
            try:
                temp = float(input(f"Enter temperature for hour {hour}: "))
                temps[day][hour] = temp
                break
            except ValueError:
                print("Please enter a valid temperature (numeric value).")

# Initialize the highest temperature to a very low value
highest = -1000.0

# Loop through the collected temperature data to find the highest temperature
for day_temps in temps:
    for temp in day_temps:
        if temp > highest:
            highest = temp

print("The highest temperature recorded is:", highest)
