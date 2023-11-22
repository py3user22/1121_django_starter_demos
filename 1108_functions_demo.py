#!/bin/python3


# functions demo 1108

def rocket_parts():
    print("payload, propellant, structure")

rocket_parts()
print("----------------------->\n")
"""
# call method
# rocket_parts()                          # payload, propellant, structure

assign to variable if need to use a value the func. is returning
if returns None then dont need to assign to variable


output1 = rocket_parts()
print(output1)

ex2.

str()           # returns empty string  >> ''

str(15)         # '15'

"""

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"


dest1 = distance_from_earth("Moon")
print(dest1)                        # 238,855

distance_from_earth("Saturn")       # Unable to compute to that destination

print("----------------------->\n")

"""
Multiple required arguments
"""

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24


total_days = days_to_complete(238855, 75)
round(total_days)           # 133

print("----------------------->\n")

def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank}"""

    print(output)

generate_report(80, 70, 75)

"""
Create a report generation function
Your spaceship has three tanks: Main, External and Hydrogen. You want to create an app to display the amount of fuel in each tank, and the average amount of fuel between the three tanks. Because you wish to reuse this code in other projects, you want to create a function with the logic.
Create a function named generate_report. The function will take three parameters named main_tank, external_tank and hydrogen_tank. When run, the function will display output which resembles the following:
"""
