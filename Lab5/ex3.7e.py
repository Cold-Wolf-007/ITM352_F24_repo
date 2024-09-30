# Create a list of dictionaries where each dictionary is a trip

import re


trips = [
    {'duration': 1.1, 'fare': 6.25},
    {'duration': 0.8, 'fare': 5.25},
    {'duration': 2.5, 'fare': 10.50},
    {'duration': 2.6, 'fare': 8.05}
]
# Use regex to convert the string fares to numeric values
for trip in trips:
    trip['fare'] = float(re.sub(r'\$(.*)', r'\1', trip['fare']))

print(trips)
print(f"The 3rd trip was {trips[2]['duration']} miles and cost ${trips[2]['fare']:0.2f}")