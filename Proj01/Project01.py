
    #######################################################
    #  Computer Project #1
    #
    #  Unit Converter
    #    prompt for distance in rods
    #    converts rods to different units as floats
    #    Outputs the distance in multiple units
    #    calculates time spent walking that distance
    ########################################################

Rods = input("Input rods: ")

Rods = float(Rods)
print("You input " + str(Rods) + " rods.")

print("Conversions")

Furlongs = round(float(Rods / 40) ,3)         # Converts Rods to Furlongs
Meters = round(float(Rods * 5.0292) , 3)      # Converts Rods to Meters        
Feet = round(float(Meters / .3048) ,3)        # Converts Meters to Feet
Miles = round(float(Meters / 1609.34)  , 3)   # Converts Meters to Miles
SpeedInRods = float(3.1 *320)/60              # Converts MpH to Rods per minute
Time = round(float(Rods / SpeedInRods) ,3)    # Divides distance by speed




print("Meters: " + str(Meters))
print("Feet: " + str(Feet))
print("Miles: " + str(Miles))
print("Furlongs: " + str(Furlongs))
print("Minutes to walk " + str(Rods) + " rods: " + str(Time))
#print("Minutes to walk " + str(Rods) + " Rods:" + )



