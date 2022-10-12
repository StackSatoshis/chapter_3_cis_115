# colorMixer.py
# Ryan Carroll
# CIS 115 NLE01
# Determines color based on CMYK. Print's results to Turtle.

import turtle as t # Import turtle module

color1 = input("Enter the first color\n Magenta, Yellow or Cyan: ")   # Defines variables
color2 = input("Enter the second color\n Magenta, Yellow or Cyan: ")  #
wn = t.Screen() # defines turtle screen

if (color1.lower() == "magenta" and color2.lower() == "cyan") \
        or (color1.lower() == "cyan" and color2.lower() == "magenta"):   # Comparing strings
    t.bgcolor('purple')        # Changes the background color to Purple
    wn.addshape('turtle.gif')  # Adds gfx's
    t.shape('turtle.gif')      #
    wn.mainloop()              # Tells turtle window to wait for user input (Error handling)

elif (color1.lower() == "magenta" and color2.lower() == "yellow") \
        or (color1.lower() == "yellow" and color2.lower() == "magenta"):
    t.bgcolor("orange")
    wn.addshape('turtle.gif')
    t.shape('turtle.gif')
    wn.mainloop()

elif (color1.lower() == "cyan" and color2.lower() == "yellow") \
        or (color1.lower() == "yellow" and color2.lower() == "cyan"):
    t.bgcolor("green")
    wn.addshape('turtle.gif')
    t.shape('turtle.gif')
    wn.mainloop()

elif color1.lower() == color2.lower():  # Compares if the colors are equal
    t.bgcolor(f"{color2}")     # Changes the background to color selected above
    wn.addshape('turtle.gif')
    t.shape('turtle.gif')
    wn.mainloop()

else:
    t.write("ERROR", move=False, align="left", font=("Arial", 30, "normal")) # Draws the error message in
    wn.mainloop()                                                            # turtle window






