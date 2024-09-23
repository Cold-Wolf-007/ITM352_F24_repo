# Create a list of trip durations and fares

tripDuration = [1.1, 0.8, 2.5, 2.6]
tripFares = ("$6.25", "$5.25", "$10.50", "$8.05")

#tripDict = {"miles": tripDuration,
        #    "fares": tripFares}

#print(tripDict)
#print(tripDict["miles"][2], tripDict["fares"][2])

#Create a new doctionary by zipping together the duration list and the fares tuple
newDict = dict(zip(tripDuration,tripFares))

#print("New dictionary:", newDict)
#print(f"Trip duration={tripDuration[2]} cost={newDict[tripDuration[2]]}" )

#trip_list = [{"duration": duration, "fare": fare} for duration, fare in newDict.items()]

trip_list = [
  {'duration': 1.1, 'fare': '$6.25'},
  {'duration': 0.8, 'fare': '$5.25'},
  {'duration': 2.5, 'fare': '$10.50'},
  {'duration': 2.6, 'fare': '$8.05'}
]
print("trip list:", trip_list)
print(f"Trip duration = {trip_list[2]['duration']} cost = {trip_list[2]['fare']}")