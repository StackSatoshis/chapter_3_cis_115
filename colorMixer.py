# colorMixer.py
# Ryan Carroll
# CIS 115 NLE01
# Proves I know how to do this homework, with colors
#adding this

import turtle as t
wn = t.Screen()

color1 = input("Enter the first color\n Magenta, Yellow or Cyan: ")
color2 = input("Enter the second color\n Magenta, Yellow or Cyan: ")

if (color1.lower() == "magenta" and color2.lower() == "cyan") \
        or (color1.lower() == "cyan" and color2.lower() == "magenta"):
    t.bgcolor('purple')
    wn.addshape('turtle.gif')
    t.shape('turtle.gif')
    wn.mainloop()

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

elif color1.lower().lower() == color2.lower().lower():
    t.bgcolor(f"{color2}")
    wn.addshape('turtle.gif')
    t.shape('turtle.gif')
    wn.mainloop()

else:
    t.write("ERROR", move=False, align="left", font=("Arial", 30, "normal"))





