# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:27:14 2019

@author: Admin
"""

# Exercise 2

# Satellites:
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500
               }

# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]

sat_database.update({"GOES":2000,"worldview":0.31})

print("I have the following satellites in my database:")

# 2) print out all satellite names contained in the dictionary [2P]
    
for x in sat_database:
    print(x)

# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]

eingabe=input("From which satellite you like to know the resolution: ")

print(sat_database.get(eingabe))

# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]
if eingabe in sat_database.keys():
# 5) If the satellite name is in the database, print a meaningful message containing the satellite name and it's resolution [2P]
    #print("The resolution for", eingabe,"is",sat_database.get(eingabe))
    print("The resolution for {0} is {1:5.2f}.".format (eingabe,sat_database.get(eingabe)))
else:
    print("Your satellite is not in the dictionary - please try again!")

