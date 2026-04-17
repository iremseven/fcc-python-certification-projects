# Project: Travel Weather Planner
# Source: freeCodeCamp Python Certification
# Description: A script that determines commute possibility based on weather, distance, and vehicle availability using conditional logic.

distance_mi = 6
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)
  
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
      
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
      
elif distance_mi > 6:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
